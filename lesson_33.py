# employees = ["Michael", "James", "Daniel"]

# for index, name in enumerate(employees):
#   print(index, name)


# employees = ["Michael", "James", "Daniel"]

# for index, name in enumerate(employees, start=1):
#   print(index, name)


# employees = ["Michael", "James", "Daniel"]

# for index, name in enumerate(employees, start=1):
#   print(f"Employee {index}:{name}")


# employees = ["Michael", "James", "Daniel", "Alex"]

# for index, name in enumerate(employees, start=1):
#   if index % 2 == 0:
#     print(index, name)


# salaries = [5000, 8000, 12000, 6000]

# for index, salary in enumerate(salaries, start=1):
#   if salary > 7000:
#     print(f"Employee {index}: {salary}")


employees = ["Michael", "James", "Daniel", "Alex"]
salaries = [5000, 9000, 12000, 6000]

for index, name in enumerate(employees):
  salary = salaries[index]
  print(f"All employees: {index + 1}.  {name} - {salary}")

for index, salary in enumerate(salaries):
  name = employees[index]
  if salary > 7000:
    print(f"Employees with salary > 7000: {index + 1} {name} - {salary}")