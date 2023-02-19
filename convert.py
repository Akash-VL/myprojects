store = [('shirt', 40),
         ('pant', 50),
         ('shoes', 35)]


def convert(x): return (x[0], x[1]*65)


newstore = map(convert, store)
for i in newstore:
    print(i)
