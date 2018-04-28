#!/usr/bin/python3

import subprocess
import os
from sys import argv

if len(argv) < 2:
    print('Usage: betty FILE1 <FILE2...>')
    exit()

cwd = os.getcwd()
args = ['docker', 'run', '--rm', '-it', '--name', 'bettyd']
args += ['--mount', f'type=bind,source={cwd},target=/Betty']
args += ['betty-docker', 'betty']
for arg in argv[1:]:
    args.append(arg)
subprocess.run(args)
