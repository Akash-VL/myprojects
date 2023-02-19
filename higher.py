def up(txts):
    return txts.upper()


def down(txts):
    return txts.lower()


def fun(hy):
    assi = hy("hai there")
    print(assi)


fun(up)
fun(down)
