# 全局常量
best_weizhi = (7, 8, 2, 6, 8, 1, 3, 5, 4)
win = ((0, 1, 2), (4, 5, 6), (8, 9, 10), (0, 4, 8), (1, 5, 9), (2, 6, 10), (0, 5, 10), (2, 5, 8), (4, 8, 12))
X = "x"
O = "o"
EMPTY = " "


# 定义函数产生一个新的棋盘
def new_board():
    board = []
    for square in range(16):
        board.append(EMPTY)
    return board


# 询问该谁下棋
def ask_yes_no(question):
    response = None
    # 如果输入不是"y", "n"，继续重新输入
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


# 询问谁先走，先走方为X，后走方为O
# 函数返回电脑方、玩家的角色代号
def pieces():
    go_first = ask_yes_no("你是否先走 (y/n): ")
    if go_first == "y":
        print("\n玩家你先走.")
        human = X
        computer = O
    else:
        print("\n电脑先走.")
        computer = X
        human = O
    return computer, human


# 显示棋盘
def display_board(board):
    board2 = board[:]  # 创建副本，修改不影响原来列表board
    for i in range(len(board)):
        if board[i] == EMPTY:
            board2[i] = i
    print("\t", board2[0], "|", board2[1], "|", board2[2], "|", board2[3],)
    print("\t", "-----------------")
    print("\t", board2[4], "|", board2[5], "|", board2[6], "|", board2[7])
    print("\t", "-----------------")
    print("\t", board2[8], "|", board2[9], "|", board2[10],  "|", board2[11])
    print("\t", "-----------------")
    print("\t", board2[8 + 4], "|", board2[9 + 4], "|", board2[10 + 4],  "|", board2[11 + 4])



# 输入你想下的位置数字
def ask_number(question, low, high):
    response = None
    while response not in range(0, 16):
        response = int(input(question))
    return response


# 产生可以合法走棋位置序列（也就是还未下过子位置）
def legal_moves(board):
    moves = []
    for i in range(16):
        if board[i] == EMPTY:
            moves.append(i)
    return moves


# 判断输赢
def winner(board):
    for row in win:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner  # 返回赢方
    # 棋盘没有空位置
    if EMPTY not in board:
        return "True"  # "平局和棋，游戏结束"
    return False


# 人走棋
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("你走那个位置? (0 - 9):", 0, 9)
        if move not in legal:
            print("\n此位置已经落过子了")
    return move


# 电脑走棋
def computer_move(board, computer, human):
    # make a copy to work with since function will be changing list
    board = board[:]  # 创建副本，修改不影响原来列表board
    # 按优劣顺序排序的下棋位置best_weizhi
    # 如果电脑能赢，就走那个位置
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print("电脑下棋位置是", move)
            return move
        # 取消走棋方案
        board[move] = EMPTY
    # 如果玩家能赢，就堵住那个位置
    # 不是上面情况则，也就是这一轮时都赢不了则
    # 从最佳下棋位置表中挑出第一个合法位置
    for move in best_weizhi:
        if move in legal_moves(board):
            print("电脑下棋位置是", move)
            return move


# 转换角色
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


# 主方法：
def main():
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        the_winner = winner(board)
    if the_winner == computer:
        print("真是不好意思，电脑赢!\n")
    elif the_winner == human:
        print("恭喜，您赢了!\n")
    elif the_winner == "True":  # "平局"
        print("平局,和棋，游戏结束\n")

main()
input("按任意键退出游戏.")