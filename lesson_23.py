def calculate_salary(salary, bonus=1000):
  total = salary + bonus
  return total

result = calculate_salary(6000)
print(result)
result = calculate_salary(6000, 3000)
print(result)