# def employee_info(**kwargs):
#   print(kwargs)

# employee_info(name = "James", age = 25, salary=6000)


# def employee_info(**kawrgs):
#   print(kawrgs["name"])
#   print(kawrgs["salary"])

# employee_info(name = "James", salary = 7000, age = 25)


# def emlpoyee_info(**kwargs):
#   print(kwargs.get("name", "No name"))
#   print(kwargs.get("salary", 0))

# emlpoyee_info(name = "Daniel")


# def employee_info(**kwargs):
#   for key, value in kwargs.items():
#     print(key, value)

# employee_info(name = "James", salary = 7000)


def employee_info(**kwargs):
  for key, value in kwargs.items():
    print(key, value)
employee_info(name = "Michael", salary = 9000, department = "IT")