def fullname(fname, lman):
    print("hello"+"  "+fname+"  "+lman)


fullname(fname="akash", lman="variyath")


def fullname(**kwargs):
    print("hello"+"  "+kwargs['fname']+"  "+kwargs['lman'])


fullname(fname='akash', lman="variyath")
