# Program that generate random password and ask how strong you want pasword
import random
import string


def low_leters():
    return random.choice(string.ascii_lowercase)


def numbers():
    return random.randint(0, 9)


def up_leters():
    return random.choice(string.ascii_uppercase)


def password_generator(length=8):
    choice = input(
        'Please choice how strong you want you password, print 1 for weak, 2 for medium and 3 for strong: ')
    password = []
    while len(password) < length:
        if choice == 1:
            password.append(low_leters())

        if choice == 2:
            crt = random.choice((low_leters(), numbers()))
            password.append(str(crt))

        if choice == 3:
            crt = random.choice((low_leters(), numbers(), up_leters()))
            password.append(str(crt))
    print password
    password = ''.join(password)

    return password

print password_generator(10)
