#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json
import os.path
import sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_items.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)
for i in argv[1:]:
    json_list.append(i)
    
save_to_json_file(json_list, filename)
