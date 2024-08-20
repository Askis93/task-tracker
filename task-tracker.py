import json
import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--add", help="Add task to tracker", required=False)
parser.add_argument("-l", "--list", help="Show all tasks, filter by [all, done, todo, in-progress]", required=False)
parser.add_argument("-u", "--update", help="Update task", required=False)
parser.add_argument("-d", "--delete", help="Delete task", required=False)
parser.add_argument("-c", "--complete", help="Mark as done", required=False)
parser.add_argument("-p", "--progress", help="Mark as in progress", required=False)

args = parser.parse_args()

if args.add:
    print("hello")
