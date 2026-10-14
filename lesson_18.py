# try:
#   salary = int(input("Enter your salary: "))
#   bonus = salary * 0.10
#   print("Salary:", salary)
#   print("Bonus:", bonus)
#   print("Total:", bonus + salary)

# except ValueError:
#   print("Invalid salary!")


# while True:
#   try:
#     salary = int(input("Enter your salary: "))
#     print("Salary,", salary)
#     bonus = salary * 0.10
#     break 
#   except ValueError:
#     print("Invalid salary!")

# print("Bonus,", bonus)
# print("Total:", bonus + salary)


while True:
  try:
    salary = int(input("Enter your salary: "))

    if salary < 0:
      print("Salary cannot be negative!")
      continue 
    bonus = salary * 0.10
    break 
  
  except ValueError:
    print("Invalid salary!")

print("Sarary,", salary)
print("Bonus,", bonus)
print("Total:", bonus + salary)