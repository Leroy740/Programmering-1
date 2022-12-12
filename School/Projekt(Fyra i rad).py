#Fyra i rad
def printboard(board):
    for row in board:
        print(*row)

        print()

rows = 3
cols = 8
board =[["-" for _ in range(cols)]for _ in range(rows)]
printboard(board)

board[2][2] = "X"

printboard(board) 