#!C:\Program Files\Python39\Python39\python.exe python

value = int(input("Enter an integar value: "))

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)