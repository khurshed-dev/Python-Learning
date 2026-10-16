# def greet(name):
#   print("Hello,", name)

# greet("James")
# greet("John")


# def introduce(name, age):
#   print("My name is", name)
#   print("I am", age, "years old")

# introduce("James", 25)


def calculate_salary(salary, bonus):
  total = salary + bonus
  return total

result = calculate_salary(6000, 2000)

if result >= 8000:
  print("High salary")
else:
  print("Low salary")