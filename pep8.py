#!/usr/bin/env python3

import subprocess
from sys import argv
import os

if len(argv) < 2:
    print('Usage: pep8 FILE1 <FILE2...>')
    exit()

cwd = os.getcwd()
args = ['sudo', 'docker-compose', '-f', '/docker-compose.yml', 'exec', 'pep8', 'pep8']
for arg in argv[1:]:
    args.append('{}/{}'.format(cwd, arg))
subprocess.call(args)
