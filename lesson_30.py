# salaries = [5000, 7000, 9000, 11000]

# lowest = min(salaries)
# highest = max(salaries)

# print("Lowest salaty: ", lowest)
# print("Highest salary: ", highest)


# salaries = [6000, 8500, 4000, 12000, 7500]

# difference = max(salaries) - min(salaries)

# print(difference)


def salary_info(salaries):
  if len(salaries) > 0:
    lowest = min(salaries)
    highest = max(salaries)
    return highest - lowest
  else:
    return 0 
salaries = [4000, 6500, 9000, 12000, 7500]
result = salary_info(salaries)
print("Salary difference:", result)