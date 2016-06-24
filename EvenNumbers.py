#This program return list of even numbers in basic list
list_a = [1, 4, 9, 16, 25, 36, 'f', 49, 64, 81, 100, [2,3], -2]
def even_numbers(list_a):
    even = []
    for i in list_a:
        if not isinstance(i, int):
            continue
        if i % 2 == 0:
            even.append(i)
    return even

if __name__ == '__main__':
    print even_numbers(list_a)