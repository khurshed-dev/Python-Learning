def count_employees(employees):
  total = len(employees)
  return total

employees = ["James", "Michael", "Daniel"]

total = count_employees(employees)

if total >= 3:
  print("Many employees")
else:
  print("Few employees")
  


