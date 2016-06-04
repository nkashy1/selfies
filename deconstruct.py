#!/usr/bin/python3

import sys

script_file = sys.argv[1]
args = sys.argv[2:]

with open(script_file, 'r') as script_body:
    script = script_body.read()

    if len(args) == 0:
        print(script)
    else:
        print(script.format(*args))
