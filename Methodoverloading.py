# Efficient method for overloading
from multipledispatch import dispatch


@dispatch(int, int, int)
def sum(a, b, c):
    result = a + b + c
    print(result)


@dispatch(float, float, float)
def sum(w, r, t):
    result = w + r + t
    print(result)


sum(2, 3, 4)
sum(3.1, 2.2, 3.5)
