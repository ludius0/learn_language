import random


def game_menu():
    print("Welcome to hangman game!\nWords are chosen randomly from list of 1000 words.\nFor every missed letter you lose 1 live. You begin with 10 lives.")
           
    r_word = pick_up_word()
    game_loop(r_word)
    
def pick_up_word():
    with open("words_list.txt", "r") as f:
        w_list = []
        for item in f:
            w_list.append(item)

    w_list = [i.split('\n', 1)[0] for i in w_list]
#   map(str.lower,w_list)
    r_word = random.choice(w_list)
    return r_word
    

def user_guess():
    guess = input("Please enter the letter you guess: ")
    map(str.lower, guess)
    return guess

def result(r_word):
    if guesses == lives:
        print("Failure. The word was:" , r_word)
    else:
        print("YOU'VE WON!")
        print(f"You made {guesses} wrong guesses")

    game_end = input("Do you want play again? [yes/no]: ")
    if game_end == "yes":
        game_menu()
    else:
        None
   

def game_loop(r_word):
    print("The length of the word is: " , len(r_word)) if r_word else None

    global guesses
    guesses = 0
    letters_guessed = []
    word = []
        
    for i in range(len(r_word)):
        word.append('_ ')

    while guesses < lives:
        guess = user_guess()

        if(guess in r_word):
            print("The letter is in the word.")
            for index, letter in enumerate(r_word):
                if letter == guess:
                        word[index] = guess
            letters_guessed.append(guess)

        else:
            print("The letter is not in the word.")
            guesses = guesses + 1
            letters_guessed.append(guess)

        print(f"you have guessed these letters: {''.join(letters_guessed)}")
        print(f"Letters matched so far {''.join(word)}")
            
        print(f"You have {lives - guesses} lives left." + "\n")

        if ''.join(word) == r_word:
            break
        
    result(r_word)


lives = 10

game_menu()
        

