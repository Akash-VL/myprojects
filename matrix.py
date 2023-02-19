a = [[1, 7, 3],
     [6, 1, 4],
     [8, 9, 7]]
b = [[1, 0, 0],
     [1, 7, 7],
     [8, 1, 2]]
s = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            s[i][j] += a[i][k]*b[k][j]
for n in s:
    print(s)
