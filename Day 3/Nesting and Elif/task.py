# nested if
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age>=18:
#         print("pay 12$")
#     else:
#         print("pay 7$")
# else:
#     print("Sorry you have to grow taller before you can ride.")
# elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
     print("You can ride the rollercoaster")
     age = int(input("What is your age? "))
     if age<12:
         print("pay $5")
     elif age<=18:
         print("pay $7")
     elif age>18:
         print("pay $18")
else:
     print("Sorry you have to grow taller before you can ride.")

