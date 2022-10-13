import json


def number_list():
    return [(3+5, 8, 16), (2+4, 6, 12), (6*9, 42, 96)]

  
def parse_json(path):  
  # Opening JSON file
  # './data/test_emp.json'
  f = open(path)  
  # returns JSON object as 
  # a dictionary
  data = json.load(f)
  # Closing file
  f.close()
  return data

def read_json(path):  
  # Iterating through the json
  # list
  data=parse_json(path)
  emp_list=list()
  for i in data['emp_details']:
      emp=list()
      emp.append(i["id"])
      emp.append(i["name"])
      emp.append(i["department"])
      emp_list.append(tuple(emp))  
