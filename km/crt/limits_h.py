

CHAR_BIT = 0x00000008
SCHAR_MIN = -128
SCHAR_MAX = 0x0000007F
UCHAR_MAX = 0x000000FF
CHAR_MIN = SCHAR_MIN
CHAR_MAX = SCHAR_MAX
MB_LEN_MAX = 0x00000005
SHRT_MIN = -32768
SHRT_MAX = 0x00007FFF
USHRT_MAX = 0x0000FFFF
INT_MIN = -2147483647 - 1
INT_MAX = 0x7FFFFFFF
UINT_MAX = 0xFFFFFFFF
LONG_MIN = -2147483647 - 1
LONG_MAX = 0x7FFFFFFF
ULONG_MAX = 0xFFFFFFFF
LLONG_MAX = 9223372036854775807
LLONG_MIN = -9223372036854775807 - 1
ULLONG_MAX = 0xFFFFFFFFFFFFFFFF
_I8_MIN = -127 - 1
_I8_MAX = 127
_UI8_MAX = 0x000FF
_I16_MIN = -32767 - 1
_I16_MAX = 32767
_UI16_MAX = 0xFFFF
_I32_MIN = -2147483647 - 1
_I32_MAX = 2147483647
_UI32_MAX = 0xFFFFFFFF
_I64_MIN = -9223372036854775807 - 1
_I64_MAX = 9223372036854775807
_UI64_MAX = 0xFFFFFFFFFFFFFFFF
_I128_MIN = -170141183460469231731687303715884105727 - 1
_I128_MAX = 170141183460469231731687303715884105727
_UI128_MAX = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
SIZE_MAX = _UI64_MAX
RSIZE_MAX = SIZE_MAX

__all__ = (
    'SCHAR_MIN', '_I128_MIN', 'LONG_MIN', 'CHAR_MAX', 'UCHAR_MAX', '_I16_MAX',
    'USHRT_MAX', '_I32_MAX', '_I64_MAX', 'LONG_MAX', '_UI16_MAX', '_I8_MIN',
    '_I128_MAX', 'CHAR_BIT', 'SHRT_MIN', '_I8_MAX', 'RSIZE_MAX', 'SIZE_MAX',
    'UINT_MAX', '_UI32_MAX', '_I64_MIN', '_UI8_MAX', '_UI64_MAX', 'LLONG_MIN',
    '_UI128_MAX', 'ULLONG_MAX', 'CHAR_MIN', 'LLONG_MAX', 'INT_MIN', 'INT_MAX',
    '_I16_MIN', 'ULONG_MAX', 'SHRT_MAX', 'MB_LEN_MAX', 'SCHAR_MAX',
    '_I32_MIN',
)
