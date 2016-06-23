#Program make two random lists and serch common elements
import random

def common_elements_finding(a, b):
    c = []
    for i in a:
        if type(i) == str:
            pass
        if i in b:
            c.append(i)
    return c

def common_elements_in_lists():
    a, b  = [], []
    while len(a) < 10 and len(b) < 11:
        a.append(random.randint(1, 10))
        b.append(random.randint(1, 10))
    print a,b

    common_array = common_elements_finding(a, b)

    return common_array

if __name__ == '__main__':
    print common_elements_in_lists()