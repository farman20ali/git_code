#!/usr/bin/env python3
import shutil
import sys

def checkdiskusage(disk,min_gb, min_percent):
    """Returns true if there is enough free disk space, false otherwise"""
    du=shutil.disk_usage(disk)
    #calcuate the percentage of free space
    percent_free=100*du.free/du.total
    gigabytes_free =du.free/2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return False
    return True

def main():
    #merging the code and fixing
    if not checkdiskusage('/',2,20):
        print("Error: Not enough disk space")
        sys.exit(1)
    print("everything ok")
    sys.exit(0)

main()
