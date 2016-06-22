import random

def compare_numbers(number, guess):
    cow_bull = {'Cows': 0,'Bulls': 0} 
    user_guess = str(guess)
    for i in range(len(user_guess)):
        if user_guess[i] == number[i]:
            cow_bull['Cows'] += 1
        elif user_guess[i] in number and user_guess[i] != number[i]:
            cow_bull['Bulls'] += 1
    return cow_bull


def cows_and_bulls():
    number = str(random.randint(1000, 9999))
    print number
    count_trys = 0
    print("Ruls: guess a 4-digit number.\n For every digit that the user guessed correctly in the correct place, they have a 'cow'. \n For every digit the user guessed correctly in the wrong place is a 'bull'.")
    while True:
        guess = input('Try guess a 4 digit number, ') 
        answer = compare_numbers(number, guess)
        count_trys += 1

        if answer['Cows'] == 4:
            print "You win the number is " + number + ' you mom can be proud'
            break
        else:
            print 'No No, not correctly.\nTry again!.\nTry harder!\nYou have %s - cows and %s - buls' % (answer['Cows'], answer['Bulls'])

cows_and_bulls()
            
