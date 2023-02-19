li = [('sasi', 'b', 3),
      ('remesh', 'a', 6),
      ('titan', 'c', 9)]


# def ind(ind): return ind[1]
def ind(ind): return ind[0]
# def ind(ind): return ind[2]


li.sort(key=ind)
print(li)
