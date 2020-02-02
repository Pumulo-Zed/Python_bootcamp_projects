# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:14:06 2020

@author: Pumulo
"""

print( 'Welcome to tic-tac-toe.')
print('      by Pumulo Chotela')
print('\n') 
print('\n')  
a='   PS1  |  PS2 | PS3 '
b='   PS4  |  PS5 | PS6 '
c='   PS7  |  PS8 | PS9 ' 
mark='None'
winning_combs=set([a[4]+a[12]+a[18],b[4]+b[12]+b[18],c[4]+c[12]+c[18],a[4]+b[4]+c[4],a[12]+b[12]+c[12],a[18]+b[18]+c[18],a[4]+b[12]+c[18],a[18]+b[12]+c[4]])

name_1=''
name_2=''
print('\n')
def player_assigment():
    ''' given the names of the players,player_assignment() assigns who player one and two is randomly'''
    global player_one
    global player_two
    import random
    b=[name_1,name_2]
    player_one=random.choice(b)
    player_two=[item for item in b if item!=player_one][0]
    print(f'player one is {player_one} and player two is {player_two}')


 
track=[]
def board():
    ''' creats the tick-tack-toe board '''
    print('        |      |       ')
    print(a)
    print('-----------------------')
    print('        |      |       ')
    print(b)
    print('-----------------------')
    print(c)
    print('        |      |       ')

def fill_position(token,position):
    ''' takes in a token, either X or O, and the position where that token is to be placed as inputs and adjusts the tic-tack to board by placing the token in the osition entered'''
    global a
    global b
    global c
    if position in a:
        a=a.replace(position,' '+token+' ')
    elif position in b:
        b=b.replace(position,' '+token+' ')
    else:
        c=c.replace(position,' '+token+' ')
        
def make_move():
    global track
    global winning_combs
    global mark
    if len(track)==0 or track[-1]==2:
        position=input(f'{player_one} select position to place token:').upper()
        if len(position)==3 and position in a+b+c:
            track.append(1)
            fill_position('X',position)
            mark='X'
        else:
             print('invalid position entered')
             print('\n')
             make_move()
    else:
        position=input(f'{player_two} select position to place token:').upper()
        if len(position)==3 and position in a+b+c:
            track.append(2)
            fill_position('O',position)
            mark='O'
        else:
             print('invalid position entered')
             print('\n')
             make_move()
    winning_combs=set([a[4]+a[12]+a[18],b[4]+b[12]+b[18],c[4]+c[12]+c[18],a[4]+b[4]+c[4],a[12]+b[12]+c[12],a[18]+b[18]+c[18],a[4]+b[12]+c[18],a[18]+b[12]+c[4]])
    
    
def check_for_winner():
    ''' checks for a winner and returns the name of the winner'''
    if mark*3 in winning_combs:
        if mark=='X':
            return f'{player_one} wins'
        else:
            return f'{player_two} wins'
    else:
        pass
    
def reset_board_and_track():
    ''' resets the board and track to their original state i.e when no one had made a move'''
    global a
    global b
    global c
    global track
    a='   PS1  |  PS2 | PS3 '
    b='   PS4  |  PS5 | PS6 '
    c='   PS7  |  PS8 | PS9 '
    track=[]
    
def game_play():
    while len(track)<9:
        board()
        print('\n')
        make_move()
        print('\n')
    
        if check_for_winner()==f'{player_one} wins' or check_for_winner()==f'{player_two} wins':
            board()
            print('\n')
            print(check_for_winner())
            print('\n')
            rematch=input('would you like a rematch (yes or no):').lower()
            print('\n')
            if rematch.lower()=='yes':
                reset_board_and_track()
                winning_combs=set([a[4]+a[12]+a[18],b[4]+b[12]+b[18],c[4]+c[12]+c[18],a[4]+b[4]+c[4],a[12]+b[12]+c[12],a[18]+b[18]+c[18],a[4]+b[12]+c[18],a[18]+b[12]+c[4]])
                player_assigment()
                print('\n')
            else:
                reset_board_and_track()
                winning_combs=set([a[4]+a[12]+a[18],b[4]+b[12]+b[18],c[4]+c[12]+c[18],a[4]+b[4]+c[4],a[12]+b[12]+c[12],a[18]+b[18]+c[18],a[4]+b[12]+c[18],a[18]+b[12]+c[4]])
                print('THANK YOU FOR PLAYING :-)')
                break
        else:
            pass
    if len(track)==9:
        board()
        print('\n')
        print('ITS A DRAW')
        rematch=input('would you like a rematch (yes or no):').lower()
        print('\n')
        if rematch.lower()=='yes':
            reset_board_and_track()
            winning_combs=set([a[4]+a[12]+a[18],b[4]+b[12]+b[18],c[4]+c[12]+c[18],a[4]+b[4]+c[4],a[12]+b[12]+c[12],a[18]+b[18]+c[18],a[4]+b[12]+c[18],a[18]+b[12]+c[4]])
            player_assigment()
            print('\n')
            game_play()
        else:
            reset_board_and_track()
            winning_combs=set([a[4]+a[12]+a[18],b[4]+b[12]+b[18],c[4]+c[12]+c[18],a[4]+b[4]+c[4],a[12]+b[12]+c[12],a[18]+b[18]+c[18],a[4]+b[12]+c[18],a[18]+b[12]+c[4]])
            print('THANK YOU FOR PLAYING :-)')
    else:
        pass
        
  #actual game code
name_1=input('enter name here:')
name_2=input('enter name here:')
print('\n')
player_assigment()
print('\n')
game_play()
print('\n')
input('Press Enter To Close')
        