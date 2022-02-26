import re
import ast
from pynput import keyboard
import time
import numpy as np

previous = 0
UserIn = 0
position_R = 0                          #position in array - Rows
position_C = 0                          #position in array - Collumns

running = True
poprzedni = 0

#dictionary
#messy naming of paths caused by many changes in the way I attempted to adress these strings in further parts of code
#might clean it up sometime

path10 = "\nIf you have problems with hardware, press 1.\n"\
         "If your inputed mathematical formula doesn't work, press 2.\n"\
         "If you would like to read more about additional features, press 3.\n"
path110 = "\nIf your keyboard doesn't work, press 1.\nIf your monitor doesn't work, press 2.\nIf your mouse doesn't work, press 3.\n"
path120 = "\nLiar\n"
path210 = path120
path111 = path120
path20 = "\nTry restarting program, and check if your formula is correct for python's eval.\n"
path11 = "\nYou can use plus/minus as the word in your formula :D\n" \
         "try typing dupa or Iba\n"

#linking dictionary to array-type-thigy
array = np.array(([path10, 0, 0],
         [path110, path20, path11],
         [path210, path120], path111), dtype='object')

def zero_error():
    print("Dont divide by 0!")

def myeval1(s):
    try:
        return eval(s)
    except ZeroDivisionError:
        zero_error()
        return 0

def myeval2(w, p):
    try:
        return eval(str(p) + w)
    except ZeroDivisionError:
        zero_error()
        return 0

def help_panel():
    global position_C
    global position_R
    global previous

    previous = 0

    print("\n**************************************************************")
    print(array[position_R][position_C])
    print("**************************************************************")

    if position_R == 2:
        return
    elif position_R == 1 and position_C == 1:
        return
    elif position_R == 1 and position_C == 2:
        return

    path_selector()

def path_selector():
    global position_R
    global position_C
    finished = False

    while not finished:
        with keyboard.Events() as events:
            event = events.get(1e6)


            if event.key == keyboard.KeyCode.from_char('1'):
                finished = True
                position_R = position_R + 1
                time.sleep(1)
                help_panel()

            if event.key == keyboard.KeyCode.from_char('2'):
                finished = True
                position_R = position_R + 1
                position_C = 1
                time.sleep(1)
                help_panel()

            if event.key == keyboard.KeyCode.from_char('3'):
                finished = True
                position_R = position_R + 1
                position_C = 2
                time.sleep(1)
                help_panel()


def UserInput(previous):
    global position_R
    global position_C
    global UserIn
    global poprzedni

    position_C = 0
    position_R = 0

    if previous == 0:
        UserIn = input("Type your calculations [type !help to access help panel, or type quit, to close script]")
    else:
        UserIn = input(str(poprzedni))

    return UserIn

def ASCII_dupa():                    #ASCII art dupy

    print("⠄⠄⠸⣿⣿⢣⢶⣟⣿⣖⣿⣷⣻⣮⡿⣽⣿⣻⣖⣶⣤⣭⡉⠄⠄⠄⠄⠄\n"
          "⠄⠄⠄⢹⠣⣛⣣⣭⣭⣭⣁⡛⠻⢽⣿⣿⣿⣿⢻⣿⣿⣿⣽⡧⡄⠄⠄⠄\n"
          "⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣽⢘⣿⣷⣿⡻⠏⣛⣀⠄⠄\n"
          "⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⡅⣿⠚⣡⣴⣿⣿⣿⡆⠄\n"
          "⠄⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⣱⣾⣿⣿⣿⣿⣿⣿⠄\n"
          "⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⠄\n"
          "⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄\n"
          "⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠑⣿⣮⣝⣛⠿⠿⣿⣿⣿⣿⠄\n"
          "⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄\n"
          "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄\n"
          "⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⡿⢟⣣⣀")

def ASCII_iba():                       #ASCII art Iby

    print("                     , \n"
          "                ,.  | \ \n"
          "               |: \ ; :\ \n"
          "               :' ;\| ::\ \n"
          "                \ : | `::\ \n"
          "                _)  |   `:`.\n"
          "              ,' , `.    ;: ;\n"
          "            ,' ;:  ; '  ,:: |_ \n"
          "           /,   ` .    ;::: |:`-.__ \n"
          "        _,' _o\  ,::.`:' ;  ;   . ' \n"
          "    _,-'           `:.          ;""\, \n"
          " ,-'                     ,:         `-;, \n"
          " \,                       ;:           ;--._ \n"
          "  `.______,-,----._     ,' ;:        ,/ ,  ,` \n"
          "         / /,-';'  \     ; `:      ,'/,::.::: \n"
          "       ,',;-'-'_,--;    ;   :.   ,',',;:::::: \n"
          "      ( /___,-'     `.     ;::,,'o/  ,::::::: \n"
          "       `'             )    ;:,'o /  ; -   -:: \n"
          "                      \__ _,'o ,'         ,:: \n"
          "                         ) `--'       ,..:::: \n"
          "                         ; `.        ,::::::: \n"
          "                          ;  ``::.    :::::::")

def filter(previous, UserIn):

    UserIn = re.sub('plus', '+', UserIn)
    UserIn = re.sub('minus', '-', UserIn)
    UserIn = re.sub('[a-zA-Z=:" "]', '', UserIn)  # filter symbols, that could be used to harm our computer through eval()

    calc(previous, UserIn)

def calc(previous, UserIn):
    global poprzedni

    if previous == 0:
        poprzedni = (myeval1(UserIn))
    else:
        poprzedni = (myeval2(UserIn, previous))

    return(poprzedni)

def response(previous, UserIn):
    global running

    if UserIn == 'quit' or UserIn == 'Quit' or UserIn == 'QUIT':
        running = False

    elif UserIn == 'Iba':
        ASCII_iba()

    elif UserIn == 'Dupa' or UserIn == 'dupa':
        ASCII_dupa()

    elif UserIn == '!help':
        help_panel()

    else:
        filter(previous, UserIn)

    return running

def main():
    global running
    global previous
    global position_R
    global position_C

    response(previous, UserInput(previous))
    previous = poprzedni

if __name__ == "__main__":
    while running:
        main()
