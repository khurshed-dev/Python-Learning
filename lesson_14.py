# # workers = ["Ali", "Rustam", "Karim"]

# # if "Ali" in workers:
# #   print("Employee found!")
# # else:
# #   print("Employee not found!")


# workers = ["Ali", "Rustam", "Karim", "Said"]

# name = input("Enter employee name: ")

# if name in workers:
#   print("Employee found")
# else:
#   print("Employee not found!")


# workers = ["Ali","Rustam", "Karim",  "Said", "Khurshed"]
# name = input("Enter employee name: ")
# if name in workers:
#   print("Employee found!")
# else:
#   print("Employee not found!")


# workers = ["ali", "rustam", "karim"]

# name = input("Enater employee name: ").lower()

# if name in workers:
#   print("Employee found!")
# else:
#   print("Employee not found!")



# workers = ["Ali", "Rustam", "Karim"]

# name = input("Enter employee name: ").lower()

# for worker in workers:
#   if name == worker.lower():
#     print("Employee found!")
#     break
# else:
#   print("Employee not found!")


workers = ["Ali", "Rustam", "Khurshed", "Karim"]

name = input("Enter employee name: ").lower()

for worker in workers:
  if name == worker.lower():
    print("Employee found!")
    break
else:
    print("Employee not found!")