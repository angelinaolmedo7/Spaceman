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
    rtn = ''
    for elem in secret_word:
        if elem in letters_guessed:
            rtn += elem
        else:
            rtn += '_'
        rtn += ' '
    return rtn.strip()


def is_guess_in_word(guess, secret_word):
    return guess in secret_word
    pass


def page_break():
    print('------------------------------------')


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def get_guess(prompt, guess_list):
    letter = user_input(prompt).strip()
    if not letter.isalpha():
            return get_guess('Please enter only letters: ', guess_list)
    letter = letter.upper()
    if len(letter) != 1:
        return get_guess('Please enter exactly one letter: ', guess_list)
    elif letter in guess_list:
        return get_guess('Please guess a new letter: ', guess_list)
    else:
        return letter


def color(item, colr):
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
    elif colr == 'rainbow sp':
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


def print_ship(count, word_line, alpha_list):
    if count == -1:
        print('                       /\\')
        print('                      /  \\')
        print('                     / /\\ \\')
        print('                    | (__) |')
        print('                    |  ' + color('o','green') + '   |')
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
    alpha_list[alpha_list.index(target)] = color(target, clr)
    return alpha_list


def format_alpha(alpha_list):
    rtn = ""
    for elem in alpha_list:
        rtn += elem
        rtn += ' '
    return rtn.strip()


def spaceman(secret_word):
    length = len(secret_word)
    guess_list = []

    f = open('alphabet.txt', 'r')
    alpha_list = f.readlines()
    f.close()
    alpha_list = alpha_list[0].split(' ')

    wrong_count = 0
    print('Get to space by correctly guessing letters in the rocket\'s launch code!\nBe careful though, you only get ' + color('7','red') + ' incorrect guesses before you\'re locked out.')
    print('The launch code has: ' + str(length) + ' letters.')
    page_break()
    #print(secret_word)
    while is_word_guessed(secret_word, guess_list)==False and wrong_count < 7:
        print_ship(wrong_count, get_guessed_word(secret_word, guess_list),alpha_list)
        guess = get_guess('Enter a letter: ', guess_list)
        guess_list.append(guess)
        if is_guess_in_word(guess, secret_word):
            print(color('That letter is in the launch code!', 'green'))
            alpha_list = update_alpha(alpha_list, guess, 'green')
        else:
            print(color('Oops! That letter is not in the launch code.', 'red'))
            alpha_list = update_alpha(alpha_list, guess, 'red')
            wrong_count += 1
        page_break()
    if wrong_count >= 7:
        print_ship(7, get_guessed_word(secret_word, guess_list), alpha_list)
        print(color('ACCESS DENIED. The code was ' + secret_word, 'red'))
    else:
        print(color('ACCESS GRANTED. The code was ' + secret_word, 'green'))
        print_ship(-1, '', alpha_list)


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
