import random
import string
from hangman_words import words


# hangman illustrations based on the remaining number of lives
illustrations = [
''' 
    |
    |
    O
   /|\\
   / \\
''' ,
'''
    |
    |
    O
   /|\\
   / 
''',
'''
    |
    |
    O
   /|\\
   
''',
'''
    |
    |
    O
   /|
   
''',
'''
    |
    |
    O
    |
   
''',
'''
    |
    |
    O
   
   
''',
'''
    |
    |
    

    (RIP)
'''
]

#Selecting our word from the hangman_words.py words list
def clean_word(words):
    while True:
        word = random.choice(words)
        if len(word)<6 and ' ' not in word and '-' not in word:
            return word.upper()


def hangman():
    word = clean_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    lives=6 #basic hangman gameflow
    print(f"The Word has {len(word)} letters.")
    while len(word_letters) > 0 and lives > 0:
       
        #Getting user Input
        used_letter = input('\nGuess a Letter: ').upper()
        if used_letter in alphabets - used_letters: # Only proceed if the letter is valid 
            used_letters.add(used_letter)
            if used_letter in word:
                word_letters.remove(used_letter) # Remove from word_letters if the guess is correct
            else:
                lives -= 1
                print('Wrong Guess! You lost a life.')
        elif used_letter in used_letters:
            print('You have already guessed that letter, Please Try Again!')
        else:
            print('Please Enter A Valid Input')
            
        #Show the used letters to the user and also the progress of hangman
        print(f"You have {lives} lives remaining and You have used:",' '.join(sorted(used_letters)))
        print(illustrations[6-lives])
        word_list= [letter if letter in used_letters else '_' for letter in word]
        print('Word:',' '.join(word_list))

    if lives > 0:
        print(f'Congratulations, You have guessed the word {word} correctly!')
    else:
        print(f"Oops, You have no more lives to continue the game, the word was: {word}")
        
hangman()

