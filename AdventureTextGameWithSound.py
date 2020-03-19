import time  # Imports a module to add a pause
print(1)
# import all Game messages
from GameMessages import room1, choicesOfRoom1, room1dieMessage, rockRoom, choicesOfRockRoom, rockRoomdieMessage, caveRoom, askNext,swordOptions, caveRoomdieMessage1, caveRoomSurvived, caveRoomdieMessage2, caveRoomRun, runRoom, choicesOfRunRoom, runRoomDieMessage1, runRoomDieMessage2, townRoom, townRoomMessage, townRoomSurvived, townRoomDieMessage
print(2)
import subprocess
print(3)
# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Grabbing objects
sword = 0
flower = 0

required = "\nUse only A, B, or C\n"  # Cutting down on duplication

# The story is broken into sections, starting with "intro"
def intro():
    print(room1)
    a = subprocess.run("mpg321 room1.mp3", shell=True, stderr=subprocess.DEVNULL, stdout= subprocess.DEVNULL)

    # time.sleep(12)
    print(choicesOfRoom1)
    subprocess.run("mpg321 choicesOfRoom1.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print(room1dieMessage)
        subprocess.run("mpg321 room1dieMessage.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_rock():
    print(rockRoom)
    subprocess.run("mpg321 rockRoom.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    time.sleep(1)
    print(choicesOfRockRoom)
    subprocess.run("mpg321 choicesOfRockRoom.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print(rockRoomdieMessage)
        subprocess.run("mpg321 rockRoomdieMessage.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_cave():
    print(caveRoom)
    subprocess.run("mpg321 caveRoom.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    choice = input(">>> ")
    if choice in yes:
        sword = 1  # adds a sword
    else:
        sword = 0
    print(askNext)
    subprocess.run("mpg321 askNext.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    time.sleep(1)
    print(swordOptions)
    subprocess.run("mpg321 swordOptions.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    choice = input(">>> ")
    if choice in answer_A:
        print(caveRoomdieMessage1)
        subprocess.run("mpg321 caveRoomdieMessage1.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    elif choice in answer_B:
        if sword > 0:
            print(caveRoomSurvived)
            subprocess.run("mpg321 caveRoomSurvived.mp3", shell=True, stderr=subprocess.DEVNULL,
                           stdout=subprocess.DEVNULL)
        else:  # If the user didn't grab the sword
            print(caveRoomdieMessage2)
            subprocess.run("mpg321 caveRoomSurvived.mp3", shell=True, stderr=subprocess.DEVNULL,
                           stdout=subprocess.DEVNULL)
    elif choice in answer_C:
        print(caveRoomRun)
        subprocess.run("mpg321 caveRoomRun.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print(runRoom)
    subprocess.run("mpg321 runRoom.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    time.sleep(1)
    print(choicesOfRunRoom)
    subprocess.run("mpg321 choicesOfRunRoom.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    choice = input(">>> ")
    if choice in answer_A:
        print(runRoomDieMessage1)
        subprocess.run("mpg321 runRoomDieMessage1.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    elif choice in answer_B:
        print(runRoomDieMessage2)
        subprocess.run("mpg321 runRoomDieMessage2.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print(townRoom)
    subprocess.run("mpg321 townRoom.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    choice = input(">>> ")
    if choice in yes:
        flower = 1  # adds a flower
    else:
        flower = 0
    print(townRoomMessage)
    subprocess.run("mpg321 townRoomMessage.mp3", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    time.sleep(1)
    if flower > 0:
        print(townRoomSurvived)
        subprocess.run("mpg321 townRoomSurvived.mp3", shell=True, stderr=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL)
    else:  # If the user didn't grab the sword
        print(townRoomDieMessage)
        subprocess.run("mpg321 townRoomDieMessage.mp3", shell=True, stderr=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL)


intro()
