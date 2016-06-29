# Simple program that ask you age and show year that you will turn 100
# years old

from datetime import date


def calculate_years(age):
    if not isinstance(age, int):
        return False
    if age <= 0 or age >= 100:
        return False

    now = date.today().year
    calculate = (now - age) + 100

    return calculate


def say_when():
    age = raw_input("Enter your age: ")
    add_age = calculate_years(age)
    if add_age == False:
        print "No! print your age, not some shit, age you understand?"
        say_when()
    else:
        print "100 years you will celebrate in " + str(add_age)

if __name__ == '__main__':
    say_when()
