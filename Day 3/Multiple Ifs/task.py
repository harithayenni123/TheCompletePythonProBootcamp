print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        bill=5
        print("Child ticket are $5.")
    elif age <= 18:
        bill=7
        print("Youth ticket are $7.")
    else:
        print("Adult ticket are $12.")
        bill=12
    want_photo=input("anybody wants photo, if want say yes if not say no")

    if want_photo=="yes":
        bill+=3
    print(f"total bill is {bill}:")
else:
    print("Sorry you have to grow taller before you can ride.")
