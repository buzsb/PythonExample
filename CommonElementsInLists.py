#Program make two random lists and serch common elements
import random

def common_element_in_lists():
    a, b  = [], []
    c = []
    while len(a) < 10 and len(b) < 11:
        a.append(random.randint(1, 100))
        b.append(random.randint(1, 100))
    print a,b
    for i in a:
        if i in b:
            c.append(i)
    return c

print common_element_in_lists()
