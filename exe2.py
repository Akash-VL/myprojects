try:
    a = int(input("enter the numerator"))
    b = int(input("enter the denominator"))
    r = a/b
    print(r)
except ZeroDivisionError as e:
    print(e)
    print("are u stupid")
except ValueError as v:
    print(v)
    print("datatype nokkado")
