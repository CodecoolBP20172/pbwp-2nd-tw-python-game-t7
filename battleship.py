from tkinter import *
from PIL import *
import time
import random
from tkinter import font

# Gets called after a button is being pushed.


def changer(x):
    global phase
    global board1
    global board2
    global hp1
    global hp2

    if phase == 2:
        hit = shot(x, board2)
        if hit != 2:

            if hit == 1:
                hp2 = hp2 - hit
            board2 = board_changer(x, board2)
            board_value_num = board_value(x, board2)
            print(str(board_value_num))
            ai[x].configure(image=imgs[board_value_num])

            hit = 2
            while hit == 2:
                ai_shot_pos = AI_shotter_for_real(board1)
                hit = shot(ai_shot_pos, board1)
                if hit == 1:
                    hp1 = hp1 - hit
                board1 = board_changer(ai_shot_pos, board1)
                board_value_num_2 = board_value(ai_shot_pos, board1)
                print(str(board_value_num_2))
                user[ai_shot_pos].configure(image=imgs[board_value_num_2])
                if hp1 == 0 or hp2 == 0:
                    if hp1 == 0:
                        print("AI won\n")
                        finish(0)
                    if hp2 == 0:
                        print("PLayer 1 won\n")
                        finish(1)


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

        elif command == ship_handle[3] and turn == 0:  # d moves right
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
            ship_counter += 1
            try:
                while ship_pos_validator(pos, ships1[ship_counter], look, board1) != 0:
                    look = random.randint(1, 2)  # the ship's direction RANDOM
                    pos = random.randint(0, 99)  # the ship's position RANDOM
            except(IndexError):
                pass
            starter(ships1, ship_counter, pos, look)
    if ship_counter == len(ships1):
        phase = 1
        ship_counter = 0
    if phase == 1:
        phase = prep_phase_AI(ship_handle, ships2, board2, 0)
        print(board2)
    print("\n")

# 0 = prep phase
# 1 = ai prep phase
# 2 = battle phase
# board2 = [0]*100 # from 0-99 a 100 tiles
# board values:
# 0 - nothing
# 1 - ship
# 2 - ship that got a hit
# 4 - missed shot
# ship value means how long the ship is.


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
            new_pos = pos + i
            if board[new_pos] != 0:
                print("Can't put it in another ship sry")
                return 1
    new_pos = pos
    if command == "f" and look == 2:
        for i in range(length):
            new_pos = new_pos + 10
            if new_pos > 99:
                print ("You would step out of the gameboard!")
                return 1
            new_pos = pos + i * 10
            if board[new_pos] != 0:
                print("Can't put it in another ship sry")
                return 1
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
                if i > 0 and (pos + i) % 10 == 0:
                    print("You can't put that ship there")
                    return 1
            except IndexError:
                print("You can't put that ship there")
                return 1
    return 0


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


def shot(shot, board):
    # returns with 0 if the shot missed
    # returns with 1 if the shot hit
    if board[shot] == 1:
        print("Hit!!\n")
        return 1
    elif board[shot] == 2 or board[shot] == 4:
        print("You already shot there")
        return 2
    elif board[shot] == 0:
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


def AI_shotter_for_real(board):
    hit_list = []
    operations = ["+ 1", "- 1", "+ 10", "- 10"]
    for index in range(len(board)):
        if board[index] == 2:
            for op_index in operations:
                str_index = str(index)
                real_index_for_shooting = eval(str_index + op_index)
                try:
                    if board[real_index_for_shooting] == 1 or board[real_index_for_shooting] == 0:
                        hit_list.append(real_index_for_shooting)
                except(IndexError):
                    continue
    if len(hit_list) > 0:
        shoot_pos = hit_list[random.randint(0, len(hit_list)-1)]
    else:
        shoot_pos = random.randint(0, 99)
    return shoot_pos


def finish(winner):

    time.sleep(0.75)
    for button in ai:
        button.destroy()
    for button in user:
        button.destroy()
    Label1.destroy()
    Label2.destroy()
    Label3.destroy()
    Label4.destroy()
    Label5.destroy()
    Label6.destroy()

    if winner == 0:
        Label(text="You lose", font=font).grid(row=12, column=11, pady=100, padx=100, columnspan=100)
    if winner == 1:
        Label(text="You won", font=font).grid(row=12, column=11, pady=100, padx=100, columnspan=100)


# ##########################################################################
# ################### THIS IS THE MAIN FUNCTION #############################


phase = 0
# 0 = prep phase
# 1 = ai prep phase
# 2 = battle phase

hp1 = 15  # predetermined
hp2 = 15

board1 = [0] * 100  # from 0-99 a 100 tiles
board2 = [0] * 100  # from 0-99 a 100 tiles

pos = 45
look = 1

ships1 = [3, 3, 4, 5]
ships2 = [3, 3, 4, 5]

ship_counter = 0  # helps to put the ships down

ship_handle = ["w", "a", "s", "d", "f", "g"]
# commands to move a ship during preparation and turn it or fix position

top = Tk()
font = font.Font(family="Helvetica", size=18, weight="bold")

welcome = PhotoImage(file="welcome.gif")

# borders
Label1 = Label(text="Your board", font=font)
Label1.grid(row=0, column=14, pady=20, columnspan=6)

Label2 = Label(text="Enemy board", font=font)
Label2.grid(row=0, column=3, pady=20, columnspan=6)

Label3 = Label(text="")
Label3.grid(row=1, column=0, padx=40)

Label4 = Label(text="")
Label4.grid(row=1, column=11, padx=20)

Label5 = Label(text="")
Label5.grid(row=12, column=11, pady=20)

Label6 = Label(text="")
Label6.grid(row=12, column=23, padx=40)

Button(top, image=welcome, borderwidth=0, highlightthickness=0, command=lambda k=0: sys.exit()).grid(
    row=13, column=8, columnspan=7)

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
