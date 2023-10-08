#!/usr/bin/env python3
import shutil
import sys
import os

def checkdiskusage(disk,min_gb, min_percent):
    """Returns true if there is enough free disk space, false otherwise"""
    du=shutil.disk_usage(disk)
    #calcuate the percentage of free space
    percent_free=100*du.free/du.total
    gigabytes_free =du.free/2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def reboot_check():
    if os.path.exists('/var/run/reboot-required'):
        return True
    else:
        return False
def check_root_full():
   """Returns True if the root partiition is full, False otherwise."""
   return checkdiskusage('/',2,20);
#check for at least 2gb and 18%free
def main():
    checks=[(reboot_check,"reboot is required"),(check_root_full,"Disk is Full")]
    for method,msg in checks:
        error=False
        if method():
            print(msg)
            error=True
    if error:
        sys.exit(1)

    # if not check_root_full():
    #     print("Error: Disk Full. Not enough disk space")
    #     sys.exit(1)
    # if reboot_check():
    #     print("reboot is required")
    #     sys.exit(1)
    print("everything ok")
    sys.exit(0)

main()
