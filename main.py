print("This program  will prompt the user for an integer. It will then count to the number provided by the user.")
print("Each digit that is evenly divisible by 3 will be replaced with Fizz.")
print("Each digit that is evenly divisible by 5 will be replaced with Buzz.")
print("Each digit that is evenly divisible by both 3 and 5 will be replaced with Fizzbuzz.")
print("So let's get started, shall we?")

count = 0
countTo = int(input("Please enter an integer: "))
while count < countTo:
    count = count+1
    if count % 3 == 0 and count % 5 == 0:
        print("Fizzbuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)