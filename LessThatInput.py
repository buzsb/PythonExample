#Program show what elements in array less that input number

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_than_input(array):
    num = int(raw_input("Choose a number: "))

    new_list = []

    for i in array:
        if i < num:
            new_list.append(i)
    return new_list

print less_than_input(a)

