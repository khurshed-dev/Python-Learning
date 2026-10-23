# salaries = [5000, 8000, 12000]
# result = any(salary > 10000 for salary in salaries)
# print(result)


# numbers = [2, 4, 6, 9]
# result = all(number % 2 == 0 for number in numbers)
# print(result)


# salaries = [6000, 8000, 10000, 12000]

# result1 = any(salary > 11000 for salary in salaries)
# result2 = all(salary >= 6000 for salary in salaries)

# print(result1)
# print(result2)


# salaries = [5000, 7000, 9000, 12000]

# result = all(
#   salary >= 7000
#   for salary in salaries
#   if salary > 6000
# )
# print(result)


# scores = [85, 72, 90, 58, 95]

# result1 = any(
#   score < 60
#   for score in scores
# )

# result2 = all(
#   score >= 50
#   for score in scores
# )

# print(result1)
# print(result2)

scores = [85, 72, 95, 58, 90]
any_score = any(score < 60 for score in scores)
all_scores = all(score >= 50 for score in scores)
any_score1 = any(score > 90 for score in scores)
all_score1 = all(score >= 60 for score in scores)


print("Any score below 60:", any_score)
print("All scores at least 50:", all_scores)
print("Any score above 90:", any_score1)
print("All scores at least 60:", all_score1)
