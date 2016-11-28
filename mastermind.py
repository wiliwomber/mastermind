#author Gabe & JOJO


def print_board(board):
    print ("This is the board")
    print ("______________________________") #Top line
    for row in range(12):  #Iterate though each field and print value
        for position in range(4):
            #Everytime fist position is reached print | at the beginning
            if position == 0:
                print ("| ", end="")

            #print the respective color
            if board[0][0] == "white":
                print('  ' + '\x1b[6;30;42m' + '   ' + '\x1b[0m' + '  ', end="")   #end="prevents line break"
            if board[0][0] == "white":
                print('  ' + '\x1b[6;30;42m' + '   ' + '\x1b[0m' + '  ', end="")
            if board[0][0] == "white":
                print('  ' + '\x1b[6;30;42m' + '   ' + '\x1b[0m' + '  ', end="")
            if board[0][0] == "white":
                print('  ' + '\x1b[6;30;42m' + '   ' + '\x1b[0m' + '  ', end="")
            if board[0][0] == "white":
                print('  ' + '\x1b[6;30;42m' + '   ' + '\x1b[0m' + '  ', end="")
            if board[0][0] == "white":
                print('  ' + '\x1b[6;30;42m' + '   ' + '\x1b[0m' + '  ', end="")

            #Everytime last position is reached print | at the end and line break
            if position == 3:
                print (" |")
        print ("______________________________")



def initialize_board():
    board = [ [ "blank" for row in range(12) ] for position in range(4) ] #Access bord field board[position][row]
    return board

def set_position(position,row,color):
    board[position][row]= color



#set variable
colors = ["grey","white","red","green","blue","yellow"]
board = initialize_board()
set_position(0,0,"white")
set_position(3,11,"red")
set_position(3,4,"green")
set_position(0,1,"white")
print_board(board)


#initialize_board()
#set_position()
