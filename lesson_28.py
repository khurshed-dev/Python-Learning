# def employee_info(*args, **kwargs):
#   print(args)
#   print(kwargs)

# employee_info("James", 25, salary = 9000, department = "IT")


# def employee_info(*args, **kwargs):
#   for name in args:
#     print("Employee: ", name)
#   for key, value in kwargs.items():
#     print(key, value)

# employee_info("James", "Michael", department = "IT")


# def employee_info(*args, **kwargs):
#   print("Total employees:", len(args))
#   print("Department:", kwargs.get("department", "Unknown"))

# employee_info("James", "Michael", "Daniel")


def employee_info(*args, **kwargs):
  print("Total employees:", len(args))

  for name in args:
    print("Emloyee:", name)
  print("Department:", kwargs.get("department", "Unknown"))

employee_info("James", "Michael", "Daniel", department = "IT")
