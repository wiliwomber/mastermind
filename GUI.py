from tkinter import *

class LoadingFrame():
    def __init__(self):
        root = Tk()
        #root.aspect(300, 600, 600, 1200)
        # Todo -> resizable window with fixed aspect ratio
        root.minsize(width=300, height=600)
        root.title("Mastermind")


        backgroundFrame = Frame(root, background="#B2B2B2")
        backgroundFrame.pack(expand=1, fill=BOTH)


        label_header = Label(backgroundFrame, text="Mindmaster", bg='BLUE')

        label_header.pack(expand=1, fill=BOTH)

        label_board = Label(backgroundFrame, bg="RED")
        label_board.pack(expand=1, fill=BOTH)

        label_colors = Label(backgroundFrame, bg="Yellow", text="Drag me")
        label_colors.pack(expand=0)

        root.mainloop()

if __name__ == "__main__":
    jo = LoadingFrame()


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
