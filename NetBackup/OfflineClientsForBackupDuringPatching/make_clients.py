#!/usr/bin/python
import argparse
import os
import platform
import sys
import registrykeys

# Usage
parser = argparse.ArgumentParser(description='Offline clients during patching window')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--offline', action='store_true', help='make all clients offline')
group.add_argument('--online', action='store_false', help='make all clients online')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), default=sys.stdin, metavar='', dest='file',
                    required=True, help='Input file containing the list of clients')
args = parser.parse_args()

# Install paths..

WIN_NBU_INSTALL_PATH = registrykeys.getkeyvalue()
WIN_BIN_PATH = os.path.join(WIN_NBU_INSTALL_PATH, "\\Netbackup\\bin")
WIN_ADMIN_PATH = os.path.join(WIN_NBU_INSTALL_PATH, "\\Netbackup\\bin\\admincmd")
LIN_BIN_PATH = "/usr/openv/netbackup/bin"
LIN_ADMIN_PATH = "/usr/openv/netbackup/bin/admincmd"


# Function to change directory to NBU bin path.
def nbu_bin():
    if platform.system() == "Windows":
        os.chdir(WIN_BIN_PATH)
    elif platform.system() == "Linux":
        os.chdir(LIN_BIN_PATH)
    return None


# Function to change directory to NBU admin cmd path.
def nbu_admin():
    if platform.system() == "Windows":
        win_admin_path = "c:\\Program Files\\Veritas\\NetBackup\\bin\\admincmd"
        os.chdir(win_admin_path)
    elif platform.system() == "Linux":
        os.chdir(LIN_ADMIN_PATH)
    return None


# Function to create a list of clients for whom state change is intended.
def clients_list():
    clients = []
    try:
        with open(sys.argv[3]) as inputfile:
            for each in inputfile.readlines():
                if each.isspace():
                    continue
                else:
                    clients.append(each.strip())
    except FileNotFoundError:
        print("Please check your input file")
    return clients


def main():
    if sys.argv[1] == '--offline':
        try:
            for each in clients_list():
                nbu_admin()
                os.system('bpclient -client ' + each + ' -update -offline')
        except:
            print("Please make sure NBU Services are up and running")
    elif sys.argv[1] == '--online':
        try:
            for each in clients_list():
                nbu_admin()
                os.system('bpclient -client ' + each + ' -update -online')
        except :
            print("Please make sure NBU Services are up and running")


if __name__ == "__main__":
    main()
