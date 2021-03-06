

from .wtypes_h import ULONG
# Increment this if a change has global effects
# ++ BUILD Version: 0004     Increment this if a change has global effects
# Copyright (c) 1992-1999  Microsoft Corporation
# Module Name:
# devioctl.h
# Abstract:
# This module contains
# Revision History:
# --
# begin_winioctl
# begin_ntddk begin_wdm begin_nthal begin_ntifs

# Define the various device type values.  Note that values used by Microsoft
# Corporation are in the range 0-32767, and 32768-65535 are reserved for use
# by customers.

DEVICE_TYPE = ULONG
FILE_DEVICE_BEEP = 0x00000001
FILE_DEVICE_CD_ROM = 0x00000002
FILE_DEVICE_CD_ROM_FILE_SYSTEM = 0x00000003
FILE_DEVICE_CONTROLLER = 0x00000004
FILE_DEVICE_DATALINK = 0x00000005
FILE_DEVICE_DFS = 0x00000006
FILE_DEVICE_DISK = 0x00000007
FILE_DEVICE_DISK_FILE_SYSTEM = 0x00000008
FILE_DEVICE_FILE_SYSTEM = 0x00000009
FILE_DEVICE_INPORT_PORT = 0x00000000a
FILE_DEVICE_KEYBOARD = 0x00000000b
FILE_DEVICE_MAILSLOT = 0x00000000c
FILE_DEVICE_MIDI_IN = 0x00000000d
FILE_DEVICE_MIDI_OUT = 0x00000000e
FILE_DEVICE_MOUSE = 0x00000000f
FILE_DEVICE_MULTI_UNC_PROVIDER = 0x00000010
FILE_DEVICE_NAMED_PIPE = 0x00000011
FILE_DEVICE_NETWORK = 0x00000012
FILE_DEVICE_NETWORK_BROWSER = 0x00000013
FILE_DEVICE_NETWORK_FILE_SYSTEM = 0x00000014
FILE_DEVICE_NULL = 0x00000015
FILE_DEVICE_PARALLEL_PORT = 0x00000016
FILE_DEVICE_PHYSICAL_NETCARD = 0x00000017
FILE_DEVICE_PRINTER = 0x00000018
FILE_DEVICE_SCANNER = 0x00000019
FILE_DEVICE_SERIAL_MOUSE_PORT = 0x00000001a
FILE_DEVICE_SERIAL_PORT = 0x00000001b
FILE_DEVICE_SCREEN = 0x00000001c
FILE_DEVICE_SOUND = 0x00000001d
FILE_DEVICE_STREAMS = 0x00000001e
FILE_DEVICE_TAPE = 0x00000001f
FILE_DEVICE_TAPE_FILE_SYSTEM = 0x00000020
FILE_DEVICE_TRANSPORT = 0x00000021
FILE_DEVICE_UNKNOWN = 0x00000022
FILE_DEVICE_VIDEO = 0x00000023
FILE_DEVICE_VIRTUAL_DISK = 0x00000024
FILE_DEVICE_WAVE_IN = 0x00000025
FILE_DEVICE_WAVE_OUT = 0x00000026
FILE_DEVICE_8042_PORT = 0x00000027
FILE_DEVICE_NETWORK_REDIRECTOR = 0x00000028
FILE_DEVICE_BATTERY = 0x00000029
FILE_DEVICE_BUS_EXTENDER = 0x00000002a
FILE_DEVICE_MODEM = 0x00000002b
FILE_DEVICE_VDM = 0x00000002c
FILE_DEVICE_MASS_STORAGE = 0x00000002d
FILE_DEVICE_SMB = 0x00000002e
FILE_DEVICE_KS = 0x00000002f
FILE_DEVICE_CHANGER = 0x00000030
FILE_DEVICE_SMARTCARD = 0x00000031
FILE_DEVICE_ACPI = 0x00000032
FILE_DEVICE_DVD = 0x00000033
FILE_DEVICE_FULLSCREEN_VIDEO = 0x00000034
FILE_DEVICE_DFS_FILE_SYSTEM = 0x00000035
FILE_DEVICE_DFS_VOLUME = 0x00000036
FILE_DEVICE_SERENUM = 0x00000037
FILE_DEVICE_TERMSRV = 0x00000038
FILE_DEVICE_KSEC = 0x00000039
FILE_DEVICE_FIPS = 0x00000003A
FILE_DEVICE_INFINIBAND = 0x00000003B
FILE_DEVICE_VMBUS = 0x00000003E
FILE_DEVICE_CRYPT_PROVIDER = 0x00000003F
FILE_DEVICE_WPD = 0x00000040
FILE_DEVICE_BLUETOOTH = 0x00000041
FILE_DEVICE_MT_COMPOSITE = 0x00000042
FILE_DEVICE_MT_TRANSPORT = 0x00000043
FILE_DEVICE_BIOMETRIC = 0x00000044
FILE_DEVICE_PMI = 0x00000045
FILE_DEVICE_EHSTOR = 0x00000046
FILE_DEVICE_DEVAPI = 0x00000047
FILE_DEVICE_GPIO = 0x00000048
FILE_DEVICE_USBEX = 0x00000049
FILE_DEVICE_CONSOLE = 0x00000050
FILE_DEVICE_NFP = 0x00000051
FILE_DEVICE_SYSENV = 0x00000052
FILE_DEVICE_VIRTUAL_BLOCK = 0x00000053
FILE_DEVICE_POINT_OF_SERVICE = 0x00000054
FILE_DEVICE_STORAGE_REPLICATION = 0x00000055
FILE_DEVICE_TRUST_ENV = 0x00000056
FILE_DEVICE_UCM = 0x00000057
FILE_DEVICE_UCMTCPCI = 0x00000058
FILE_DEVICE_PERSISTENT_MEMORY = 0x00000059
FILE_DEVICE_NVDIMM = 0x00000005a
FILE_DEVICE_HOLOGRAPHIC = 0x00000005b
FILE_DEVICE_SDFXHCI = 0x00000005c

# Macro definition for defining IOCTL and FSCTL function control codes.  Note
# that function codes 0-2047 are reserved for Microsoft Corporation, and
# 2048-4095 are reserved for customers.


def CTL_CODE(DeviceType, Function, Method, Access):
    return (DeviceType << 16) | (Access << 14) | (Function << 2) | Method

# Macro to extract device type out of the device io control code


def DEVICE_TYPE_FROM_CTL_CODE(ctrlCode):
    return (ctrlCode & 0x00000000ffff0000) >> 16

# Macro to extract buffering method out of the device io control code


def METHOD_FROM_CTL_CODE(ctrlCode):
    return ctrlCode & 3

# Define the method codes for how buffers are passed for I/O and FS controls


METHOD_BUFFERED = 0x00000000
METHOD_IN_DIRECT = 0x00000001
METHOD_OUT_DIRECT = 0x00000002
METHOD_NEITHER = 0x00000003

# Define some easier to comprehend aliases:
# METHOD_DIRECT_TO_HARDWARE (writes, aka METHOD_IN_DIRECT)
# METHOD_DIRECT_FROM_HARDWARE (reads, aka METHOD_OUT_DIRECT)

METHOD_DIRECT_TO_HARDWARE = METHOD_IN_DIRECT
METHOD_DIRECT_FROM_HARDWARE = METHOD_OUT_DIRECT

# Define the access check value for any access


# The FILE_READ_ACCESS and FILE_WRITE_ACCESS constants are also defined in
# ntioapi.h as FILE_READ_DATA and FILE_WRITE_DATA. The values for these
# constants *MUST* always be in sync.


# FILE_SPECIAL_ACCESS is checked by the NT I/O system the same as
# FILE_ANY_ACCESS.
# The file systems, however, may add additional access checks for I/O and FS
# controls
# that use this value.

FILE_ANY_ACCESS = 0x00000000
# file & pipe
FILE_SPECIAL_ACCESS = FILE_ANY_ACCESS
# file & pipe
FILE_READ_ACCESS = 0x00000001
FILE_WRITE_ACCESS = 0x00000002
# end_ntddk end_wdm end_nthal end_ntifs
# _DEVIOCTL_
# end_winioctl

__all__ = (
    'DEVICE_TYPE_FROM_CTL_CODE', 'CTL_CODE', 'DEVICE_TYPE', 'FILE_DEVICE_BEEP',
    'FILE_DEVICE_CD_ROM', 'FILE_DEVICE_CD_ROM_FILE_SYSTEM',
    'FILE_DEVICE_CONTROLLER', 'FILE_DEVICE_DATALINK', 'FILE_DEVICE_DFS',
    'FILE_DEVICE_DISK', 'FILE_DEVICE_DISK_FILE_SYSTEM',
    'FILE_DEVICE_FILE_SYSTEM', 'FILE_DEVICE_INPORT_PORT',
    'FILE_DEVICE_KEYBOARD', 'FILE_DEVICE_MAILSLOT', 'FILE_DEVICE_MIDI_IN',
    'FILE_DEVICE_MIDI_OUT', 'FILE_DEVICE_MOUSE',
    'FILE_DEVICE_MULTI_UNC_PROVIDER', 'FILE_DEVICE_NAMED_PIPE',
    'FILE_DEVICE_NETWORK', 'FILE_DEVICE_NETWORK_BROWSER',
    'FILE_DEVICE_NETWORK_FILE_SYSTEM', 'FILE_DEVICE_NULL',
    'FILE_DEVICE_PARALLEL_PORT', 'FILE_DEVICE_PHYSICAL_NETCARD',
    'FILE_DEVICE_PRINTER', 'FILE_DEVICE_SCANNER',
    'FILE_DEVICE_SERIAL_MOUSE_PORT', 'FILE_DEVICE_SERIAL_PORT',
    'FILE_DEVICE_SCREEN', 'FILE_DEVICE_SOUND', 'FILE_DEVICE_STREAMS',
    'FILE_DEVICE_TAPE', 'FILE_DEVICE_TAPE_FILE_SYSTEM',
    'FILE_DEVICE_TRANSPORT', 'FILE_DEVICE_UNKNOWN', 'FILE_DEVICE_VIDEO',
    'FILE_DEVICE_VIRTUAL_DISK', 'FILE_DEVICE_WAVE_IN', 'FILE_DEVICE_WAVE_OUT',
    'FILE_DEVICE_8042_PORT', 'FILE_DEVICE_NETWORK_REDIRECTOR',
    'FILE_DEVICE_BATTERY', 'FILE_DEVICE_BUS_EXTENDER', 'FILE_DEVICE_MODEM',
    'FILE_DEVICE_VDM', 'FILE_DEVICE_MASS_STORAGE', 'FILE_DEVICE_SMB',
    'FILE_DEVICE_KS', 'FILE_DEVICE_CHANGER', 'FILE_DEVICE_SMARTCARD',
    'FILE_DEVICE_ACPI', 'FILE_DEVICE_DVD', 'FILE_DEVICE_FULLSCREEN_VIDEO',
    'FILE_DEVICE_DFS_FILE_SYSTEM', 'FILE_DEVICE_DFS_VOLUME',
    'FILE_DEVICE_SERENUM', 'FILE_DEVICE_TERMSRV', 'FILE_DEVICE_KSEC',
    'FILE_DEVICE_FIPS', 'FILE_DEVICE_INFINIBAND', 'FILE_DEVICE_VMBUS',
    'FILE_DEVICE_CRYPT_PROVIDER', 'FILE_DEVICE_WPD', 'FILE_DEVICE_BLUETOOTH',
    'FILE_DEVICE_MT_TRANSPORT', 'FILE_DEVICE_BIOMETRIC', 'FILE_DEVICE_PMI',
    'FILE_DEVICE_EHSTOR', 'FILE_DEVICE_DEVAPI', 'FILE_DEVICE_GPIO',
    'FILE_DEVICE_USBEX', 'FILE_DEVICE_CONSOLE', 'FILE_DEVICE_NFP',
    'FILE_DEVICE_SYSENV', 'FILE_DEVICE_VIRTUAL_BLOCK',
    'FILE_DEVICE_POINT_OF_SERVICE', 'FILE_DEVICE_STORAGE_REPLICATION',
    'FILE_DEVICE_TRUST_ENV', 'FILE_DEVICE_UCM', 'FILE_DEVICE_UCMTCPCI',
    'FILE_DEVICE_PERSISTENT_MEMORY', 'FILE_DEVICE_NVDIMM',
    'FILE_DEVICE_HOLOGRAPHIC', 'FILE_DEVICE_SDFXHCI', 'METHOD_BUFFERED',
    'METHOD_IN_DIRECT', 'METHOD_OUT_DIRECT', 'METHOD_NEITHER',
    'METHOD_DIRECT_TO_HARDWARE', 'METHOD_DIRECT_FROM_HARDWARE',
    'FILE_ANY_ACCESS', 'FILE_SPECIAL_ACCESS', 'FILE_READ_ACCESS',
    'FILE_WRITE_ACCESS', 'METHOD_FROM_CTL_CODE'
)
