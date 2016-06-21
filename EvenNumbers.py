#This program return list of even numbers in basic list
b = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
def even_numbers(array):
    even = []
    if len(array) == 0:
        print "No elements in array"
    else:
        for i in array :
            if i % 2 == 0:
                even.append(i)
    return even
print even_numbers(b)