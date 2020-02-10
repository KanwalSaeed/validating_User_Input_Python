user_name = input("Enter User Nmae: ")
password = input("Enter password:")
if user_name and password:
   if user_name == "Kanwal" and password == "Saeed":
       print("Login Successfully")
   else:
       print("Incorrect UserName or Password. ")
else:
    print("Required UserName or Password")

first_number =  int(input("Enter First Number: "))
second_number = int(input(" Enter Second Number: "))
result = 0
if first_number and second_number:
    result = first_number + second_number * first_number
else:
    print("Required First Number or second Number.")
print(result)

