import random

def hangman(word):
    word = word.lower()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    lives = 6
    win = False
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left')
        print('Used letters:', ' '.join(used_letters))
        print('Word:', ' '.join([letter if letter in used_letters else '_' for letter in word]))
        guess = input('Guess a letter: ').lower()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1
        elif guess in used_letters:
            print('You already used that letter')
        else:
            print('Invalid input')
        if len(word_letters) == 0:
            win = True
            break
    if win:
        print('Congratulations, you won!')
    else:
        print('Sorry, you lost. The word was:', word)

words = ['das', 'spiel', 'ist', 'tripleAAA', 'niveau']
hangman(random.choice(words))