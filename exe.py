try:
    a = int(input("enter the numerator"))
    b = int(input("enter the denominator"))
    r = a/b
    print(r)
except ZeroDivisionError:
    print("denominator can't zero")
