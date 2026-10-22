# salaries = [5000, 7000, 9000]
# result = list(map(lambda salary: salary + 1000, salaries))
# print(result)


# numbers = [2, 4, 6, 8]
# result = list(map(lambda x: x * 2, numbers))
# print(result)


# salaries = [5000, 8000, 10000]
# result = list(map(lambda salary: salary * 1.1, salaries))
# print(result)


# def increase_salary(salary):
#   return salary + 2000

# salaries = [4000, 6000, 9000]
# result = list(map(increase_salary, salaries))
# print(result)


# salaries = [4000, 6000, 9000, 12000]

# result = list(
#   map(
#     lambda salary: salary + 1000,
#     filter(lambda salary: salary > 6000, salaries)
#   )
# )
# print(result)


# numbers = [2, 5, 8, 10, 15]

# result = list(
#   filter(
#     lambda x: x > 10,
#     map(lambda x: x * 2, numbers)
#   )
# )
# print(result)


# numbers = [5, 10, 15]
# step1 = list(map(lambda x: x * 2, numbers))
# step2 = list(filter(lambda x: x > 15, step1))
# print(step2)


# salaries = [5000, 7500, 9000, 12000]

# result = list(
#   filter(
#     lambda salary: salary > 8000, 
#     map(lambda salary: salary + 1000, salaries)
#   )
# )

# print("Orijinal salaries:", salaries)
# print("New salaries and filtered salaries:", result)
# print(len(result))


salaries = [5000, 7500, 9000, 12000]

new_salaries = list(map(lambda salary: salary + 1000, salaries))
filtered_salaries = list(filter(lambda salary: salary > 8000, new_salaries))

print("Orijinal salaries: ", salaries)
print("New salaries:", new_salaries)
print("Filtered salaries:", filtered_salaries)
print("Count:" , len(filtered_salaries))