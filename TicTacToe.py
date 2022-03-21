import random
import os
import math
board = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
board1 = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
def TicTacToe(Tic):
    print(f"|{Tic[1]}  | {Tic[2]} | {Tic[3]} |")
    print("|---|---|---|")
    print(f"|{Tic[4]}  | {Tic[5]} | {Tic[6]} |")
    print("|---|---|---|")
    print(f"|{Tic[7]}  | {Tic[8]} | {Tic[9]} |")
    print("|---|---|---|")
def Winner(win):
    if win[1] == "O" and win[5] == "O" and win[9] == "O"\
            or win[2] == "O" and win[5] == 'O' and win[8] == "O"\
            or win[3] == "O" and win[5] == 'O' and win[7] == "O"\
            or win[3] == "O" and win[6] == 'O' and win[9] == "O"\
            or win[1] == "O" and win[4] == 'O' and win[7] == "O"\
            or win[1] == "O" and win[2] == 'O' and win[3] == "O"\
            or win[4] == "O" and win[5] == 'O' and win[6] == "O"\
            or win[7] == "O" and win[8] == 'O' and win[9] == "O":
            return "O wins"
    elif win[1] == "X" and win[5] == "X" and win[9] == "X"\
          or win[2] == "X" and win[5] == 'X' and win[8] == "X"\
          or win[3] == "X" and win[5] == 'X' and win[7] == "X"\
          or win[3] == "X" and win[6] == 'X' and win[9] == "X"\
          or win[1] == "X" and win[4] == 'X' and win[7] == "X"\
          or win[1] == "X" and win[2] == 'X' and win[3] == "X"\
          or win[4] == "X" and win[5] == 'X' and win[6] == "X"\
          or win[7] == "X" and win[8] == 'X' and win[9] == "X":
          return "X Wins"
    else:
        return False
def play():
    print("Leader Board")
    TicTacToe(board1)
    print()
    computer_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    j=1
    text = "X"
    while j!=10:
        i = Winner(board)
        TicTacToe(board)
        if i:
            break
        print()
        if text=="X":
            num = int(input("now it is {}: ".format(text)))
            if (num) in board:
                if not board[(num)] == "O" and board[(num)] != "X":
                    board[(num)] = text
                    computer_nums.remove(num)
                    j+=1
                    
                else:
                    print('Already Clicked!', num)
                    if text == "O":
                        text = "X"
                    else:
                        text = 'O'
            else:
                print('Number should be 1 up to 9')
                if text == "O":
                    text = "X"
                else:
                    text = 'O'
        else:
            comp=random.choice(computer_nums)
            if comp in board:
                if not board[comp] == "O" and board[comp] != "X":
                    board[comp] = text
                    j+=1
                    computer_nums.remove(comp)
            
        if text =="X":
            text="O"
        else:
            text="X"
def main():
    play()
    if Winner(board):
        print(Winner(board))
    else:
        print("It is Tie!")
    TicTacToe(board)
while 1:
    main()
    pl = input("Do you want to paly again? ")
    if pl == "yes":
        os.system("cls")
        for i in range(1,10):
            board[i]=" "
        main()
        
    else:break

