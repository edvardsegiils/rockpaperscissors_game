import random
turns = ['rock', 'paper', 'scissors']

while(True):
    human_turn = input('Enter your turn: ')

    computer_turn = random.choice(turns)
    if human_turn == 'exit':
        print('Tnx for paying! BYE BYE')
        break

    print(f'Human:{human_turn} vs. Computer:{computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')

    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Humam wins!')

    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Humam wins!')

    else:
        print('Computer wins!')
