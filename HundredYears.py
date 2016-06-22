#Simple program that ask you age and show year that you will turn 100 years old

from datetime import date

def calculate_years(age):
    if age <= 0 or  age >= 100:
        return False
    now = date.today().year
    calculate = (now - age) + 100
    return calculate


def say_when():
    try:
        age = int(input("Enter youre age: "))
        add_age = calculate_years(age)
        if add_age == False:
            print "No print you age, not some shit, age you understand?"
            say_when()
        else:
            print "100 years you will celebrate in " + str(add_age)
            
    except NameError:
        print "you dont print your age punk!"
        say_when()

if __name__ == '__main__':
    say_when()