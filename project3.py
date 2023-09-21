# #ROCK PAPER SCISSOR

import random

def play():
    user = input("Choose : \n 'r' for rock \n 'p' for paper \n 's' for scissor : ")
    computer = random.choice(['r','p','s'])
    print(f"computer chooses: {computer}")
    
    if user == computer:
        return 'It\'s a tie'
    
    if win(user,computer):
        return " YOU WON"
    
    return "You lost"
    
def win(player,computer):
    if(player=='r' and computer == 's') or (player == 's' and computer == 'p') or (player== 'p' and computer=='r'):
        return True

# n=int(input("HOW MANY TIMES YOU WANT TO PLAY: "))
# for i in range(0,n):

print(play())
