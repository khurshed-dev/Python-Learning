# employees = []
# name = input("Enter emplyee name: ")
# employees.append(name)
# print("Emplyees: ", employees)


employees = []
while True:
  name = input("Enter employee name: ")
  if name == "stop":
    break
  employees.append(name)

print("Employees: ",employees)
print("Total employees: ",(len(employees)))

search = input("Search employee: ")
for employee in employees:
  if employee.lower() == search.lower():
    print("Employee found!")
    break
else:
  print("Employee not found!")

remove_name = input("Remove employee: ")
for employee in employees:
  if employee.lower() == remove_name.lower():
    employees.remove(employee)
    break
else:
  print("Employee not removed!")

print("Updated employees:",employees)
