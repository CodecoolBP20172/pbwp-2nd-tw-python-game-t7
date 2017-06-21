from tkinter import *
from PIL import *
import time
import random
from tkinter import font


# One extra variable needed to handle phase
# TODO: Deduct board2 from prep_changer arguments
#       Paste the necessary arguments of prep_changer into the key bindings.
#       Starter doesn't need look == 2

def changer(x):
    global phase
    global board1
    global board2
    global hp1
    global hp2
    global hitlist1
    global hitlist2

    if phase == 2:
        hit = shot(x, board2)
        if hit == 1 and x not in hitlist1:
            hitlist1.append(x)
            hp2 = hp2 - hit
        board2 = board_changer(x, board2)
        tile_number_1 = board_value(x, board2)
        print(str(tile_number_1))
        ai[x].configure(image=imgs[tile_number_1])

        FUNCTION2 = random.randint(0, 99)
        hit = shot(FUNCTION2, board1)
        if hit == 1 and FUNCTION2 not in hitlist2:
            hitlist2.append(FUNCTION2)
            hp1 = hp1 - hit
        board1 = board_changer(FUNCTION2, board1)
        tile_number_2 = board_value(FUNCTION2, board1)
        print(str(tile_number_2))
        user[FUNCTION2].configure(image=imgs[tile_number_2])
        if hp1 == 0 or hp2 == 0:
            if hp1 == 0:
                print("AI won\n")
            if hp2 == 0:
                print("PLayer 1 won\n")
            sys.exit()


# Displays the all the ship at creation
def starter(ships1, ship_counter, pos=45, look=1):
    try:
        length = ships1[ship_counter]  # the ship's length
        print("Setting up a start")
        i = 0
        while i < length:
            if look == 1:
                user[pos + (i * 10)].configure(image=imgs[2])
            if look == 2:
                user[pos + (i)].configure(image=imgs[2])
            i += 1
    except IndexError:
        print("No more ships but no worry the game will start now\n")


def prep_changer(key):
    global phase
    global board1
    global board2
    global ship_handle
    global ships1
    global ships2
    global ship_counter
    global pos
    global look
    global length
    print("ship list length " + str(len(ships1)))
    print("phase "+str(phase))

    turn = 0  # 0=no actions this turn yet. 1=somthing already happened

    length = ships1[ship_counter]  # the ship's length
    # look = 1 #the ship's direction
    # pos = pos #the ship's posiion
    print("ship counter " + str(ship_counter))

    command = ship_handle[key]
    print("pos "+str(pos))
    print("look "+str(look))
    print("legth "+str(length)+"\n")

    if phase == 0 and ship_counter < len(ships1):
        if command == ship_handle[0] and turn == 0:  # w moves up
            if not pos_checker(pos, length, look, board1, command) == 1:
                for i in range(length):
                    if look == 1:
                        user[pos + (i * 10)].configure(image=imgs[0])
                    if look == 2:
                        user[pos + (i)].configure(image=imgs[0])
                pos -= 10
                turn = 1
                if ship_pos_validator(pos, length, look, board1) == 0:
                    for i in range(length):

                        if look == 1:
                            user[pos + (i * 10)].configure(image=imgs[2])
                        if look == 2:
                            user[pos + (i)].configure(image=imgs[2])

        elif command == ship_handle[1] and turn == 0:  # a moves left
            if not pos_checker(pos, length, look, board1, command) == 1:
                for i in range(length):
                    if look == 1:
                        user[pos + (i * 10)].configure(image=imgs[0])
                    if look == 2:
                        user[pos + (i)].configure(image=imgs[0])
                pos -= 1
                turn = 1
                if ship_pos_validator(pos, length, look, board1) == 0:
                    for i in range(length):
                        if look == 1:
                            user[pos + (i * 10)].configure(image=imgs[2])
                        if look == 2:
                            user[pos + (i)].configure(image=imgs[2])

        elif command == ship_handle[2] and turn == 0:  # s moves down
            if not pos_checker(pos, length, look, board1, command) == 1:
                for i in range(length):
                    if look == 1:
                        user[pos + (i * 10)].configure(image=imgs[0])
                    if look == 2:
                        user[pos + (i)].configure(image=imgs[0])
                pos += 10
                turn = 1
                if ship_pos_validator(pos, length, look, board1) == 0:
                    for i in range(length):
                        if look == 1:
                            user[pos + (i * 10)].configure(image=imgs[2])
                        if look == 2:
                            user[pos + (i)].configure(image=imgs[2])

        elif command == ship_handle[3] and turn == 0:  # d mves right
            if not pos_checker(pos, length, look, board1, command) == 1:
                for i in range(length):
                    if look == 1:
                        user[pos + (i * 10)].configure(image=imgs[0])
                    if look == 2:
                        user[pos + (i)].configure(image=imgs[0])
                pos += 1
                turn = 1
                if ship_pos_validator(pos, length, look, board1) == 0:
                    for i in range(length):
                        if look == 1:
                            user[pos + (i * 10)].configure(image=imgs[2])
                        if look == 2:
                            user[pos + (i)].configure(image=imgs[2])

        elif command == ship_handle[4] and look == 1 and turn == 0:  # f changes direction
            if not pos_checker(pos, length, look, board1, command) == 1:
                for i in range(length):
                    if look == 1:
                        user[pos + (i * 10)].configure(image=imgs[0])
                    if look == 2:
                        user[pos + (i)].configure(image=imgs[0])
                look = 2
                turn = 1
                if ship_pos_validator(pos, length, look, board1) == 0:
                    for i in range(length):

                        if look == 1:
                            user[pos + (i * 10)].configure(image=imgs[2])
                        if look == 2:
                            user[pos + (i)].configure(image=imgs[2])

        elif command == ship_handle[4] and look == 2 and turn == 0:
            if not pos_checker(pos, length, look, board1, command) == 1:
                for i in range(length):
                    user[pos + (i * 1)].configure(image=imgs[0])
                look = 1
                turn = 1
                if ship_pos_validator(pos, length, look, board1) == 0:
                    for i in range(length):
                        if look == 1:
                            user[pos + (i * 10)].configure(image=imgs[2])
                        if look == 2:
                            user[pos + (i * 1)].configure(image=imgs[2])

        elif command == ship_handle[5] and turn == 0:  # g puts the ship down
            if ship_pos_validator(pos, length, look, board1) == 0:
                board1 = put_ship_down(pos, length, look, board1)
                turn = 1
                for i in range(length):
                    if look == 1:
                        user[pos + (i * 10)].configure(image=imgs[2])
                    if look == 2:
                        user[pos + (i)].configure(image=imgs[2])
            print(board1)
            look = 1
            pos = 45
            ship_counter += 1
            starter(ships1, ship_counter)
    if ship_counter == len(ships1):
        phase = 1
        ship_counter = 0
    if phase == 1:
        phase = prep_phase_AI(ship_handle, ships2, board2, 0)
        print(board2)
    print("\n")
# click eventhandler to change pics on user and ai buttons | z, w változó
# (user és AI képe), x, y változó (ai kép sorszáma)


# prep phase
# phase = 0
# 0 = prep phase
# 1 = ai prep phase
# 2 = battle phase
# hp1 = 3 #predetermined
# hp2 = 3
# board2 = [0]*100 # from 0-99 a 100 tiles
# board values:
# 0 - nothing
# 1 - ship
# 2 - ship that got a hit
# 4 - missed shot
# 0th square on both boards is ignored
# a-0, b-1, c-2, d-3, e-4, f-5, g-6, h-7, i-8, j-9
# putting down the ships
# ships1 = [2, 2, 2, 2, 3, 3, 3, 4, 4, 5] #10 ships in total
# ships1 = [2, 3, 4]
# ship value means how long the ship is.
# If it's 0 the ship is put down on the board and we move on to the next ship.
def pos_checker(pos, length, look, board, command):
    # returns 0 if new pos is ok
    # returns 1 if new pos is bad
    new_pos = pos
    new_pos -= 10
    if command == "w" and new_pos < 0:
        # since we step 10 in both vertical look
        # if we step out from the game board we allways
        # reduce our pos number uner 0
        # s similar but we always go over 99

        print("You would step out of the gameboard!")
        return 1
    if command == "w":
        if look == 2:
            for i in range(length):
                if board[new_pos+i] == 1:
                    print("You'd step on another ship")
                    return 1
        elif look == 1 and board[new_pos] == 1:
            print("You'd step on another ship")
            return 1
    new_pos = pos
    new_pos -= 1
    new_pos = new_pos % 10
    if command == "a" and new_pos == 9:
        # when we step to the right and we would step off the board we would
        # allways reach a number that ends with 9
        # d is similar but the number ends with 0
        print("You would step out of the gameboard!")
        return 1
    new_pos = pos
    new_pos -= 1
    if command == "a":
        if look == 1:
            for i in range(length):
                if board[new_pos+i*10] == 1:
                    return 1
        if look == 2:
                if board[new_pos] == 1:
                    return 1
    new_pos = pos
    new_pos = new_pos+10
    if command == "s" and new_pos > 99:
        print("You would step out of the gameboard!")
        return 1
    new_pos = pos
    if command == "s":
        if look == 2:
            for i in range(length):
                if board[new_pos+10+i] == 1:
                    print("You'd step on another ship")
                    return 1
        elif look == 1:
            if new_pos+length*10 < 99:
                if board[new_pos+(length*10)] == 1:
                    print("You'd step on another ship")
                    return 1

    new_pos = pos
    new_pos = new_pos + (length * 10)
    if command == "s" and look == 1:
        if new_pos > 99:
            print("You would step out of the gameboard!")
            return 1
    new_pos = pos
    new_pos += 1
    new_pos = new_pos % 10
    if command == "d" and new_pos == 0:
        print("You would step out of the gameboard!")
        return 1
    new_pos = pos
    new_pos += 1
    if command == "d":
        if look == 1:
            for i in range(length):
                if board[new_pos+i*10] == 1:
                    return 1
        if look == 2:
            for i in range(length):
                if board[new_pos+i] == 1:
                    return 1
    new_pos = pos
    new_pos += (length * 1)
    new_pos = new_pos % 10
    if command == "d" and look == 2:
        if new_pos == 0:
            print("You would step out of the gameboard!")
            return 1

    new_pos = pos
    if command == "f" and look == 1:
        for i in range(length):
            new_pos = pos + i
            new_pos = new_pos % 10
            if i != 0:
                if new_pos == 0:
                    print ("You would step out of the gameboard!")
                    return 1
    new_pos = pos
    i = 0
    if command == "f" and look == 2:
        while i < length:
            new_pos = new_pos + 10
            if new_pos > 99:
                print ("You would step out of the gameboard!")
                return 1
            i += 1
    return 0


def ship_pos_validator(pos, length, look, board):
    # validates if the ship can be put down at it's position
    # returns with 0 if the location is valid
    # returns with 1 if the location is not valid
    # variable to check if it is possible to put the ship down
    for i in range(length):
        if look == 1:
            try:
                if board[pos + (i * 10)] != 0:
                    print("You can't put that ship there")
                    return 1
            except IndexError:
                print("You can't put that ship there")
                return 1
        elif look == 2:
            try:
                if board[pos + i] != 0:
                    print("You can't put that ship there")
                    return 1
            except IndexError:
                print("You can't put that ship there")
                return 1
    return 0


def pick_ship_up(pos, length, look, board):
    i = 0
    if look == 1:
        while i < length:
            board[pos + (i * 10)] = 0
            i += 1
    if look == 2:
        while i < length:
            board[pos + i] = 0
            i += 1
    return board


def put_ship_down(pos, length, look, board):
    i = 0
    while i < length:
        if look == 1:
            board[pos + (i * 10)] = 1
        if look == 2:
            board[pos + i] = 1
        i += 1
    return board


# the AI's prep_phase
def prep_phase_AI(ship_handle, ships, board, ship_counter=0):
    print("AIs turn to prepare")
    print("ship list length " + str(len(ships)))

    pos = 45  # or e5
    direction = 1  # 1 is down, 2 is right

    while ship_counter < len(ships):
        cur_ship = [0, 0, 0]  # the ship we want to put down
        cur_ship[0] = ships1[ship_counter]  # the ship's length
        cur_ship[1] = random.randint(1, 2)  # the ship's direction RANDOM
        cur_ship[2] = random.randint(0, 99)  # the ship's position RANDOM
        print("ship length " + str(cur_ship[0]))
        print("ship dir " + str(cur_ship[1]))
        print("ship pos " + str(cur_ship[2]))
        print("ship counter " + str(ship_counter))

        if ship_pos_validator(cur_ship[2], cur_ship[0], cur_ship[1], board) == 0:
            board = put_ship_down(cur_ship[2], cur_ship[0], cur_ship[1], board)
            ship_counter += 1
    print("ships down " + str(ship_counter))
    print("returning to phase 2")
    return 2


def hit_searcher(hitmarker):
    # returns with 1 if there was a hit inthe last 4 shoots
    # returns with 0 if there was no hit in th last 4 shoots
    i = 0
    counter = len(hitmarker) - 1
    for i in range(counter):
        if hitmarker[i] == 1:
            return 1
    return 0


def hit_hystory(hitmarker):
    # returns with the number of turns between the current turn and the turn
    # with the last successfull hit
    # if returns 6 then there was a problem
    i = 0
    counter = len(hitmarker) - 1
    for i in range(counter):
        if hitmarker[i] == 2:
            return i
    return 6


def AI_shot_pos_checker(pos, hit_hystory):
    new_pos = pos
    new_pos -= 10
    if hit_hystory == 1 and new_pos < 0:
        return 1
    new_pos = pos
    new_pos -= 1
    new_pos = new_pos % 10
    if hit_hystory == 2 and new_pos == 9:
        return 1
    new_pos = pos
    new_pos = new_pos + 10
    if hit_hystory == 3 and new_pos > 99:
        return 1
    new_pos = pos
    new_pos += 1
    new_pos = new_pos % 10
    if hit_hystory == 4 and new_pos == 0:
        return 1
    return 0


def AI_shot(hitmarker, hit_loc, board):  # returns with the AI-s shot coordinate
    torpedo = 0
    if not hit_searcher(hitmarker) == 1:
        torpedo = random.randint(0, 99)
        return torpedo
    elif hit_hystory == 6:
        print("there is a problem as hit hystory returned 6")
    elif hit_hystory == 0:
        print("ther is a problem as hithistory returned 0")
    elif hit_hystory == 1:
        torpedo = hit_loc + 10


def shot(shot, board):
    # returns with 0 if the shot missed
    # returns with 1 if the shot hit
    if board[shot] == 1 or board[shot] == 2:
        print("Hit!!\n")
        return 1
    else:
        print("Miss\n")
        return 0


def board_changer(shot, board):
    # returns with the new modified
    # board after each shot
    if board[shot] == 1 or board[shot] == 2:
        board[shot] = 2
        return board
    else:
        board[shot] = 4
        return board


def board_value(x, board):
    if board[x] == 1 or board[x] == 2:  # hit
        return 3  # picture 4 is a hit ship
    else:
        return 1  # picture 2 is a missed shot


def battle(x):
    global board1
    global board2
    # p1, board1, hp1 and p1_turn all belongs to p1.
    # the board1 contains all his ships
    # p1 shoots at p2s board under his turn (p1_turn=p2_turn)
    hp1 = 2  # predetermined
    hp2 = 2
    p1_turn = 0
    p2_turn = 0

    # AI things
    hitmarker = [0] * 5
    # after a hit there are 4 other possible locations to shoot
    # stored values: 0-to be determined, 1-successfull shot, 2-missed shot
    hit_loc = 0

    # print("The battle begins!")
    # print("Sink all the enemy ships to win!\n\n")

    while hp1 > 0 and hp2 > 0:
        if p1_turn == p2_turn:  # p1-s turn
            print("p1-s turn")
            # p1 shoots at p2s board where p2s ships are
            hit = shot(x, board2)
            hp2 = hp2 - hit
            board2 = board_changer(x, board2)
            p1_turn += 1
            continue
        if p1_turn > p2_turn:  # p2s turn AI turn
            print("AI-s turn")
            x = random.randint(0, 99)
            print(str(x))
            # p2 shoots at p1s board where p1s ships are
            hit = shot(x, board1)
            hp1 = hp1 - hit
            board1 = board_changer(x, board1)
            p2_turn += 1
            continue
    if hp1 == 0:
        print("AI won\n")
    if hp2 == 0:
        print("PLayer 1 won\n")

# ##########################################################################
# ################### THIS IS THE MAIN FUNCTION #############################


phase = 0
# 0 = prep phase
# 1 = ai prep phase
# 2 = battle phase

hp1 = 15  # predetermined
hp2 = 15  # got to pay attention!!!!

board1 = [0] * 100  # from 0-99 a 100 tiles
board2 = [0] * 100  # from 0-99 a 100 tiles

pos = 45
look = 1

ships1 = [3, 3, 4, 5]
ships2 = [3, 3, 4, 5]

hitlist1 = []
hitlist2 = []

ship_counter = 0  # helps to put the ships down

ship_handle = ["w", "a", "s", "d", "f", "g"]
# commands to move a ship during preparation and turn it or fix position

top = Tk()
font = font.Font(family="Helvetica", size=18, weight="bold")
welcome = PhotoImage(file="welcome.gif")

# borders
Label(text="Your board", font=font).grid(row=0, column=14, pady=20, columnspan=6)
Label(text="Enemy board", font=font).grid(row=0, column=3, pady=20, columnspan=6)
Label(text="").grid(row=1, column=0, padx=40)
Label(text="").grid(row=1, column=11, padx=20)
Label(text="").grid(row=12, column=11, pady=20)
Button(top, image=welcome, borderwidth=0, highlightthickness=0).grid(row=13, column=8, columnspan=7)

# image location
# gifdir = "/home/soma/Documents/TW/week0606/BSphotos/"
# img = PhotoImage(file=gifdir+"1.gif")
imgs = [""] * 4
imgs[0] = PhotoImage(file="1.gif")  # water
imgs[1] = PhotoImage(file="2.gif")  # missed shot
imgs[2] = PhotoImage(file="3.gif")  # ship
imgs[3] = PhotoImage(file="4.gif")  # hit ship
# buttonlists
user = []
ai = []

# creating buttons for the user and the ai
i = 0
for r in range(1, 11):
    for c in range(1, 11):
        btn = Button(top, image=imgs[0], borderwidth=0, height=50, width=50)
        btn.configure(command=lambda i=i: changer(i))
        btn.grid(row=r, column=c)
        ai.append(btn)
        i += 1

for r in range(1, 11):
    for c in range(12, 22):
        btn = Button(top, image=imgs[0], borderwidth=0, height=50, width=50)
        btn.grid(row=r, column=c)
        user.append(btn)


top.bind("w", lambda k: prep_changer(0))
top.bind("a", lambda k: prep_changer(1))
top.bind("s", lambda k: prep_changer(2))
top.bind("d", lambda k: prep_changer(3))
top.bind("f", lambda k: prep_changer(4))
top.bind("g", lambda k: prep_changer(5))

starter(ships1, ship_counter)

top = mainloop()
