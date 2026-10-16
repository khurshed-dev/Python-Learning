# def calculate_salary(salary, bonus):
#   total = salary + bonus
#   return total

# result = calculate_salary(5000, 500)
# print("Total salary:", result)


# def calculate_total(salary):
#   bonus = salary * 0.15
#   total = salary + bonus 
#   return total

# result = calculate_total(6000)
# print("Total salary,", result)


# def calculate_total(salary):
#   if salary <= 0:
#     return 0

#   bonus = salary * 0.15
#   total = salary + bonus
#   return total

# print(calculate_total(-5000))
# print(calculate_total(0))
# print(calculate_total(6000))


# def calculate_total(salary):
#   bonus = salary * 0.15
#   total = salary + bonus
#   return total

# while True:
#   try:
#     salary = int(input("Enter your salary: "))
#     if salary <= 0:
#       print("Salary must be positive!")
#       continue

#     result = calculate_total(salary)
#     break
#   except ValueError:
#     print("Invalid salary!")
# print("Total salary:", result)


def calculate_total(salary):
  if salary < 5000:
    bonus = salary * 0.10
  elif salary < 10000:
    bonus = salary * 0.15
  else:
    bonus = salary * 0.20

  result = salary + bonus
  return result

while True:
  try:
    salary = int(input("Enter your salary: "))
    if salary <= 0:
      print("Salary must be positive!")
      continue

    result = calculate_total(salary)
    break
  except ValueError:
    print("Invalid salary!")
print("Total salary:", result)