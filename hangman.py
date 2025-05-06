import random
import string
from hangman_words import words

#Selecting our word from the hangman_words.py words list
def clean_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = clean_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
       
        #Getting user Input
        used_letter = input('Guess a Letter: ').upper()
        if used_letter in alphabets - used_letters: # Only proceed if the letter is valid 
            used_letters.add(used_letter)
            if used_letter in word:
                word_letters.remove(used_letter) # Remove from word_letters if the guess is correct
        elif used_letter in used_letters:
            print('You have already guessed that letter, Please Try Again!')
        else:
            print('Please Enter A Valid Input')
            
        #Show the used letters to the user and also the progress of hangman
        print('You have used:',' '.join(sorted(used_letters)))
        word_list= [letter if letter in used_letters else '_' for letter in word]
        print('Word:',' '.join(word_list))


    print(f'Congratulations, You have guessed the word {word} correctly!')
        
hangman()