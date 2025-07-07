board = ['1','2','3','4','5','6','7','8','9']
global win
win = 0


def print_board():
    print("current board:")
    for i in range(1,10):
        print("",board[i-1],end="|")
        if (i % 3 == 0):
            print("\n",end="")


print_board()
# player one movement
def player_one_move():
    move = int(input("player x enter move"))
    if board[move-1]=='X' or board[move-1]=='O':
        print("error!!!!")
        player_one_move()
    else:
        board[move - 1]='X'

# player two movement
def player_two_move():
    move = int(input("player O enter move"))
    if board[move-1]=='X' or board[move-1]=='O':
        print("error!!!!")
        player_two_move()
    else:
        board[move - 1]='O'


# check win
def check_win():
    global win
    for i in range(0,9,3):
      if  board[i]=='X' and board[i+1]=='X' and board[i+2]=='X':
            print(i)
            print("player one win")
            win = 1
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == 'O':
            print(i)
            print("player two win")
            win = 1
    for i in range(0, 3,):
        if board[i] == 'X' and board[i + 3] == 'X' and board[i + 6] == 'X':
            print("player one win")
            win = 1
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] == 'O':
            print("player two win")
            win = 1
    if board[0]==board[4]==board[8]=='X':
        print("player one win")
        win = 1
    if board[2]==board[4]==board[6]=='X':
        print("player one win")
        win = 1
    if board[0] == board[4] == board[8] == 'O':
        print("player two win")
        win = 1
    if board[2] == board[4] == board[6] == 'O':
        print("player two win")
        win = 1


# runner
while win==0:
    player_one_move()
    print_board()
    check_win()
    if win == 1:
        break
    player_two_move()
    print_board()
    check_win()
    if win == 1:
        break

    # print(win)
