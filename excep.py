import sys
try:
    x = int(input("x : "))
    y = int(input("y : "))
except ValueError:
    print("invalid input")
    sys.exit(1)
try :
  c = x/y
except ZeroDivisionError:
    print("can not divide by zero")
    sys.exit(1)

print(c)