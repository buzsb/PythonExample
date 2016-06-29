# Program show what elements in array less that input number

a = [1, 1, 2, 3, [5, 6], 5, 8, 'ss', 21, 34, 55, 89]


def less_than_input(list_a, number):
    new_list = []

    if not isinstance(number, (int, float)):
        return new_list

    for i in list_a:
        if i < number:
            new_list.append(i)
    return new_list

if __name__ == '__main__':
    print less_than_input(a, 35)
