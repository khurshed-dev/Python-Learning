# def add_numbers(*args):
#   total = 0
#   for number in args:
#     total += number
#   return total
 

# def add_numbers(*args):
#   return sum(args)
# print(add_numbers(10, 20, 30))


# numbers = [10, 20, 30, 40]
# total = sum(numbers)
# print(total)


# salaries = [5000, 6000, 7000]
# total = sum(salaries)
# avarage = total / len(salaries)
# print(avarage)


# salaries = []
# total = sum(salaries)
# print(total)


# salaries = []
# total = sum(salaries)
# averange = total / len(salaries)
# print(averange)


# salaries = [4000, 6000, 8000]

# if len(salaries) > 0:
#   averange = sum(salaries) / len(salaries)
#   print("Averange salary:", averange)
# else:
#   print("No emoloyee")


def calculate_averange(salaries):
  if len(salaries) > 0:
    result = sum(salaries) / len(salaries)
    return result
  else:
    return 0
salaries = [5000, 7000, 9000, 11000]
  
result = calculate_averange(salaries)
print("Averange salary:", result)
  

