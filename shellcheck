#!/usr/bin/env python3

import subprocess
from sys import argv

if len(argv) < 2:
    print('Usage: shellcheck FILE1 <FILE2...>')
    exit()

args = ['sudo', 'docker-compose', 'exec', 'shellcheck', 'shellcheck']
for arg in argv[1:]:
    args.append(arg)
subprocess.call(args)
