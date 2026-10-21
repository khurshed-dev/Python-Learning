# salaries = [5000, 9000, 12000, 6000]
# result = list(filter(lambda salary: salary > 7000, salaries))
# print(result)


# employees = ["Michael", "James", "Daniel", "Alex"]
# result = list(filter(lambda name: len(name) > 5, employees))
# print(result)


# numbers = [5, 10, 15, 20, 25, 30]
# result = list(filter(lambda x: x > 10 and x < 30, numbers))
# print(result)


# def high_salary(salary):
#   return salary > 8000

# salaries = [5000, 9000, 12000, 7000]
# result = list(filter(high_salary, salaries))
# print(result)


def high_salary(salary):
  return salary > 10000

salaries = [4500, 7000, 9000, 12000, 5500, 15000, 8000]
higt_salary = list(filter(lambda salary: salary > 8000, salaries))
low_salary = list(filter(lambda salary: salary <= 7000, salaries))
total = list(filter(high_salary, salaries))

print("Orijinal salaries:", salaries)
print("Salaries > 8000:", higt_salary)
print("Salaries <= 7000:", low_salary)
print("Salaries > 10000", total)
print("Total high salaries:", len(total))