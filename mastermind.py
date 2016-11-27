#12

#author Gabe & JOJO

def initialize_board():
    board = []
    row = []
    for i in range (0, 11):
        for j in range (0 ,4):
            x = 0
            row.append(x)
        board.append(row)
    print board

initialize_board()
