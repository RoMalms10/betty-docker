#!/usr/bin/python3

import subprocess
from sys import argv

if len(argv) < 2:
    print('Usage: betty FILE1 <FILE2...>')
    exit()

args = ['sudo', 'docker-compose', 'exec', 'betty', 'betty']
for arg in argv[1:]:
    args.append(arg)
subprocess.call(args)
