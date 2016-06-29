# Program that asks the user for a long string containing multiple words
# Print back to the user the same string, except with the words in
# backwards order


def user_string():
    your_string = raw_input("Print your long string: ")
    you_revers_str = backwards_string(your_string)
    return you_revers_str


def backwards_string(your_string):

    if not isinstance(your_string, basestring):
        raise TypeError

    split_string = your_string.split()

    revers_str = ' '.join(split_string[::-1])
    return revers_str

if __name__ == '__main__':
    try:
        print user_string()
    except TypeError:
        print 'Your input not a string'
