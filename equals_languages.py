import requests
import bs4
import json


with open("/Users/drake/Desktop/vscode/parsing/data.json", 'r') as file:

    info = json.load(file)



set_list = [set(inf["ranks"]["languages"].keys())  for inf in info]
print(set_list)
common_languages = set.intersection(*set_list)

print(list(common_languages))