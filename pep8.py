#!/usr/bin/env python3

import subprocess
import os
from sys import argv

if len(argv) < 2:
    print('Usage: pep8 FILE1 <FILE2...>')
    exit()

cwd = os.getcwd()
args = ['sudo', 'docker-compose', 'exec', 'pep8', 'pep8']
# args += ['pep8']
for arg in argv[1:]:
    args.append(arg)
subprocess.call(args)
