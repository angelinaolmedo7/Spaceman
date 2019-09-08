import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word.upper()

def is_word_guessed(secret_word, letters_guessed):
    for elem in secret_word:
        if elem not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    rtn = ""
    for elem in secret_word:
        if elem in letters_guessed:
            rtn += elem
        else:
            rtn += "_"
        rtn += " "
    return rtn.strip()


def is_guess_in_word(guess, secret_word):
    return guess in secret_word
    pass


def page_break():
    print("------------------------------------")


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def get_guess(prompt, guess_list):
    letter = user_input(prompt).upper().strip()
    if len(letter) != 1:
        return get_guess("Please enter exactly one letter: ", guess_list)
    elif letter in guess_list:
        return get_guess("Please guess a new letter: ", guess_list)
    else:
        return letter


def spaceman(secret_word):
    length = len(secret_word)
    guess_list = []
    wrong_count = 0
    print("Help spaceman get to space by correctly guessing letters in the launch code!\nBe careful though, you only get 7 incorrect guesses before the rocket falls apart.")
    print("The launch code has: " + str(length) + " letters.")
    page_break()
    print(secret_word)
    while is_word_guessed(secret_word, guess_list)==False and wrong_count < 7:
        print(get_guessed_word(secret_word, guess_list) + " | Incorrect guesses: " + str(wrong_count) + "/7")
        guess = get_guess("Enter a letter: ", guess_list)
        guess_list.append(guess)
        if is_guess_in_word(guess, secret_word):
            print("That letter is in the launch code!")
        else:
            print("Oops! Your rocket just lost a piece.")
            wrong_count += 1
        page_break()
    if wrong_count >= 7:
        print ("Dang. You lost. The launch code was " + secret_word)
    else:
        print ("Wow! You won. The launch code was " + secret_word)
    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost





#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
