# for adding number of paramenters we have to use * with a name
def sum(*args):
    sum = 0
    lissa = list(args)
    print(lissa)
    for i in args:
        sum += i
    return sum


print(sum(1, 2, 3, 4, 5, 6, 7, 8))
