import random

def RPS():
    choices = ['rock', 'paper', 'scissors']
    win_condition = {'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'}
    lose_condition = {'rock' : 'paper', 'paper' : 'scissors', 'scissors' : 'rock'}
    
    computer_choice, player_choice = None, None
    round = 0
    player_rounds_won = 0
    computer_rounds_won = 0
    
    while round < 3:
        computer_choice = random.choice(choices)
        player_choice = input('Rock, paper or scissors: ').lower()
        while player_choice not in choices:
            player_choice = input('Rock, paper or scissors: ').lower()
        print(f'Computer has chosen {computer_choice}.')
        round += 1
        if computer_choice == win_condition[player_choice]:
            print('You have won this round.\n')
            player_rounds_won += 1
        elif computer_choice == lose_condition[player_choice]:
            print('You have lost this round.\n')
            computer_rounds_won += 1
        else:
            print('You have drawn with the computer.\n')
    
    print(f'Player: {player_rounds_won}, Computer: {computer_rounds_won}')
    
    if player_rounds_won > computer_rounds_won:
        print('Congratulations, you have won this set.')
    elif computer_rounds_won > player_rounds_won:
        print('You have lost this set.')
    else:
        print('You have drawn with the computer.')

if __name__ == "__main__":
    RPS()
