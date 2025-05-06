import random

def play():
    while True:
        user = input("Make Your Choice!\n'r' for Rock, 'p' for Paper, 's' for Scissor:\n").lower()
        choices = {'r':'rock','p':'paper','s':'scissor'}
        if user not in choices:
            print('Please type in a valid input')
            continue
    
        user = choices[user]
        bot = random.choice(['rock','paper','scissor'])

        if user == bot:
            print(f"It's a tie!\nYour Choice: {user}\nComputer's Choice: {bot}")

        elif is_win(user,bot):
            print(f"Congratulations! You have Won\nYour Choice: {user}\nComputer's Choice: {bot}")

        elif is_win(bot,user):
            print(f"Oops, You lose\nYour Choice: {user}\nComputer's Choice: {bot}\n")

        again=input(f"Press P if you want to play again or Press Q if you want to quit: ").lower()
        if again == 'q':
            print('Thanks For Playing! Yayy!')
            break
        

def is_win(player,opponent):
    #returns True if the player wins
    #rock>scissor,paper>rock,scissor>paper

    if (player=='rock' and opponent=='scissor') or\
    (player=='paper' and opponent=='rock') or\
    (player=='scissor' and opponent=='paper'):
        return True
    
play()


