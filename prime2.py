
start = int(input('starting'))
stop = int(input('stoping'))
for val in range(start, stop+1):
    for n in range(2, val):
        if val % n == 0:
            break
        else:
            print(val)
            break
