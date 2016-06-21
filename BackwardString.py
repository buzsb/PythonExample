# programthat asks the user for a long string containing multiple words
# Print back to the user the same string, except with the words in backwards order

def backwards_string():
    you_string = input("Print you long string: ")

    split_string = you_string.split()

    revers_str = ' '.join(split_string[::-1])
    print revers_str

backwards_string()

