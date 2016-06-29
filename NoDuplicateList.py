# Function that takes a list and returns a new list that contains all the
# elements of the first list minus all the duplicates
a = [1, 2, 2, [1, 2], [1, 2]]


def list_remuve_duplicates(array):
    nd_list = []
    for i in array:
        if i in nd_list:
            continue
        else:
            nd_list.append(i)

    return nd_list

if __name__ == '__main__':
    try:
        print list_remuve_duplicates(a)
    except TypeError:
        print "You can`t iterate number"
