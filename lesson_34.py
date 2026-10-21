# employees = ["Michael", "James", "Daniel", "Alex"]
# salaries = [5000, 9000]

# for name, salary in zip(employees, salaries):
#   print(name, salary)


# names = ["Michael", "James"]
# salaries = [5000, 9000]
# departments = ["IT", "HR"]

# for name, salary, department in zip(names, salaries, departments):
#   print(name, salary, department)


# names = ["Michael", "James", "Alex"]
# salaries = [5000, 9000, 12000, 6000]

# for name, salary in zip(names, salaries):
#   if salary >= 9000:
#     print(name, salary)


# names = ["Michael", "James", "Daniel"]
# salaries = [5000, 9000, 12000]

# for index, (name, salary) in enumerate(zip(names, salaries),start=1):
#   print(index, name, salary)


names = ["Michael", "James", "Daniel", "Alex"]
salaries = [5000, 9000, 12000, 6000]
departments = ["IT", "HR", "Finance", "IT"]

count = 0
for index, (name, salary, department) in enumerate(zip(names, salaries, departments), start=1):
  print(f"{index}. {name} - {salary} - {department}")
for name, salary , department in zip(names, salaries, departments):
  if salary >= 9000:
    count += 1
    print(name, salary, department)
print("Employees count:", count)


