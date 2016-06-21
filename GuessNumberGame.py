import random
def guess_number():
    number = random.randint(1, 100)
    quite_word = 'i try but giving up like little bitch'
    count = 0
    guess = 0

    while guess != number and guess != quite_word:
        guess = input("Guess the number between 1 and 9, or print " + quite_word + " to stop: ")

        if guess == quite_word:
            print "I knew that you will give up"
            break

        guess = int(guess)
        count += 1

        if guess < number:
            print ("Low")
        elif guess > number:
            print ("Higth")
        else:
            print("You did it in " + str(count) + " times")

guess_number()