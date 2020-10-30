import argparse
import subprocess
import sys


####################
# Argument parsing #
####################
parser = argparse.ArgumentParser(description='Revert LVM Snapshots for E2E Tests')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--prepdest', action='store_true', help="LVM Snapshot the store volume and mounts for testing")
group.add_argument('--preporig', action='store_true', help="Unmounts the LVM Snapshot and mounts the original volume")
args = parser.parse_args()


##################################
# Commands to run on docker host #
##################################
SNAP_BEFORE_MIG = ['lvcreate', '--size', '5G', '--snapshot', '--name', 'zenko_snap', '/dev/mapper/centos-zenko_project']
CONTAINER_STOP_CMD = ['docker-compose', '-f', '/store/static/docker-compose-cloudserver.conf', 'down']
UMOUNT_ORIG = ['umount', '/store']
MOUNT_SNAP = ['mount', '/dev/mapper/centos-zenko_snap', '/store']
MOUNT_ORIG = ['mount', '-a']
CONTAINER_START_CMD = ['docker-compose', '-f', '/store/static/docker-compose-cloudserver.conf', 'up', '-d']
REMOVE_SNAP = ['lvremove', '/dev/mapper/centos-zenko_snap', '--force']


# List of commands
if sys.argv[1] == '--prepdest':
    CMD_LIST = [CONTAINER_STOP_CMD, UMOUNT_ORIG, MOUNT_SNAP, CONTAINER_START_CMD]
elif sys.argv[1] == '--preporig':
    CMD_LIST = [CONTAINER_STOP_CMD, UMOUNT_ORIG, MOUNT_ORIG, CONTAINER_START_CMD, REMOVE_SNAP]


# Function to Snapshot the store volume and prepare it for backup and restore tests from destination and vice versa.
def main():
    for each in CMD_LIST:
        sub_exec = subprocess.Popen(each, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    universal_newlines=True)
        return_code = sub_exec.wait()
        output, error = sub_exec.communicate()
        if return_code == 0:
            continue
        else:
            print("Revert failed with ERROR : {}".format(error))


if __name__ == '__main__':
    main()
