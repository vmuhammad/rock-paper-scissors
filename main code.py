import random
#rock paper scissors
print ('hi for starting game, choose rock, paper, scissors')
game=['rock', 'paper','scissors']
n= input('choose rock, paper, scissors: ')
b = random.choice(game)
print('computer says: ' , b)
if b==n:
    print ('try again')
elif n=='rock':
    if b=='scissors':
        print('you are a winner')
    else:
        print('you lose')
        
elif n=='paper':
    if b=='rock':
        print('you are a winner')
    else:
        print('you lose')
elif n== 'scissors':
    if b== 'paper':
        print('you are a winner')
    else:
        print('you lose')
                        
    
