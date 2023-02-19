n = 0
val = 0
for val in range(2, 50):
    for n in range(2, 50):
        if val % n == 0:
            break
        else:
            print(val)
            break
