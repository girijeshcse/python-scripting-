#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='envirionmanr arg')
parser.add_argument('-l', help='Provide a string to convert in loawer case')
parser.add_argument('-u', help='Provide a string to convert in upper case')
args = parser.parse_args()

if args.l:
    print(args.i.lower())
elif args.u:
    print(args.u.upper())
else:
    print("Provide a string to convert in lower case with -l and in upper case with -u")
