'''Write a script that does the following:

Receives a file_name and line_number as command line parameters.
Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.
Make sure that you handle the following error cases by presenting the user with a useful message:

The file doesn’t exist.
The file doesn’t contain the line_number specified (file is too short).'''

#!/usr/bin/env python3.6

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='the file to read')
parser.add_argument('line_number', type=int, help='the line to print from the file')

args = parser.parse_args()

try:
    lines = open(args.file_name, 'r').readlines()
    line = lines[args.line_number - 1]
except IndexError:
    print(f"Error: file '{args.file_name}' doesn't have {args.line_number} lines.")
except IOError as err:
    print(f"Error: {err}")
else:
    print(line)
