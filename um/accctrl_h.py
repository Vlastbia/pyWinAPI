

import ctypes
from shared.wtypes_h import * # NOQA
from shared.winapifamily_h import * # NOQA


AccFree = VOID


class _SE_OBJECT_TYPE(ENUM):
    SE_UNKNOWN_OBJECT_TYPE = 0
    SE_FILE_OBJECT = 1
    SE_SERVICE = 2
    SE_PRINTER = 3
    SE_REGISTRY_KEY = 4
    SE_LMSHARE = 5
    SE_KERNEL_OBJECT = 6
    SE_WINDOW_OBJECT = 7
    SE_DS_OBJECT = 8
    SE_DS_OBJECT_ALL = 9
    SE_PROVIDER_DEFINED_OBJECT = 10
    SE_WMIGUID_OBJECT = 11
    SE_REGISTRY_WOW64_32KEY = 12
    SE_REGISTRY_WOW64_64KEY = 13


SE_OBJECT_TYPE = _SE_OBJECT_TYPE


class _TRUSTEE_TYPE(ENUM):
    TRUSTEE_IS_UNKNOWN = 0
    TRUSTEE_IS_USER = 1
    TRUSTEE_IS_GROUP = 2
    TRUSTEE_IS_DOMAIN = 3
    TRUSTEE_IS_ALIAS = 4
    TRUSTEE_IS_WELL_KNOWN_GROUP = 5
    TRUSTEE_IS_DELETED = 6
    TRUSTEE_IS_INVALID = 7
    TRUSTEE_IS_COMPUTER = 8


TRUSTEE_TYPE = _TRUSTEE_TYPE


class _TRUSTEE_FORM(ENUM):
    TRUSTEE_IS_SID = 0
    TRUSTEE_IS_NAME = 1
    TRUSTEE_BAD_FORM = 2
    TRUSTEE_IS_OBJECTS_AND_SID = 3
    TRUSTEE_IS_OBJECTS_AND_NAME = 4


TRUSTEE_FORM = _TRUSTEE_FORM


class _MULTIPLE_TRUSTEE_OPERATION(ENUM):
    NO_MULTIPLE_TRUSTEE = 0
    TRUSTEE_IS_IMPERSONATE = 1


MULTIPLE_TRUSTEE_OPERATION = _MULTIPLE_TRUSTEE_OPERATION



class _OBJECTS_AND_SID(ctypes.Structure):
    _fields_ = [
        ('ObjectsPresent', DWORD),
        ('ObjectTypeGuid', GUID),
        ('InheritedObjectTypeGuid', GUID),
        (' pSid', POINTER(SID)),
    ]


OBJECTS_AND_SID = _OBJECTS_AND_SID
POBJECTS_AND_SID = POINTER(_OBJECTS_AND_SID)



class _OBJECTS_AND_NAME_A(ctypes.Structure):
    _fields_ = [
        ('ObjectsPresent', DWORD),
        ('ObjectType', SE_OBJECT_TYPE),
        ('ObjectTypeName', LPSTR),
        ('InheritedObjectTypeName', LPSTR),
        ('ptstrName', LPSTR),
    ]


OBJECTS_AND_NAME_A = _OBJECTS_AND_NAME_A
POBJECTS_AND_NAME_A = POINTER(_OBJECTS_AND_NAME_A)



class _OBJECTS_AND_NAME_W(ctypes.Structure):
    _fields_ = [
        ('ObjectsPresent', DWORD),
        ('ObjectType', SE_OBJECT_TYPE),
        ('ObjectTypeName', LPWSTR),
        ('InheritedObjectTypeName', LPWSTR),
        ('ptstrName', LPWSTR),
    ]


OBJECTS_AND_NAME_W = _OBJECTS_AND_NAME_W
POBJECTS_AND_NAME_W = POINTER(_OBJECTS_AND_NAME_W)


OBJECTS_AND_NAME_ = OBJECTS_AND_NAME_W
POBJECTS_AND_NAME_ = POBJECTS_AND_NAME_W


class _TRUSTEE_A(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('ptstrName', LPSTR),
            ('pSid', POINTER(SID)),
            ('pObjectsAndSid', POINTER(OBJECTS_AND_SID)),
            ('pObjectsAndName', POINTER(OBJECTS_AND_NAME_A)),
        ]

    _anonymous_ = ('_Union_0', )


_TRUSTEE_A._fields_ = [
    ('pMultipleTrustee', POINTER(_TRUSTEE_A)),
    ('MultipleTrusteeOperation', MULTIPLE_TRUSTEE_OPERATION),
    ('TrusteeForm', TRUSTEE_FORM),
    ('TrusteeType', TRUSTEE_TYPE),
    ('_Union_0', _TRUSTEE_A._Union_0),
    ('ptstrName', LPCH),
]


TRUSTEE_A = _TRUSTEE_A
PTRUSTEE_A = POINTER(_TRUSTEE_A)
TRUSTEEA = _TRUSTEE_A
PTRUSTEEA = POINTER(_TRUSTEE_A)


class _TRUSTEE_W(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('ptstrName', LPWSTR),
            ('pSid', POINTER(SID)),
            ('pObjectsAndSid', POINTER(OBJECTS_AND_SID)),
            ('pObjectsAndName', POINTER(OBJECTS_AND_NAME_W)),
        ]

    _anonymous_ = ('_Union_0', )


_TRUSTEE_W._fields_ = [
    ('pMultipleTrustee', POINTER(_TRUSTEE_W)),
    ('MultipleTrusteeOperation', MULTIPLE_TRUSTEE_OPERATION),
    ('TrusteeForm', TRUSTEE_FORM),
    ('TrusteeType', TRUSTEE_TYPE),
    ('_Union_0', _TRUSTEE_W._Union_0),
    ('ptstrName', LPWCH),
]

TRUSTEE_W = _TRUSTEE_W
PTRUSTEE_W = POINTER(_TRUSTEE_W)
TRUSTEEW = _TRUSTEE_W
PTRUSTEEW = POINTER(_TRUSTEE_W)


TRUSTEE_ = TRUSTEE_W
PTRUSTEE_ = PTRUSTEE_W
TRUSTEE = TRUSTEEW
PTRUSTEE = PTRUSTEEW


class _ACCESS_MODE(ENUM):
    NOT_USED_ACCESS = 0
    GRANT_ACCESS = 1
    SET_ACCESS = 2
    DENY_ACCESS = 3
    REVOKE_ACCESS = 4
    SET_AUDIT_SUCCESS = 5
    SET_AUDIT_FAILURE = 6


ACCESS_MODE = _ACCESS_MODE


NO_INHERITANCE = 0x00000000
SUB_OBJECTS_ONLY_INHERIT = 0x00000001
SUB_CONTAINERS_ONLY_INHERIT = 0x00000002
SUB_CONTAINERS_AND_OBJECTS_INHERIT = 0x00000003
INHERIT_NO_PROPAGATE = 0x00000004
INHERIT_ONLY = 0x00000008
INHERITED_ACCESS_ENTRY = 0x00000010
INHERITED_PARENT = 0x10000000
INHERITED_GRANDPARENT = 0x20000000


class _EXPLICIT_ACCESS_A(ctypes.Structure):
    _fields_ = [
        ('grfAccessPermissions', DWORD),
        ('grfAccessMode', ACCESS_MODE),
        ('grfInheritance', DWORD),
        ('Trustee', TRUSTEE_A),
    ]


EXPLICIT_ACCESS_A = _EXPLICIT_ACCESS_A
PEXPLICIT_ACCESS_A = POINTER(_EXPLICIT_ACCESS_A)
EXPLICIT_ACCESSA = _EXPLICIT_ACCESS_A
PEXPLICIT_ACCESSA = POINTER(_EXPLICIT_ACCESS_A)


class _EXPLICIT_ACCESS_W(ctypes.Structure):
    _fields_ = [
        ('grfAccessPermissions', DWORD),
        ('grfAccessMode', ACCESS_MODE),
        ('grfInheritance', DWORD),
        ('Trustee', TRUSTEE_W),
    ]


EXPLICIT_ACCESS_W = _EXPLICIT_ACCESS_W
PEXPLICIT_ACCESS_W = POINTER(_EXPLICIT_ACCESS_W)
EXPLICIT_ACCESSW = _EXPLICIT_ACCESS_W
PEXPLICIT_ACCESSW = POINTER(_EXPLICIT_ACCESS_W)


EXPLICIT_ACCESS_ = EXPLICIT_ACCESS_W
PEXPLICIT_ACCESS_ = PEXPLICIT_ACCESS_W
EXPLICIT_ACCESS = EXPLICIT_ACCESSW
PEXPLICIT_ACCESS = PEXPLICIT_ACCESSW

ACCCTRL_DEFAULT_PROVIDERA = "Windows NT Access Provider"
ACCCTRL_DEFAULT_PROVIDERW = "Windows NT Access Provider"
ACCCTRL_DEFAULT_PROVIDER = ACCCTRL_DEFAULT_PROVIDERW
# ACCCTRL_DEFAULT_PROVIDER = ACCCTRL_DEFAULT_PROVIDERA

ACCESS_RIGHTS = ULONG
PACCESS_RIGHTS = POINTER(ULONG)
INHERIT_FLAGS = ULONG
PINHERIT_FLAGS = POINTER(ULONG)


class _ACTRL_ACCESS_ENTRYA(ctypes.Structure):
    _fields_ = [
        ('Trustee', TRUSTEE_A),
        ('fAccessFlags', ULONG),
        ('Access', ACCESS_RIGHTS),
        ('ProvSpecificAccess', ACCESS_RIGHTS),
        ('Inheritance', INHERIT_FLAGS),
        ('lpInheritProperty', LPSTR),
    ]


ACTRL_ACCESS_ENTRYA = _ACTRL_ACCESS_ENTRYA
PACTRL_ACCESS_ENTRYA = POINTER(_ACTRL_ACCESS_ENTRYA)


class _ACTRL_ACCESS_ENTRYW(ctypes.Structure):
    _fields_ = [
        ('Trustee', TRUSTEE_W),
        ('fAccessFlags', ULONG),
        ('Access', ACCESS_RIGHTS),
        ('ProvSpecificAccess', ACCESS_RIGHTS),
        ('Inheritance', INHERIT_FLAGS),
        ('lpInheritProperty', LPWSTR),
    ]


ACTRL_ACCESS_ENTRYW = _ACTRL_ACCESS_ENTRYW
PACTRL_ACCESS_ENTRYW = POINTER(_ACTRL_ACCESS_ENTRYW)


ACTRL_ACCESS_ENTRY = ACTRL_ACCESS_ENTRYW
PACTRL_ACCESS_ENTRY = PACTRL_ACCESS_ENTRYW


class _ACTRL_ACCESS_ENTRY_LISTA(ctypes.Structure):
    _fields_ = [
        ('cEntries', ULONG),
        ('pAccessList', POINTER(ACTRL_ACCESS_ENTRYA)),
    ]


ACTRL_ACCESS_ENTRY_LISTA = _ACTRL_ACCESS_ENTRY_LISTA
PACTRL_ACCESS_ENTRY_LISTA = POINTER(_ACTRL_ACCESS_ENTRY_LISTA)


class _ACTRL_ACCESS_ENTRY_LISTW(ctypes.Structure):
    _fields_ = [
        ('cEntries', ULONG),
        ('pAccessList', POINTER(ACTRL_ACCESS_ENTRYW)),
    ]


ACTRL_ACCESS_ENTRY_LISTW = _ACTRL_ACCESS_ENTRY_LISTW
PACTRL_ACCESS_ENTRY_LISTW = POINTER(_ACTRL_ACCESS_ENTRY_LISTW)


ACTRL_ACCESS_ENTRY_LIST = ACTRL_ACCESS_ENTRY_LISTW
PACTRL_ACCESS_ENTRY_LIST = PACTRL_ACCESS_ENTRY_LISTW


class _ACTRL_PROPERTY_ENTRYA(ctypes.Structure):
    _fields_ = [
        ('lpProperty', LPSTR),
        ('pAccessEntryList', PACTRL_ACCESS_ENTRY_LISTA),
        ('fListFlags', ULONG),
    ]


ACTRL_PROPERTY_ENTRYA = _ACTRL_PROPERTY_ENTRYA
PACTRL_PROPERTY_ENTRYA = POINTER(_ACTRL_PROPERTY_ENTRYA)



class _ACTRL_PROPERTY_ENTRYW(ctypes.Structure):
    _fields_ = [
        ('lpProperty', LPWSTR),
        ('pAccessEntryList', PACTRL_ACCESS_ENTRY_LISTW),
        ('fListFlags', ULONG),
    ]


ACTRL_PROPERTY_ENTRYW = _ACTRL_PROPERTY_ENTRYW
PACTRL_PROPERTY_ENTRYW = POINTER(_ACTRL_PROPERTY_ENTRYW)


ACTRL_PROPERTY_ENTRY = ACTRL_PROPERTY_ENTRYW
PACTRL_PROPERTY_ENTRY = PACTRL_PROPERTY_ENTRYW


class _ACTRL_ALISTA(ctypes.Structure):
    _fields_ = [
        ('cEntries', ULONG),
        ('pPropertyAccessList', PACTRL_PROPERTY_ENTRYA),
    ]


ACTRL_ACCESSA = _ACTRL_ALISTA
PACTRL_ACCESSA = POINTER(_ACTRL_ALISTA)
ACTRL_AUDITA = _ACTRL_ALISTA
PACTRL_AUDITA = POINTER(_ACTRL_ALISTA)



class _ACTRL_ALISTW(ctypes.Structure):
    _fields_ = [
        ('cEntries', ULONG),
        ('pPropertyAccessList', PACTRL_PROPERTY_ENTRYW),
    ]


ACTRL_ACCESSW = _ACTRL_ALISTW
PACTRL_ACCESSW = POINTER(_ACTRL_ALISTW)
ACTRL_AUDITW = _ACTRL_ALISTW
PACTRL_AUDITW = POINTER(_ACTRL_ALISTW)


ACTRL_ACCESS = ACTRL_ACCESSW
PACTRL_ACCESS = PACTRL_ACCESSW
ACTRL_AUDIT = ACTRL_AUDITW
PACTRL_AUDIT = PACTRL_AUDITW
TRUSTEE_ACCESS_ALLOWED = 0x00000001
TRUSTEE_ACCESS_READ = 0x00000002
TRUSTEE_ACCESS_WRITE = 0x00000004
TRUSTEE_ACCESS_EXPLICIT = 0x00000001
TRUSTEE_ACCESS_READ_WRITE = TRUSTEE_ACCESS_READ | TRUSTEE_ACCESS_WRITE
TRUSTEE_ACCESS_ALL = 0xFFFFFFFF


class _TRUSTEE_ACCESSA(ctypes.Structure):
    _fields_ = [
        ('lpProperty', LPSTR),
        ('Access', ACCESS_RIGHTS),
        ('fAccessFlags', ULONG),
        ('fReturnedAccess', ULONG),
    ]


TRUSTEE_ACCESSA = _TRUSTEE_ACCESSA
PTRUSTEE_ACCESSA = POINTER(_TRUSTEE_ACCESSA)


class _TRUSTEE_ACCESSW(ctypes.Structure):
    _fields_ = [
        ('lpProperty', LPWSTR),
        ('Access', ACCESS_RIGHTS),
        ('fAccessFlags', ULONG),
        ('fReturnedAccess', ULONG),
    ]


TRUSTEE_ACCESSW = _TRUSTEE_ACCESSW
PTRUSTEE_ACCESSW = POINTER(_TRUSTEE_ACCESSW)


TRUSTEE_ACCESS = TRUSTEE_ACCESSW
PTRUSTEE_ACCESS = PTRUSTEE_ACCESSW
ACTRL_RESERVED = 0x00000000
ACTRL_PERM_1 = 0x00000001
ACTRL_PERM_2 = 0x00000002
ACTRL_PERM_3 = 0x00000004
ACTRL_PERM_4 = 0x00000008
ACTRL_PERM_5 = 0x00000010
ACTRL_PERM_6 = 0x00000020
ACTRL_PERM_7 = 0x00000040
ACTRL_PERM_8 = 0x00000080
ACTRL_PERM_9 = 0x00000100
ACTRL_PERM_10 = 0x00000200
ACTRL_PERM_11 = 0x00000400
ACTRL_PERM_12 = 0x00000800
ACTRL_PERM_13 = 0x00001000
ACTRL_PERM_14 = 0x00002000
ACTRL_PERM_15 = 0x00004000
ACTRL_PERM_16 = 0x00008000
ACTRL_PERM_17 = 0x00010000
ACTRL_PERM_18 = 0x00020000
ACTRL_PERM_19 = 0x00040000
ACTRL_PERM_20 = 0x00080000
ACTRL_ACCESS_ALLOWED = 0x00000001
ACTRL_ACCESS_DENIED = 0x00000002
ACTRL_AUDIT_SUCCESS = 0x00000004
ACTRL_AUDIT_FAILURE = 0x00000008
ACTRL_ACCESS_PROTECTED = 0x00000001
ACTRL_SYSTEM_ACCESS = 0x04000000
ACTRL_DELETE = 0x08000000
ACTRL_READ_CONTROL = 0x10000000
ACTRL_CHANGE_ACCESS = 0x20000000
ACTRL_CHANGE_OWNER = 0x40000000
ACTRL_SYNCHRONIZE = 0x80000000
ACTRL_STD_RIGHTS_ALL = 0xF8000000
ACTRL_STD_RIGHT_REQUIRED = ACTRL_STD_RIGHTS_ALL & ~ACTRL_SYNCHRONIZE
ACTRL_DS_OPEN = ACTRL_RESERVED
ACTRL_DS_CREATE_CHILD = ACTRL_PERM_1
ACTRL_DS_DELETE_CHILD = ACTRL_PERM_2
ACTRL_DS_LIST = ACTRL_PERM_3
ACTRL_DS_SELF = ACTRL_PERM_4
ACTRL_DS_READ_PROP = ACTRL_PERM_5
ACTRL_DS_WRITE_PROP = ACTRL_PERM_6
ACTRL_DS_DELETE_TREE = ACTRL_PERM_7
ACTRL_DS_LIST_OBJECT = ACTRL_PERM_8
ACTRL_DS_CONTROL_ACCESS = ACTRL_PERM_9
ACTRL_FILE_READ = ACTRL_PERM_1
ACTRL_FILE_WRITE = ACTRL_PERM_2
ACTRL_FILE_APPEND = ACTRL_PERM_3
ACTRL_FILE_READ_PROP = ACTRL_PERM_4
ACTRL_FILE_WRITE_PROP = ACTRL_PERM_5
ACTRL_FILE_EXECUTE = ACTRL_PERM_6
ACTRL_FILE_READ_ATTRIB = ACTRL_PERM_8
ACTRL_FILE_WRITE_ATTRIB = ACTRL_PERM_9
ACTRL_FILE_CREATE_PIPE = ACTRL_PERM_10
ACTRL_DIR_LIST = ACTRL_PERM_1
ACTRL_DIR_CREATE_OBJECT = ACTRL_PERM_2
ACTRL_DIR_CREATE_CHILD = ACTRL_PERM_3
ACTRL_DIR_DELETE_CHILD = ACTRL_PERM_7
ACTRL_DIR_TRAVERSE = ACTRL_PERM_6
ACTRL_KERNEL_TERMINATE = ACTRL_PERM_1
ACTRL_KERNEL_THREAD = ACTRL_PERM_2
ACTRL_KERNEL_VM = ACTRL_PERM_3
ACTRL_KERNEL_VM_READ = ACTRL_PERM_4
ACTRL_KERNEL_VM_WRITE = ACTRL_PERM_5
ACTRL_KERNEL_DUP_HANDLE = ACTRL_PERM_6
ACTRL_KERNEL_PROCESS = ACTRL_PERM_7
ACTRL_KERNEL_SET_INFO = ACTRL_PERM_8
ACTRL_KERNEL_GET_INFO = ACTRL_PERM_9
ACTRL_KERNEL_CONTROL = ACTRL_PERM_10
ACTRL_KERNEL_ALERT = ACTRL_PERM_11
ACTRL_KERNEL_GET_CONTEXT = ACTRL_PERM_12
ACTRL_KERNEL_SET_CONTEXT = ACTRL_PERM_13
ACTRL_KERNEL_TOKEN = ACTRL_PERM_14
ACTRL_KERNEL_IMPERSONATE = ACTRL_PERM_15
ACTRL_KERNEL_DIMPERSONATE = ACTRL_PERM_16
ACTRL_PRINT_SADMIN = ACTRL_PERM_1
ACTRL_PRINT_SLIST = ACTRL_PERM_2
ACTRL_PRINT_PADMIN = ACTRL_PERM_3
ACTRL_PRINT_PUSE = ACTRL_PERM_4
ACTRL_PRINT_JADMIN = ACTRL_PERM_5
ACTRL_SVC_GET_INFO = ACTRL_PERM_1
ACTRL_SVC_SET_INFO = ACTRL_PERM_2
ACTRL_SVC_STATUS = ACTRL_PERM_3
ACTRL_SVC_LIST = ACTRL_PERM_4
ACTRL_SVC_START = ACTRL_PERM_5
ACTRL_SVC_STOP = ACTRL_PERM_6
ACTRL_SVC_PAUSE = ACTRL_PERM_7
ACTRL_SVC_INTERROGATE = ACTRL_PERM_8
ACTRL_SVC_UCONTROL = ACTRL_PERM_9
ACTRL_REG_QUERY = ACTRL_PERM_1
ACTRL_REG_SET = ACTRL_PERM_2
ACTRL_REG_CREATE_CHILD = ACTRL_PERM_3
ACTRL_REG_LIST = ACTRL_PERM_4
ACTRL_REG_NOTIFY = ACTRL_PERM_5
ACTRL_REG_LINK = ACTRL_PERM_6
ACTRL_WIN_CLIPBRD = ACTRL_PERM_1
ACTRL_WIN_GLOBAL_ATOMS = ACTRL_PERM_2
ACTRL_WIN_CREATE = ACTRL_PERM_3
ACTRL_WIN_LIST_DESK = ACTRL_PERM_4
ACTRL_WIN_LIST = ACTRL_PERM_5
ACTRL_WIN_READ_ATTRIBS = ACTRL_PERM_6
ACTRL_WIN_WRITE_ATTRIBS = ACTRL_PERM_7
ACTRL_WIN_SCREEN = ACTRL_PERM_8
ACTRL_WIN_EXIT = ACTRL_PERM_9


class _ACTRL_OVERLAPPED(ctypes.Structure):

    class DUMMYUNIONNAME(ctypes.Union):
        _fields_ = [
            ('Provider', PVOID),
            ('Reserved1', ULONG),
        ]

    _fields_ = [
        ('DUMMYUNIONNAME', DUMMYUNIONNAME),
        ('Reserved2', ULONG),
        ('hEvent', HANDLE),
    ]


ACTRL_OVERLAPPED = _ACTRL_OVERLAPPED
PACTRL_OVERLAPPED = POINTER(_ACTRL_OVERLAPPED)


class _ACTRL_ACCESS_INFOA(ctypes.Structure):
    _fields_ = [
        ('fAccessPermission', ULONG),
        ('lpAccessPermissionName', LPSTR),
    ]


ACTRL_ACCESS_INFOA = _ACTRL_ACCESS_INFOA
PACTRL_ACCESS_INFOA = POINTER(_ACTRL_ACCESS_INFOA)


class _ACTRL_ACCESS_INFOW(ctypes.Structure):
    _fields_ = [
        ('fAccessPermission', ULONG),
        ('lpAccessPermissionName', LPWSTR),
    ]


ACTRL_ACCESS_INFOW = _ACTRL_ACCESS_INFOW
PACTRL_ACCESS_INFOW = POINTER(_ACTRL_ACCESS_INFOW)


ACTRL_ACCESS_INFO = ACTRL_ACCESS_INFOW
PACTRL_ACCESS_INFO = PACTRL_ACCESS_INFOW


class _ACTRL_CONTROL_INFOA(ctypes.Structure):
    _fields_ = [
        ('lpControlId', LPSTR),
        ('lpControlName', LPSTR),
    ]


ACTRL_CONTROL_INFOA = _ACTRL_CONTROL_INFOA
PACTRL_CONTROL_INFOA = POINTER(_ACTRL_CONTROL_INFOA)


class _ACTRL_CONTROL_INFOW(ctypes.Structure):
    _fields_ = [
        ('lpControlId', LPWSTR),
        ('lpControlName', LPWSTR),
    ]


ACTRL_CONTROL_INFOW = _ACTRL_CONTROL_INFOW
PACTRL_CONTROL_INFOW = POINTER(_ACTRL_CONTROL_INFOW)


ACTRL_CONTROL_INFO = ACTRL_CONTROL_INFOW
PACTRL_CONTROL_INFO = PACTRL_CONTROL_INFOW
ACTRL_ACCESS_NO_OPTIONS = 0x00000000
ACTRL_ACCESS_SUPPORTS_OBJECT_ENTRIES = 0x00000001
TREE_SEC_INFO_SET = 0x00000001
TREE_SEC_INFO_RESET = 0x00000002
TREE_SEC_INFO_RESET_KEEP_EXPLICIT = 0x00000003


class _PROGRESS_INVOKE_SETTING(ENUM):
    ProgressInvokeNever = 1
    ProgressInvokeEveryObject = 2
    ProgressInvokeOnError = 3
    ProgressCancelOperation = 4
    ProgressRetryOperation = 5
    ProgressInvokePrePostError = 6


PROG_INVOKE_SETTING = _PROGRESS_INVOKE_SETTING
PPROG_INVOKE_SETTING = POINTER(_PROGRESS_INVOKE_SETTING)


class _FN_OBJECT_MGR_FUNCTIONS(ctypes.Structure):
    _fields_ = [
        ('Placeholder', ULONG),
    ]


FN_OBJECT_MGR_FUNCTS = _FN_OBJECT_MGR_FUNCTIONS
PFN_OBJECT_MGR_FUNCTS = POINTER(_FN_OBJECT_MGR_FUNCTIONS)


class _INHERITED_FROMA(ctypes.Structure):
    _fields_ = [
        ('GenerationGap', LONG),
        ('AncestorName', LPSTR),
    ]


INHERITED_FROMA = _INHERITED_FROMA
PINHERITED_FROMA = POINTER(_INHERITED_FROMA)


class _INHERITED_FROMW(ctypes.Structure):
    _fields_ = [
        ('GenerationGap', LONG),
        ('AncestorName', LPWSTR),
    ]


INHERITED_FROMW = _INHERITED_FROMW
PINHERITED_FROMW = POINTER(_INHERITED_FROMW)


INHERITED_FROM = INHERITED_FROMW
PINHERITED_FROM = PINHERITED_FROMW


__all__ = (
    'ACTRL_FILE_READ_ATTRIB', 'ACTRL_REG_LIST', 'ACTRL_WIN_EXIT', 'AccFree',
    'TRUSTEE_ACCESS_READ', 'ACTRL_SVC_INTERROGATE', 'ACTRL_WIN_CLIPBRD',
    'ACTRL_WIN_WRITE_ATTRIBS', 'TREE_SEC_INFO_RESET', 'ACTRL_PRINT_SLIST',
    'TREE_SEC_INFO_RESET_KEEP_EXPLICIT', 'ACTRL_KERNEL_VM', 'ACTRL_SVC_STOP',
    'ACTRL_WIN_LIST_DESK', 'ACTRL_SVC_STATUS', 'ACTRL_KERNEL_SET_CONTEXT',
    'ACTRL_CHANGE_ACCESS', 'ACTRL_WIN_SCREEN', 'ACTRL_SVC_PAUSE', 'PTRUSTEEW',
    'ACTRL_ACCESS_PROTECTED', 'INHERIT_ONLY', 'TRUSTEE_ACCESS_ALL', 'TRUSTEE',
    'ACTRL_PERM_18', 'ACTRL_PERM_19', 'ACTRL_STD_RIGHTS_ALL', 'ACTRL_PERM_14',
    'ACTRL_DS_WRITE_PROP', 'ACTRL_PERM_15', 'ACTRL_PRINT_PADMIN', 'PTRUSTEEA',
    'ACTRL_PERM_17', 'ACTRL_PERM_10', 'ACTRL_PERM_11', 'ACTRL_PERM_12',
    'ACTRL_PERM_13', 'ACTRL_KERNEL_VM_READ', 'ACTRL_KERNEL_IMPERSONATE',
    'ACTRL_WIN_LIST', 'ACTRL_PERM_16', 'ACTRL_DIR_CREATE_OBJECT', 'TRUSTEEA',
    'ACTRL_STD_RIGHT_REQUIRED', 'ACTRL_SVC_START', 'TRUSTEE_ACCESS_ALLOWED',
    'ACTRL_KERNEL_DIMPERSONATE', 'ACTRL_ACCESS_ALLOWED', 'ACTRL_READ_CONTROL',
    'ACTRL_KERNEL_GET_INFO', 'ACTRL_ACCESS_DENIED', 'ACTRL_DIR_TRAVERSE',
    'SUB_CONTAINERS_AND_OBJECTS_INHERIT', 'ACTRL_FILE_EXECUTE', 'ACCESS_MODE',
    'TRUSTEE_ACCESS_WRITE', 'ACTRL_AUDIT_FAILURE', 'ACTRL_DS_LIST_OBJECT',
    'ACTRL_REG_QUERY', 'INHERITED_GRANDPARENT', 'ACTRL_REG_CREATE_CHILD',
    'ACTRL_FILE_CREATE_PIPE', 'INHERIT_NO_PROPAGATE', 'INHERITED_PARENT',
    'ACTRL_FILE_WRITE_ATTRIB', 'ACTRL_KERNEL_SET_INFO', 'ACTRL_REG_SET',
    'ACTRL_SYSTEM_ACCESS', 'ACTRL_PERM_4', 'ACTRL_WIN_READ_ATTRIBS',
    'ACTRL_FILE_APPEND', 'ACTRL_DS_LIST', 'ACTRL_REG_LINK', 'ACTRL_DS_SELF',
    'ACTRL_CHANGE_OWNER', 'ACTRL_KERNEL_CONTROL', 'ACTRL_RESERVED',
    'ACTRL_PRINT_JADMIN', 'ACTRL_PRINT_PUSE', 'ACTRL_DS_READ_PROP',
    'TRUSTEE_ACCESS_READ_WRITE', 'ACTRL_KERNEL_TOKEN', 'TREE_SEC_INFO_SET',
    'INHERITED_ACCESS_ENTRY', 'ACTRL_ACCESS_NO_OPTIONS', 'ACTRL_SYNCHRONIZE',
    'ACTRL_PERM_8', 'ACTRL_AUDIT_SUCCESS', 'ACTRL_KERNEL_VM_WRITE',
    'ACTRL_DS_CREATE_CHILD', 'ACTRL_KERNEL_PROCESS', 'ACTRL_KERNEL_THREAD',
    'ACCCTRL_DEFAULT_PROVIDER', 'SUB_OBJECTS_ONLY_INHERIT', 'ACTRL_DIR_LIST',
    'ACTRL_REG_NOTIFY', 'ACTRL_DIR_CREATE_CHILD', 'ACTRL_DS_CONTROL_ACCESS',
    'ACTRL_SVC_UCONTROL', 'ACTRL_SVC_SET_INFO', 'ACTRL_DS_OPEN', '_TRUSTEE_A',
    'ACTRL_FILE_WRITE', 'ACTRL_DS_DELETE_CHILD', 'ACTRL_KERNEL_TERMINATE',
    'TRUSTEE_ACCESS_EXPLICIT', 'ACTRL_DS_DELETE_TREE', 'ACTRL_WIN_CREATE',
    'ACTRL_PERM_20', 'ACTRL_WIN_GLOBAL_ATOMS', 'ACTRL_KERNEL_ALERT',
    'ACTRL_DELETE', 'ACTRL_FILE_READ', 'ACCCTRL_DEFAULT_PROVIDERW',
    'ACTRL_PERM_6', 'ACTRL_PERM_7', 'ACTRL_FILE_READ_PROP', 'ACTRL_PERM_5',
    'ACTRL_PERM_2', 'ACTRL_PERM_3', 'ACTRL_PERM_1', 'ACTRL_KERNEL_DUP_HANDLE',
    'ACCCTRL_DEFAULT_PROVIDERA', 'SUB_CONTAINERS_ONLY_INHERIT', '_TRUSTEE_W',
    'ACTRL_PERM_9', 'ACTRL_ACCESS_SUPPORTS_OBJECT_ENTRIES', 'NO_INHERITANCE',
    'ACTRL_KERNEL_GET_CONTEXT', 'ACTRL_FILE_WRITE_PROP', 'ACTRL_PRINT_SADMIN',
    'ACTRL_SVC_GET_INFO', 'ACTRL_DIR_DELETE_CHILD', 'ACTRL_SVC_LIST',
    'TRUSTEE_FORM', 'TRUSTEE_TYPE', '_ACCESS_MODE', 'PROG_INVOKE_SETTING',
    '_PROGRESS_INVOKE_SETTING', 'SE_OBJECT_TYPE', '_TRUSTEE_TYPE', 'TRUSTEEW',
    '_SE_OBJECT_TYPE', '_TRUSTEE_FORM', '_MULTIPLE_TRUSTEE_OPERATION',
    'MULTIPLE_TRUSTEE_OPERATION', 'PPROG_INVOKE_SETTING', 'PEXPLICIT_ACCESSW',
    'PFN_OBJECT_MGR_FUNCTS', 'PACTRL_PROPERTY_ENTRYA', 'POBJECTS_AND_NAME_W',
    '_ACTRL_PROPERTY_ENTRYW', 'FN_OBJECT_MGR_FUNCTS', 'POBJECTS_AND_NAME_A',
    'PACTRL_PROPERTY_ENTRYW', '_ACTRL_PROPERTY_ENTRYA', 'PEXPLICIT_ACCESS_A',
    '_FN_OBJECT_MGR_FUNCTIONS', 'PACTRL_ACCESS_ENTRY_LISTW', '_ACTRL_ALISTW',
    'PACTRL_ACCESS_ENTRY_LISTA', 'ACTRL_ACCESS_ENTRYA', 'ACTRL_ACCESS_ENTRYW',
    'ACTRL_ACCESS_ENTRY_LISTA', 'PEXPLICIT_ACCESSA', 'PACTRL_AUDITW',
    'ACTRL_ACCESS_ENTRY_LISTW', 'PACTRL_AUDITA', '_ACTRL_ACCESS_ENTRYA',
    'POBJECTS_AND_SID', 'PACTRL_CONTROL_INFOW', '_ACTRL_ACCESS_ENTRYW',
    '_ACTRL_ACCESS_ENTRY_LISTA', '_ACTRL_ALISTA', 'PACTRL_CONTROL_INFOA',
    '_ACTRL_ACCESS_ENTRY_LISTW', 'EXPLICIT_ACCESS_W', '_OBJECTS_AND_NAME_W',
    '_ACTRL_ACCESS_INFOA', '_OBJECTS_AND_NAME_A', '_ACTRL_ACCESS_INFOW',
    'OBJECTS_AND_NAME_A', 'TRUSTEE_ACCESSW', '_INHERITED_FROMA', 'PTRUSTEE_A',
    'INHERITED_FROMW', '_INHERITED_FROMW', 'OBJECTS_AND_NAME_W', 'PTRUSTEE_W',
    'TRUSTEE_ACCESSA', 'INHERITED_FROMA', 'ACTRL_CONTROL_INFOA', 'TRUSTEE_A',
    'PACTRL_ACCESSW', '_ACTRL_OVERLAPPED', 'ACTRL_CONTROL_INFOW', 'TRUSTEE_W',
    'PACTRL_ACCESSA', 'PACTRL_OVERLAPPED', '_TRUSTEE_ACCESSW', 'ACTRL_AUDITA',
    'PTRUSTEE_ACCESSA', '_TRUSTEE_ACCESSA', 'ACTRL_ACCESSA', 'ACTRL_ACCESSW',
    '_EXPLICIT_ACCESS_W', 'ACTRL_ACCESS_INFOA', '_EXPLICIT_ACCESS_A',
    'ACTRL_ACCESS_INFOW', 'ACTRL_PROPERTY_ENTRYW', 'PACTRL_ACCESS_INFOW',
    'ACTRL_PROPERTY_ENTRYA', 'ACTRL_AUDITW', 'PACTRL_ACCESS_INFOA',
    'PACTRL_ACCESS_ENTRYW', 'EXPLICIT_ACCESSA', 'EXPLICIT_ACCESSW',
    'PACTRL_ACCESS_ENTRYA', 'OBJECTS_AND_SID', 'ACTRL_OVERLAPPED', 'PTRUSTEE',
    'PINHERITED_FROMW', 'PTRUSTEE_ACCESSW', 'PEXPLICIT_ACCESS_W', 'PTRUSTEE_',
    'PINHERITED_FROMA', '_OBJECTS_AND_SID', '_ACTRL_CONTROL_INFOA',
    'EXPLICIT_ACCESS_A', '_ACTRL_CONTROL_INFOW', 'PINHERIT_FLAGS', 'TRUSTEE_',
    'TRUSTEE_ACCESS', 'PACTRL_ACCESS_INFO', 'ACTRL_AUDIT', 'PTRUSTEE_ACCESS',
    'PACTRL_PROPERTY_ENTRY', 'PACCESS_RIGHTS', 'ACTRL_ACCESS_ENTRY',
    'PACTRL_CONTROL_INFO', 'ACCESS_RIGHTS', 'PACTRL_ACCESS_ENTRY',
    'EXPLICIT_ACCESS', 'EXPLICIT_ACCESS_', 'POBJECTS_AND_NAME_',
    'INHERITED_FROM', 'ACTRL_PROPERTY_ENTRY', 'PEXPLICIT_ACCESS_',
    'OBJECTS_AND_NAME_', 'PINHERITED_FROM', 'INHERIT_FLAGS', 'PACTRL_AUDIT',
    'ACTRL_ACCESS_INFO', 'ACTRL_ACCESS_ENTRY_LIST', 'PACTRL_ACCESS',
    'ACTRL_CONTROL_INFO', 'PACTRL_ACCESS_ENTRY_LIST', 'ACTRL_ACCESS',
    'PEXPLICIT_ACCESS',
)