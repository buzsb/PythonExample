#Finding Fibonacci number in two ways, first simple summing, second recursive method
def fib(n):
    if n < 1:
        raise ValueError
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
try:
    print fib(17)
except ValueError:
    print "hi"


def rfib(n):
    if n < 2:
        return n
    a = rfib(n - 1) + rfib(n - 2)
    return a 

print rfib(17)