import pytest

@pytest.fixtures
def read_simple_list(): 
  paramlist=[(1,2,3),(3,4,7),(6,4,10)]
  return paramlist

@pytest.fixtures
def read_simple_list(): 
  simplelist=["05","renu","qe"]
  return simplelist


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
