#author Gabe & JOJO
import time

def print_board(board):
    print ("This is the board")
    print ("______________________________") #Top line
    for row in range(12):  #Iterate though each field and print value
        for position in range(4):
            #Everytime fist position is reached print | at the beginning
            if position == 0:
                print ("| ", end="")

            #print the respective color
            if board[position][row] == "blank":
                print('       ', end="")
            if board[position][row] == "cyan":
                print('  ' + '\x1b[6;30;46m' + '   ' + '\x1b[0m' + '  ', end="")   #end="prevents line break"
            if board[position][row] == "purple":
                print('  ' + '\x1b[0;31;45m' + '   ' + '\x1b[0m' + '  ', end="")
            if board[position][row] == "red":
                print('  ' + '\x1b[6;30;41m' + '   ' + '\x1b[0m' + '  ', end="")
            if board[position][row] == "green":
                print('  ' + '\x1b[6;30;42m' + '   ' + '\x1b[0m' + '  ', end="")
            if board[position][row] == "blue":
                print('  ' + '\x1b[6;30;44m' + '   ' + '\x1b[0m' + '  ', end="")
            if board[position][row] == "yellow":
                print('  ' + '\x1b[6;30;43m' + '   ' + '\x1b[0m' + '  ', end="")

            #Everytime last position is reached print | at the end and line break
            if position == 3:
                print (" |")
        print ("______________________________")



def initialize_board():
    board = [ [ "blank" for row in range(12) ] for position in range(4) ] #Access bord field board[position][row]
    return board

def set_position(position,row,color):
    board[position][(11-row)]= color #11-row to set start printing at the bottom of the board

def get_color(position, row):
    color = (input('Enter color: ')).lower()
    if color in colors: #check if input is a valid color
        if colors.index(color)>5:
            color = colors[(colors.index(color)-6)]
        board[position][(11-row)]= color #11-row to set start printing at the bottom of the board
        return True
    else:
        print ('\x1b[1A\x1b[2K\x1b[1A')
        print ("Not a valid color, try again")
        time.sleep(2)
        print ('\x1b[1A\x1b[2K\x1b[1A')
        return get_color(position, row)

#set variable
colors = ["cyan","purple","red","green","blue","yellow","c","p","r","g","b","y"]
#secret solution pattern
#hit list   + (1)  - (0.2)
board = initialize_board()



#initialize_board()
#set_position()
