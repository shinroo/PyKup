#!/usr/bin/env python
import sys, argparse
from lib import backup

parser = argparse.ArgumentParser(description='PyBack WebApp backup utils')
parser.add_argument('-d', action='store', dest='directory', help="Set a backup directory", type=str)

args = parser.parse_args()

if args.directory is None:
	print('You must insert a directory')
	exit(255)

backup = backup.Backup(args.directory)
backup.run()
