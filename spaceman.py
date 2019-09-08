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
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    return False

    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


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
    print("Help spaceman get to space by correctly guessing letters in the launch code!\nBe careful though, you only get 7 incorrect guesses before the rocket falls apart.")
    print("The launch code has: " + str(length) + " letters.")
    page_break()
    print(secret_word)
    while is_word_guessed(secret_word, guess_list)==False:
        print(get_guessed_word)
        guess = get_guess("Enter a letter: ", guess_list)
        guess_list.append(guess)
        if is_guess_in_word(guess, secret_word):
            print("That letter is in the launch code!")
        else:
            print("Oops! Your rocket just lost a piece.")
        page_break()

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost





#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
