#!/usr/bin/python3

import subprocess
import os
import glob
from sys import argv

if len(argv) < 2:
    print('Usage: betty FILE1 <FILE2...>')
    exit()

cwd = os.getcwd()
path = cwd.split('/')
args = ['docker', 'run', '--rm', '-it', '--name', 'bettyd']
args += ['--mount', 'type=bind,source={},target=/Betty'.format(cwd)]
args += ['betty-docker', 'betty']
for arg in argv[1:]:
    args.append(arg)
subprocess.call(args)
