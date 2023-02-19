def split():
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
         '12', '13', '14', '15', '16', '17', '18', '19', '20']
    even = []
    odd = []
    for i in range(len(a)):
        if (i % 2 == 0):
            even.append(i)
            print(even)
        else:
            odd.append(i)

            print(odd)
