import time  # Imports a module to add a pause
from gtts import gTTS
import os
import subprocess
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
    room1 = '''    After a drunken night out with friends, you awaken the 
    next morning in a thick, dank forest. Head spinning and 
    fighting the urge to vomit, you stand and marvel at your new, 
    unfamiliar setting. The peace quickly fades when you hear a 
    grotesque sound emitting behind you. A slobbering orc is 
    running towards you. You will:'''

    print(room1)

    tts = gTTS(text=room1, lang='en')
    tts.save("room1.mp3")
    # os.system("mpg321 room1.mp3")
    sp = subprocess.run("mpg321 room1.mp3", shell=True, stderr=subprocess.DEVNULL, stdout= subprocess.DEVNULL)

    time.sleep(1)

    choicesOfRoom1 = """    A. Grab a nearby rock and throw it at the orc
    B. Lie down and wait to be mauled
    C. Run"""
    print(choicesOfRoom1)
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        Room1dieMessage = '''Welp, that was quick. "
        You died!'''
        # print("\nWelp, that was quick. "
        #       "\n\nYou died!")
        print(Room1dieMessage)
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_rock():
    rockRoom = '''The orc is stunned, but regains control. He begins "
          "running towards you again. Will you:   '''
    # print("\nThe orc is stunned, but regains control. He begins "
    #       "running towards you again. Will you:")
    print(rockRoom)
    time.sleep(1)
    choicesOfRockRoom = """  A. Run
  B. Throw another rock
  C. Run towards a nearby cave"""
  #   print("""  A. Run
  # B. Throw another rock
  # C. Run towards a nearby cave""")
    print(choicesOfRockRoom)
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        rockRoomdieMessage = '''You decided to throw another rock, as if the first
              rock thrown did much damage. The rock flew well over the
              orcs head. You missed. \n\nYou died!'''
        # print("\nYou decided to throw another rock, as if the first "
        #       "rock thrown did much damage. The rock flew well over the "
        #       "orcs head. You missed. \n\nYou died!")
        print(rockRoomdieMessage)
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_cave():
    caveRoom = '''You were hesitant, since the cave was dark and
          ominous. Before you fully enter, you notice a shiny sword on
          the ground. Do you pick up a sword. Y/N?'''
    # print("\nYou were hesitant, since the cave was dark and "
    #       "ominous. Before you fully enter, you notice a shiny sword on "
    #       "the ground. Do you pick up a sword. Y/N?")
    print(caveRoom)
    choice = input(">>> ")
    if choice in yes:
        sword = 1  # adds a sword
    else:
        sword = 0
    askNext = "What do you do next?"
    # print("\nWhat do you do next?")
    print(askNext)
    time.sleep(1)
    swordOptions = """  A. Hide in silence
  B. Fight
  C. Run"""
  #   print("""  A. Hide in silence
  # B. Fight
  # C. Run""")
    print(swordOptions)
    choice = input(">>> ")
    if choice in answer_A:
        caveRoomdieMessage1 = '''Really? You're going to hide in the dark? I think 
              orcs can see very well in the dark, right? Not sure, but 
              I'm going with YES, so...\n\nYou died!'''
        # print("\nReally? You're going to hide in the dark? I think "
        #       "orcs can see very well in the dark, right? Not sure, but "
        #       "I'm going with YES, so...\n\nYou died!")
        print(caveRoomdieMessage1)
    elif choice in answer_B:
        if sword > 0:
            caneRoomSurvived = '''You laid in wait. The shimmering sword attracted "
                  "the orc, which thought you were no match. As he walked "
                  "closer and closer, your heart beat rapidly. As the orc "
                  "reached out to grab the sword, you pierced the blade into "
                  "its chest. \n\nYou survived!'''
            # print("\nYou laid in wait. The shimmering sword attracted "
            #       "the orc, which thought you were no match. As he walked "
            #       "closer and closer, your heart beat rapidly. As the orc "
            #       "reached out to grab the sword, you pierced the blade into "
            #       "its chest. \n\nYou survived!")
            print(caneRoomSurvived)
        else:  # If the user didn't grab the sword
            caveRoomdieMessage2 = '''You should have picked up that sword. You're "
                  "defenseless. \n\nYou died!'''
            # print("\nYou should have picked up that sword. You're "
            #       "defenseless. \n\nYou died!")
            print(caveRoomdieMessage2)
    elif choice in answer_C:
        caveRoomRun = '''As the orc enters the dark cave, you sliently 
              sneak out. You're several feet away, but the orc turns 
              around and sees you running.'''
        # print("As the orc enters the dark cave, you sliently "
        #       "sneak out. You're several feet away, but the orc turns "
        #       "around and sees you running.")
        print(caveRoomRun)
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    runRoom = '''You run as quickly as possible, but the orc's 
          speed is too great. You will:'''
    # print("\nYou run as quickly as possible, but the orc's "
    #       "speed is too great. You will:")
    print(runRoom)
    time.sleep(1)
    choicesOfRunRoom = '''  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town'''
  #   print("""  A. Hide behind boulder
  # B. Trapped, so you fight
  # C. Run towards an abandoned town""")
    print(choicesOfRunRoom)
    choice = input(">>> ")
    if choice in answer_A:
        runRoomDieMessage1 = '''You're easily spotted. "
              "\n\nYou died!'''
        # print("You're easily spotted. "
        #       "\n\nYou died!")
        print(runRoomDieMessage1)
    elif choice in answer_B:
        runRoomDieMessage2 = '''You're no match for an orc. "
              "\n\nYou died!'''
        # print("\nYou're no match for an orc. "
        #       "\n\nYou died!")
        print(runRoomDieMessage2)
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    townRoom = '''While frantically running, you notice a rusted 
          sword lying in the mud. You quickly reach down and grab it, 
          but miss. You try to calm your heavy breathing as you hide 
          behind a delapitated building, waiting for the orc to come 
          charging around the corner. You notice a purple flower 
          near your foot. Do you pick it up? Y/N'''
    # print("\nWhile frantically running, you notice a rusted "
    #       "sword lying in the mud. You quickly reach down and grab it, "
    #       "but miss. You try to calm your heavy breathing as you hide "
    #       "behind a delapitated building, waiting for the orc to come "
    #       "charging around the corner. You notice a purple flower "
    #       "near your foot. Do you pick it up? Y/N")
    print(townRoom)
    choice = input(">>> ")
    if choice in yes:
        flower = 1  # adds a flower
    else:
        flower = 0
    townRoomMessage = '''You hear its heavy footsteps and ready yourself for "
          "the impending orc.'''
    # print("You hear its heavy footsteps and ready yourself for "
    #       "the impending orc.")
    print(townRoomMessage)
    time.sleep(1)
    if flower > 0:
        townRoomSurvived = '''You quickly hold out the purple flower, somehow "
              "hoping it will stop the orc. It does! The orc was looking "
              "for love. "
              "\n\nThis got weird, but you survived!'''
        # print("\nYou quickly hold out the purple flower, somehow "
        #       "hoping it will stop the orc. It does! The orc was looking "
        #       "for love. "
        #       "\n\nThis got weird, but you survived!")
        print(townRoomSurvived)
    else:  # If the user didn't grab the sword
        townRoomDieMessage = '''Maybe you should have picked up the flower. "
              "\n\nYou died!'''
        # print("\nMaybe you should have picked up the flower. "
        #       "\n\nYou died!")
        print(townRoomDieMessage)


intro()
