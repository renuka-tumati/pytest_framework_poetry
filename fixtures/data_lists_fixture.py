import pytest
from helpers.json_utils import parse_json


@pytest.fixtures
def read_simple_list(): 
    return [(1, 2, 3), (3, 4, 7), (6, 4, 10)]


def number_list():
    return [(3+5, 8, 16), (2+4, 6, 12), (6*9, 42, 96)]


@pytest.fixtures
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
  return emp_list
