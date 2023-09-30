#!/usr/bin/env python3
import psutil

def check(percetage):
    usage=psutil.cpu_percent()
    print()
    return usage<percetage
value=int(input("Check percetage: "))
if not check(value):
    print("CPU is overloaded ")
else:
    print("everything is ok ")
print('end of code')

