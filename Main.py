score_h = [0]

def EnterName():
    try:
        name = input("What is your name?")
        if len(name) > 0:
            print("Welcome to HorL,", name + ".", 'Press \'s\' anytime to show your score.')
            DrawCards()

        else:
            print("There was an error. Please try again.")
            return EnterName()

    except:
        print("There was an error. Please try again.")
        return EnterName()

def DrawCards():
    try:
        from random import randint
        firstcard = randint(1,10)
        secondcard = randint(1,10)

        #Uncomment below to see card numbers
        #print(firstcard, "    ", secondcard)

        if secondcard == firstcard:
            firstcard = 1
            secondcard = 2
            DrawCards()

        else:
            #Clean this up later
            stringfirstcard = str(firstcard)

            #Actual answer
            gameanswer = SetWin(firstcard, secondcard)

            #Uncomment below to see answer
            #print(str(gameanswer))

            guess = str(UserGuess(input("Is the second card higher(h) or lower(l) than " + stringfirstcard + "?")))

            if str(gameanswer) == guess:
                print("Hooray! You win the round!")
                ChangeScore(1)
                DrawCards()

            else:
                print("Whoops. You lose this round. Try again!")
                DrawCards()

    except:
        print('Error. Try again')
        DrawCards()

def SetWin(first,second):
    if second > first:
        return True
        print(True)
    else:
        return False
        print(False)

def UserGuess(guess):
    try:
        if guess.lower() == 'h':
            return True

        elif guess.lower() == 'l':
            return False

        elif guess.lower() == 's':
            print(CurrentPoints())
            DrawCards()

        else:
            print("Whoops. Enter 'h' for higher or 'l' for lower or 's' to show your score")
            DrawCards()

    except:
        print("There was an error. Try again.")
        DrawCards()

def Main():
    EnterName()

def InitialPoints():
    return score_h[0]

def CurrentPoints():
    return score_h[-1]

def ChangeScore(addedPoints):
    score_h.append(CurrentPoints() + addedPoints)
    return CurrentPoints()

Main()


