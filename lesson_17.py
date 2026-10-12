# file = open("Employee.txt", "w")
# file.write("James - Operator")
# file.close()


# file = open("employees.txt", "w")

# file.write("James - Operator\n")
# file.write("Michael - Driver\n")
# file.write("John - Mechanic\n")

# file.close()


# file = open("employees.txt", "a")
# file.write("Daniel - Electrician\n")
# file.close()


# file = open("employees.txt", "r")
# print(file.read())

# file.close()


# file = open("employees.txt", "r")

# for line in file:
#   print(line.strip())

# file.close()


# file = open("employees.txt", "r")
# count = 0

# for line in file: 
#   print(line.strip())
#   count = count + 1

# file.close()

# print("Total employees: ", count)



# workers = ["James", "Michael", "John", "David", "Daniel"]

# count = 0

# for worker in workers:
#   if len(worker) > 5:
#     count += 1

# print("Total workers: ", count)


workers = ["James", "Michael", "John", "David", "Daniel"]

count = 0

for worker in workers:
  if len(worker) > 4 and worker[0] == "J":
    count += 1

print("Total workers: ", count)