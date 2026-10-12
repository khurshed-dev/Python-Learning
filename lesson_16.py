# # def greet():
# #   print("Hello, Khurshed!")

# # greet()


# def greet(name):
#   print("Hello,", name)

# greet("Ali")
# greet("Rustam")
# greet("Karim")


# def employee(name, salary):
#   print(name, salary)

# employee("Khurshed", 7000)


# def employee_info(name, position, salary):
#   print(name, position, salary)

# employee_info("Ali", "Operator", 4000)
# employee_info("Rustam", "Driver", 5000)
# employee_info("Karim", "Mechanic", 6000)


# def add(a, b):
#   print(a + b)

# add(5, 3)


# def add(a, b):
#   return a + b
# result = add(5, 3)
# print(result)


# def add(a, b):
#   return a + b
# result = add(5, 3)
# print(result * 2)


def calculate_salary(salary, bonus):
  return salary + bonus

james_salary = calculate_salary(4000, 500)
michael_salary = calculate_salary(5000, 1000)
john_salary = calculate_salary(6000, 1500)

print("James", james_salary)
print("Michael", michael_salary)
print("John", john_salary)
