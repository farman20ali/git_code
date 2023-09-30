#!/usr/bin/env python3
import shutil
import sys

def checkdiskusage(disk,min_absolute, min_percent):
    """Returns true if there is enough free disk space, false otherwise"""
    du=shutil.disk_usage(disk)
    #calcuate the percentage of free space
    percent_free=100*du.free/du.total
    gigabytes_free =du.free/2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

#check for at least 2gb and 18%free
if not checkdiskusage('/',2*2**30,18):
    print("Error: Not enough disk space")
    return 1

print("everything ok")
return 0
