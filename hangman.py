# Step1: import external libraries
import random 

# Step2: make a list if word
#words = ['orange','lime','lemon','melon','grape','mango']

words = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon']

while True:
    #Step 3
    start = input("Press enter / return to start, or enter Q to quit")

    if start.lower() == 'q':
        break

    #Step4: pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
    
    strike = len(secret_word)+2
    print(strike)
    #Step5: add contition of win or loose
    while len(bad_guesses) < strike and len(good_guesses) != len (list( secret_word)):
        # Step 6: draw  spaces
        # draw guessed letters, spaces and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print ( letter , end='')
            else:
                print('_', end=' ')
                #print ('')

        print('\nStrikes : {} / {}'.format(len(bad_guesses), strike))
        print ('')

        # Step 7: take guess
        guess = input ("Guess a letter : ").lower()

        # Step8: Check the input from user for boundary conditions
        if  len(guess) != 1:
            print ("You can only guess a single letter !") 
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print ("You can only guess letters !")
            continue
        
        # Step9: print out win / lose

        if guess in secret_word:
            for i in range(secret_word.count(guess)):
                 good_guesses.append(guess)

        if len (good_guesses) == len ( list(secret_word)):
            print ("You win : The word was {}". format(secret_word))
            break
        else:
            bad_guesses.append(guess)
    
    else:   # else for the while, if you win, it will never be executed
        print ("You didn't guess it: my secret word was {}". format(secret_word))

