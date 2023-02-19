
a = int(input('enter the number'))
k = 0
for prime in range(2, a):

    if a % prime == 0:
        print('not prime')
        break
    else:
        print('is prime')
        break
