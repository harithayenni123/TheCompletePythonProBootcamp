# sum=0
# for number in range(1, 101):
#     sum+=number
# print(sum)
for number in range(1, 101):

    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
          print("FizzBuz")
    else:
         print(number)