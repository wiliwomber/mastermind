#author Gabe & JOJO
import time
import random

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
        return color
    elif (color == 'undo' and position > 0):
            board[position-1][(11-row)]= 'blank'
            print_board(board)
            print("%d after blank"%position)
            return 'blank'

    else:
        print ('\x1b[1A\x1b[2K\x1b[1A')
        print ("Not a valid color, try again")
        time.sleep(2)
        print ('\x1b[1A\x1b[2K\x1b[1A')
        return get_color(position, row)

def gen_secretcode():
    print ("This is the secret code")
    secretcode = []
    for position in range (4):
        secretcode.append(colors[random.randint(0,5)]) # picks 4 random values from full color names in  array 'colors'
    print (secretcode)
    return secretcode

def submit():
    #print ('\x1b[1A\x1b[2K\x1b[1A\x1b[1A\x1b[2K\x1b[1A') #delete last two text rows
    submit_input = (input("Do you wanna submit? (Yes / No): ")).lower()
    if submit_input == 'yes':
        return (True)
    elif submit_input == 'no':
        print ('\x1b[1A\x1b[2K\x1b[1A')
        return (False)
    else:
        print ('\x1b[1A\x1b[2K\x1b[1A')
        print ("Please enter yes or no, try again")
        time.sleep(2)
        print ('\x1b[1A\x1b[2K\x1b[1A')
        return submit()



def round(board, scode, position):

    print_board(board)
    while (position < 4):
        if get_color(position, row) != 'blank':
            position +=1
            print_board(board)
        else:
            position -=1
            print_board(board)

        print ("%d after color"%position)
    if not submit():
        set_position(position-1,row,'blank')
        return round (board, scode, 3)



# def guess_vs_secretcode(color):
#    if color in scode:
#        pegpoints=+ 1
#    elif colors(colors.index(color) + 6) in scode:
#        pegpoints=+ 1
#    elif colors(colors.index(color) - 6) in scode:
#        pegpoints=+ 1
#    return pegpoints


#set variable
colors = ["cyan","purple","red","green","blue","yellow","c","p","r","g","b","y"]
#secret solution pattern
#hit list   + (1)  - (0.2)
board = initialize_board()
scode = gen_secretcode()    #secret combination colors
row = 0  #round number -> determins the row which is played in
position = 0 #
round(board, scode, position)


'''
for turn in range(12):
    pegpoints = 0
    for guess in range(4):
        print_board(board)
        get_color(guess,turn)
'''



#initialize_board()
#set_position()
