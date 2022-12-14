#Fyra i rad
def printboard(board):
    for row in board:
        print(*row)

    print()

rows = 4
cols = 6
board =[["-" for _ in range(cols)]for _ in range(rows)]
printboard(board)



board[row][col]  = "X"

printboard(board) 