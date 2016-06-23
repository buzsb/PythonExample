#This program return list of even numbers in basic list
a = [1, 4, 9, 16, 25, 36, 'f', 49, 64, 81, 100, [2,3], -2]
def even_numbers(array):
    even = []
    if len(array) == 0:
        print "No elements in array"
    else:
        for i in array:
            if type(i) != int:
                continue
            if i % 2 == 0:
                even.append(i)
    return even

if __name__ == '__main__':
    print even_numbers(a)