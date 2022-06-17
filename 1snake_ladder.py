import random
pos1=0 #player1
pos2=0 #player2

ladders={14:32,19:31,5:90,35:48,60:75,38:71}
snakes={91:12,88:22,39:16,77:57}

def move(pos):
    dice=random.randint(1,6)
    print('you have rolled',dice)
    pos+=dice
    if pos in ladders:
        print('found a ladder,lets move up')
        pos=ladders[pos]
    elif pos in snakes:
        print('we got bitten by snake,lets go down')
        pos=snakes[pos]
    print('New position',pos)
    return pos

def start():
    global pos1,pos2
    while True:
        player1=input('player1 turn:\nenter "y" to continue')
        if player1=='y':
            pos1=move(pos1)
            if pos1==100:
                print('player 1 wins')
                break
        player2=input('player2 turn:\nenter "y" to continue')
        if player2=='y':
            pos2=move(pos2)
            if pos2==100:
                print('player 2 wins')
                break 
    if player1 !='y'  or player2 !='y':
        print('\ninvalid input quit the game\n')

if __name__ =='__main__':
    start()       
 


