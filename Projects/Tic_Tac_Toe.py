import random
import time
import sys
n = [j for j in range(1,10)]
board = [" " for i in range(9)]
print("TIC TAC TOE")
def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])
    print(row1)
    print(row2)
    print(row3)
def player_move(icon):
    if icon=="X":
        number = 1
    elif icon=="O":
        number=2
    print("your turn player {}".format(number))
    choice1 = int(input("Enter your move (1-9):").strip())
    if choice1>0 and choice1<=9:
        if board[choice1-1]==" ":
            board[choice1-1]=icon
        else:
            print()
            print("The space was taken..:(")
            print()
            player_move(icon)
    else:
        print("invalid move... please enter again")
        player_move(icon)
def player_movec(icon):
    n1=random.choice(n)
    while board[n1-1] != ' ':
        n1=random.choice(n)
    print("computer turn:")
    time.sleep(0.5)
    print(n1)
    time.sleep(1)
    if board[n1-1] ==" ":
        board[n1-1]=icon
    else:
        print("This space was take....:(")
        print()
        player_movec(icon)
def is_victory(icon):

    if (board[0]==icon and board[1]==icon and board[2]==icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False
while True:
    start_key = input("Enter Y to start or N to quit:").lower()
    if start_key=='y':
        ch = int(input("which mode you want to play \n 1.comuter vs player \n 2.player vs player \n choice:"))
        if ch==1:
            while True:
                print_board()
                player_move("X")
                print_board()
                if is_victory("X"):
                    print("player (X) wins.. congratulations")
                    break
                elif is_draw():
                    print("Its a draw")
                    break
                player_movec("O")
                if is_victory("O"):
                    print_board()
                    print("player (O) wins.... congratulations")
                    break
                elif is_draw():
                    print("Its a draw")
                    break
        elif ch==2:
            while True:
                print_board()
                player_move("X")
                print_board()
                if is_victory("X"):
                    print("player (X) wins.. congratulationsn")
                    break
                elif is_draw():
                    print("Its a draw")
                    break
                player_move("O")
                if is_victory("O"):
                    print_board()
                    print("player (O) wins.... congratulations")
                    break
                elif is_draw():
                    print("Its a draw")
                    break
        else:
            print("Enter again:")
    elif start_key=='n':
        print("Have a nice day.. Bye..")
        exit()
    else:
        print("Enter only valid key")
