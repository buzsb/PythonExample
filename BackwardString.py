# programthat asks the user for a long string containing multiple words
# Print back to the user the same string, except with the words in backwards order

def user_string():
    try:
        you_string = input("Print you long string: ")
    except SyntaxError:
        print 'You dont print enything'
    else:
        
        you_revers_str = backwards_string(you_string)
        return you_revers_str

def backwards_string(you_string):

    if type(you_string) != str:
        raise TypeError

    split_string = you_string.split()

    revers_str = ' '.join(split_string[::-1])
    return revers_str

if __name__ == '__main__':
    try:
        print user_string()
    except TypeError:
        print 'You input not a string'
