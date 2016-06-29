# Finding Fibonacci number in two ways, first simple summing, second
# recursive method


def fib(n):
    if n < 1 or type(n) == str:
        raise ValueError
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def rfib(n):
    if type(n) == str:
        return "This is not a namber"
    if n < 2:
        return n
    a = rfib(n - 1) + rfib(n - 2)
    return a

if __name__ == '__main__':
    try:
        print fib('dd')
    except ValueError:
        print "What is wrong with you?"

    print rfib(12)
