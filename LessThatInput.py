#Program show what elements in array less that input number

a = [1, 1, 2, 3, [5, 6],5, 8, 'ss', 21, 34, 55, 89]

def less_than_input(array, number):
    new_list = []

    if type(number) == str:
        return array

    for i in array:
        if i < number:
            new_list.append(i)
    return new_list

if __name__ == '__main__':
    print less_than_input(a, 35)

