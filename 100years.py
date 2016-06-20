#Simple program that ask you age and show year that you will turn 100 years old


from datetime import date
def calculate_years(age):
    now = date.today().year
    calculate = (now - age) + 100
    return calculate


def say_when():
    try:
        age = int(input("Enter youre age: "))
        add_age = calculate_years(age)
        print "You 100 yers whill be in  " + str(add_age)
    except NameError:
        print "you not print your age punk!"
        say_when()
say_when()