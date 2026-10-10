# attempts = 0

# while attempts < 3:
#   print("Try again!")
#   attempts = attempts + 1

# print("Account blocked!")

attempts = 0
while attempts < 3:
    password = input("Enter your password: ")
    if password == "1234":
        print("Password correct!")
        break
    else:
        print("Incorrect password. Try again.")
        attempts = attempts + 1
        print("Account blocked!" if attempts == 3 else "")


