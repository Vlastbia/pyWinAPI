# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.
from __future__ import print_function, absolute_import
import sys
import requests
import os
from code_converter import win_functions

base_path = os.path.dirname(__file__)

functions_file = os.path.join(base_path, 'win_functions.py')
not_found_file = os.path.join(base_path, 'win_functions_not_found.txt')

if not os.path.exists(not_found_file):
    with open(not_found_file, 'w') as f:
        f.write('')

with open(not_found_file, 'r') as f:
    not_found_funcs = list(
        itm.strip() for itm in f.read().split('\n') if itm.strip()
    )

NOT_ALLOWED_PATTERN = [
    '_Post_',
    '_Success_',
    '_Struct_',
    '_Field_',
    '_Opt_',
    '_When_',
    'ctypes',
    '_IRQL_',
    '_At_',
    '_Out_',
    '_In_',
    '_Byteswap_',
    '_Bytes_',
    '_MM_'
]


def write_functions():
    from io import StringIO
    output = StringIO()

    for key, value in known_dlls.items():
        key = key.replace('.', '__').decode('utf-8')
        output.write(key + ' = [\n')
        for item in value:
            output.write("    '{0}',\n".format(item).decode('utf-8'))
        output.write(u']\n\n')

    output.seek(0)

    with open(functions_file, 'w') as f:
        f.write(output.read())


known_dlls = {}

for key, value in win_functions.__dict__.items():
    if key.startswith('__'):
        continue
    known_dlls[key.replace('__', '.')] = value[:]


TEMPLATE_DLL_1 = '''{indent}{dll_lower} = ctypes.windll.{dll_upper}'''
TEMPLATE_DLL_2 = '''{indent}{dll_lower} = (
{indent}    ctypes.windll.{dll_upper}
{indent})'''

TEMPLATE_ORIGINAL = '''{original_lines}'''
TEMPLATE_FUNCTION_1 = '''{indent}{func_name} = {dll_lower}.{func_name}'''
TEMPLATE_FUNCTION_2 = '''{indent}{func_name} = (
{indent}    {dll_lower}.{func_name}
{indent})'''

TEMPLATE_RESTYPE_1 = '''{indent}{func_name}.restype = {return_value}
'''
TEMPLATE_RESTYPE_2 = '''{indent}{func_name}.restype = (
{indent}    {return_value}
{indent})
'''

NOT_ALLOWED_PUNC = '#/<>()=*+-\\!"\',%^$@&|{}[];:.?` \n'


def print_not_found():
    output = '\n'.join(not_found_funcs)
    with open(not_found_file, 'w') as f:
        f.write(output)


def get_dll_name(func):
    if func.startswith('Gdip'):
        return 'GdiPlus'
    for item in list(NOT_ALLOWED_PUNC):
        if item in func:
            return None
    if func in not_found_funcs:
        return None
    if func.startswith('__'):
        return None

    for item in NOT_ALLOWED_PATTERN:
        if item in func:
            return None
        if item.lower() in func:
            return None

    sys.stderr.write('locating "{0}" on docs.microsoft.com'.format(func))

    response = requests.get(
        'https://docs.microsoft.com/api/search',
        params={'search': func, 'locale': 'en', '$top': '1'}
    )
    response = response.json()
    results = response['results']
    if results:
        url = results[0]['url']
        response = requests.get(url).content
        if '<td><strong>DLL</strong></td>' in response:
            sys.stderr.write(' --- FOUND\n')
            response = response.split('<td><strong>DLL</strong></td>')[1]
            response = response.split('/td>')[0]
            dll = response.split('>')[-1]
            dll = dll.split(' ')[0]
            return os.path.splitext(dll)[0]

    not_found_funcs.append(func)
    sys.stderr.write(' --- NOT FOUND\n')


def parse_dll(indent, data, found_dlls):
    new_data = []
    for d in data:
        d = d.strip()
        if d.endswith(' ('):
            d = d[:-2] + '('
        new_data += [d]

    data = new_data
    new_data = ' '.join(data).replace(';', '')
    pos_funcs = new_data.split(' ')
    search_funcs = []
    for func in pos_funcs:
        if func.startswith('(') or func.endswith(')'):
            continue
        if '*' in func:
            continue
        if '(' not in func:
            continue

        func = func.split('(')[0].strip()
        search_funcs += [func]

    for pos_func in search_funcs:
        for dll, known_funcs in known_dlls.items():
            if pos_func in known_funcs:
                break
        else:
            continue

        break
    else:
        try:
            pos_func = search_funcs[-1]
        except IndexError:
            return ''
        dll = get_dll_name(pos_func)
        if dll is None:
            return ''

        if dll not in known_dlls:
            for k_dll in known_dlls.keys():
                if k_dll.lower() == dll.lower():
                    known_dlls[dll] = known_dlls[k_dll][:]
                    del known_dlls[k_dll]
                    break
            else:
                known_dlls[dll] = [pos_func]
        known_dlls[dll] += [pos_func]

    lines = []

    if dll not in found_dlls:
        template = TEMPLATE_DLL_1.format(
            indent=indent,
            dll_lower=dll.lower(),
            dll_upper=dll.upper(),
        )

        if len(template) > 79:
            template = TEMPLATE_DLL_2.format(
                indent=indent,
                dll_lower=dll.lower(),
                dll_upper=dll.upper(),
            )

        template += '\n'

        found_dlls += [dll]

    else:
        template = ''

    return_values = new_data.split(pos_func)[0]
    return_values = list(item for item in return_values.split(' ') if item)
    if len(return_values) >= 3:
        return_value = return_values[-2]
    elif return_values:
        return_value = return_values[-1]
    else:
        return ''

    if return_value == 'NTKERNELAPI':
        return_value = return_values[-1]

    if return_value == '*':
        return_value = 'POINTER(' + return_values[-2].strip() + ')'

    original_lines = '\n' + '\n'.join(indent + '# ' + ln for ln in data)

    func_template = TEMPLATE_FUNCTION_1.format(
        indent=indent,
        func_name=pos_func,
        dll_lower=dll.lower()
    )
    if len(func_template) > 79:
        func_template = TEMPLATE_FUNCTION_2.format(
            indent=indent,
            func_name=pos_func,
            dll_lower=dll.lower()
        )

    if '(' in return_value and ')' in return_value:
        return_value = return_value.split('(', 1)[-1]
        return_value = return_value.split(')', 1)[0]

    if return_value == 'STDAPI':
        lines += [
            template,
            TEMPLATE_ORIGINAL.format(original_lines=original_lines),
            func_template,
        ]
    else:
        res_template = TEMPLATE_RESTYPE_1.format(
            indent=indent,
            func_name=pos_func,
            return_value=return_value
        )

        if len(res_template) > 79:
            res_template = TEMPLATE_RESTYPE_2.format(
                indent=indent,
                func_name=pos_func,
                return_value=return_value
            )

        lines += [
            template,
            TEMPLATE_ORIGINAL.format(original_lines=original_lines),
            func_template,
            res_template
        ]

    return '\n'.join(lines)
