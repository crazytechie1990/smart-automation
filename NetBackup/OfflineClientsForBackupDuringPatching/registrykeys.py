#!/usr/bin/python
import errno
import os
import winreg

PROC_ARCH = os.environ['PROCESSOR_ARCHITECTURE'].lower()
PROC_ARCH64 = os.environ['PROCESSOR_ARCHITEW6432'].lower()

# Check for the processor architecture.

if PROC_ARCH == 'x86' and not PROC_ARCH64:
    arch_keys = {0}
elif PROC_ARCH == 'x86' or PROC_ARCH64 == 'amd64':
    arch_keys = {winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY}
else:
    raise Exception("Unhandled arch: {}".format(PROC_ARCH))


# Function to get value of a particular key.

def getkeyvalue():
    for arch_key in arch_keys:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Veritas\NetBackup", 0, winreg.KEY_READ | arch_key)
        for i in range(0, winreg.QueryInfoKey(key)[0]):
            skey_name = winreg.EnumKey(key, i)
            skey = winreg.OpenKey(key, skey_name)
            try:
                value = winreg.QueryValueEx(skey, 'INSTALLDIR')[0]
            except OSError as e:
                if e.errno == errno.ENOENT:
                    # INSTALLDIR doesn't exist in this skey
                    pass
            finally:
                skey.Close()
    return value


def main():
    print("Value of the key is :")
    print(getkeyvalue())


if __name__ == "__main__":
    main()
