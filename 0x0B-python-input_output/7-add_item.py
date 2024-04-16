#!/usr/bin/python3
"""Defines the script that adds all arguments to a Python list,
and then save them to a file
"""


import json
import sys 
from os import path

save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

filename = 'add_item.json'
args = sys.argv[1:]

p_list = []

if not os.path.exists(filename):
    save_to_json_file(p_list, filename)

p_list = load_from_json_file(filename)

for i in range(1, args):
    p_list.append(args)
save_to_json_file(p_list, filename)
