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
    Checks if all letters in the secret word have been guessed
    Returns true or false
    '''
    for elem in secret_word:
        if elem not in letters_guessed:
            return False #returns false if any letter in the secret word has not been guessed
    return True #only reached if everything has been guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    Returns a string made up of _ and letters from the secret word.
    Ex. If the word was 'dog' and O had been guessed, would return '_ O _'
    '''
    rtn = '' #empty string
    for elem in secret_word:
        if elem in letters_guessed: #if the letter has already been guessed
            rtn += elem
        else: #if the letter has not been guessed
            rtn += '_'
        rtn += ' '
    return rtn.strip() #remove trailing whitespace


def is_guess_in_word(guess, secret_word):
    return guess in secret_word
    pass


def page_break():
    print('------------------------------------') #page_break() is easier to type


def user_input(prompt):
    user_input = input(prompt) #if I'm being honest I don't know why this is different than just using input(prompt)
    return user_input


def get_guess(prompt, guess_list):
    '''
    Returns the user input using the prompt
    Useful because can be called recursively to handle invalid inputs
    '''
    letter = user_input(prompt).strip() #assign to variable & remove trailing whitespace
    if not letter.isalpha(): #no numbers/special characters. Must do this before attempting letter.upper()
            return get_guess('Please enter only letters: ', guess_list)
    letter = letter.upper() #easier to compare to guess_list if all uppercase
    if len(letter) != 1:
        return get_guess('Please enter exactly one letter: ', guess_list) #empty answers should be removed by isalpha(), but this would also catch
    elif letter in guess_list:
        return get_guess('Please guess a new letter: ', guess_list) #duplicate answers do not count against the player
    else:
        return letter #passed all checks


def color(item, colr): #colors stored in a single function so I can minimieze them all together
    if colr == 'red':
        return '\033[31m{}\033[00m'.format(item)
    elif colr == 'orange':
        return '\033[91m{}\033[00m'.format(item)
    elif colr == 'yellow':
        return '\033[93m{}\033[00m'.format(item)
    elif colr == 'green':
        return '\033[32m{}\033[00m'.format(item)
    elif colr == 'blue':
        return '\033[34m{}\033[00m'.format(item)
    elif colr == 'purple':
        return '\033[35m{}\033[00m'.format(item)
    elif colr == 'pink':
        return '\033[95m{}\033[00m'.format(item)
    elif colr == 'indigo':
        return '\033[94m{}\033[00m'.format(item)
    elif colr == 'rainbow':
        color_count = 0
        new_string = ''
        for elem in item:
            if elem == ' ':
                new_string += elem
                color_count += -1
            elif color_count == 0:
                new_string += color(elem, 'red')
            elif color_count == 1:
                new_string += color(elem, 'orange')
            elif color_count == 2:
                new_string += color(elem, 'yellow')
            elif color_count == 3:
                new_string += color(elem, 'green')
            elif color_count == 4:
                new_string += color(elem, 'blue')
            elif color_count == 5:
                new_string += color(elem, 'purple')
            elif color_count == 6:
                new_string += color(elem, 'pink')
                color_count = -1
            color_count += 1
        return new_string
    elif colr == 'rainbow sp': #I wrote this already for Captain Rainbow Checklist
        color_count = 0
        new_string = ''
        for elem in item:
            if color_count == 0:
                new_string += color(elem, 'red')
            elif color_count == 1:
                new_string += color(elem, 'orange')
            elif color_count == 2:
                new_string += color(elem, 'yellow')
            elif color_count == 3:
                new_string += color(elem, 'green')
            elif color_count == 4:
                new_string += color(elem, 'blue')
            elif color_count == 5:
                new_string += color(elem, 'purple')
            elif color_count == 6:
                new_string += color(elem, 'pink')
                color_count = -1
            color_count += 1
        return new_string
    else:
        return item


def print_ship(count, word_line, alpha_list): #this is all very ugly so I want to be able to minimize it
    '''
    Handles printing of the ASCII art based on # of incorrect guesses.
    Lights on the rocket turn red with each miss.
    '''
    if count == -1: #win
        print('                       /\\')
        print('                      /  \\')
        print('                     / /\\ \\')
        print('                    | (__) |')
        print('                    |  ' + color('o','green') + '   |') #can't use multiline with ''' ''' because of the coloring
        print('                    |   ' + color('o','green') + '  |')
        print('                    |  ' + color('o','green') + '   |')
        print('                    |   ' + color('o','green') + '  |')
        print('                   /|  ' + color('o','green') + '   |\\')
        print('                  / |   ' + color('o','green') + '  | \\')
        print('                 |  |  ' + color('o','green') + '   |  |')
        print('                 | /|______|\\ |')
        print('                 |/  ' + color('((()))','orange') + '  \\|')
        print(color('                    (((|)))','orange'))
        print(color('                     (((|)))','orange'))
        print(color('                    (((|)))','orange'))
        print(color('                     (((|)))','orange'))
        print(color('                     ((()))','orange'))
        print(color('                       ()','orange'))
        print('')
        print(color(' __     __  _____  ______   ___    _____  _____','rainbow'))
        print(color('|  |   |  ||  ___||__  __|/  _  \\ |  ___||  ___|','rainbow'))
        print(color('|  |__ |  ||  __|   |  | |  | |  ||  __| |  __|','rainbow'))
        print(color('|_____||__||__|     |__|  \\ ___ / |__|   |__|','rainbow'))
    elif count < -1 or count > 7:
        print(color('Something\'s gone wrong! Please restart the game.', 'red')) #this shouldn't happen
    else:
        print('      /\\')
        print('     /  \\')
        print('    / /\\ \\')
        print('   | (__) |')
        if count > 0:
            print('   |  ' + color('o','red') + '   |  ' + format_alpha(alpha_list))
        else:
            print('   |  o   |  ' + format_alpha(alpha_list))

        if count > 1:
            print('   |   ' + color('o','red') + '  |  ACCESS CODE: ' + word_line)
        else:
            print('   |   o  |  ACCESS CODE: ' + word_line)

        if count > 2:
            print('   |  ' + color('o','red') + '   |  ATTEMPTS REMAINING: ' + str(7-count) + '/7')
        else:
            print('   |  o   |  ATTEMPTS REMAINING: ' + str(7-count) + '/7')

        if count > 3:
            print('   |   ' + color('o','red') + '  |')
        else:
            print('   |   o  |')

        if count > 4:
            print('  /|  ' + color('o','red') + '   |\\')
        else:
            print('  /|  o   |\\')

        if count > 5:
            print(' / |   ' + color('o','red') + '  | \\')
        else:
            print(' / |   o  | \\')

        if count > 6:
            print('|  |  ' + color('o','red') + '   |  |')
        else:
            print('|  |  o   |  |')

        print('| /|______|\\ |')
        print('|/    \\/    \\|')


def update_alpha(alpha_list, target, clr):
    '''
    A list of the alphabet is printed beside the rocket.
    This function makes it easier to update these letters with the correct colors
    (Red for an incorrect guess and green for a correct guess).
    '''
    alpha_list[alpha_list.index(target)] = color(target, clr)
    return alpha_list #use with alpha_list = update_alpha(a,t,c)


def format_alpha(alpha_list):
    '''
    Spaces the alphabet list nicely for printing. Returns string.
    '''
    rtn = ""
    for elem in alpha_list:
        rtn += elem
        rtn += ' ' #space like 'A B C...'
    return rtn.strip() #remove trailing whitespace


def spaceman(secret_word):
    '''
    Runs once through the spaceman program
    '''
    guess_list = [] #empty list

    f = open('alphabet.txt', 'r')
    alpha_list = f.readlines()
    f.close()
    alpha_list = alpha_list[0].split(' ') #create a list of letters to color accordingly

    wrong_count = 0 #count of incorrect guesses
    print('Get to space by correctly guessing letters in the rocket\'s launch code!\nBe careful though, you only get ' + color('7','red') + ' incorrect guesses before you\'re locked out.')
    print('The launch code has: ' + str(len(secret_word)) + ' letters.')
    page_break()
    #print(secret_word) #testing only
    while is_word_guessed(secret_word, guess_list)==False and wrong_count < 7: #haven't won or lost
        print_ship(wrong_count, get_guessed_word(secret_word, guess_list),alpha_list) #print ship art and info
        guess = get_guess('Enter a letter: ', guess_list)
        guess_list.append(guess) #add new guess to the guess list
        if is_guess_in_word(guess, secret_word):
            print(color('That letter is in the launch code!', 'green')) #correct
            alpha_list = update_alpha(alpha_list, guess, 'green')
        else:
            print(color('Oops! That letter is not in the launch code.', 'red')) #incorrect
            alpha_list = update_alpha(alpha_list, guess, 'red')
            wrong_count += 1 #increment wrong_count by 1
        page_break()
    if wrong_count >= 7: #lose condition
        print_ship(7, get_guessed_word(secret_word, guess_list), alpha_list)
        print(color('ACCESS DENIED. The code was ' + secret_word + '.', 'red'))
    else: #win condition: once the while loop ends, the player has either won or lost
        print(color('ACCESS GRANTED. The code was ' + secret_word + '.', 'green'))
        print_ship(-1, '', alpha_list)


def play_again(): #separate from main() so I can call recursively
    again = user_input("Play again? [Y/N]: ")
    if not again.isalpha():
        return play_again()
    elif again.upper().strip() == "YES" or again.upper().strip() == "Y":
        return True
    elif again.upper().strip() == "NO" or again.upper().strip() == "N":
        return False
    else:
        return play_again() #invalid input

def main(): #main function
    playing = True #prevents unnecessary global variables
    while playing:
        secret_word = load_word()
        spaceman(secret_word)
        playing = play_again()


main()
