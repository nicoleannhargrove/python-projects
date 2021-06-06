#!C:\Program Files\Python39\Python39\python.exe python

#Python implementation

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5/ 9

print(fahrenheit, "F is", round(celsius, 2), "C")