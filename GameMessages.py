
# Game Messages
room1 = '''    After a drunken night out with friends, you awaken the 
    next morning in a thick, dank forest. Head spinning and 
    fighting the urge to vomit, you stand and marvel at your new, 
    unfamiliar setting. The peace quickly fades when you hear a 
    grotesque sound emitting behind you. A slobbering orc is 
    running towards you. You will:'''

choicesOfRoom1 = '''    A. Grab a nearby rock and throw it at the orc
    B. Lie down and wait to be mauled
    C. Run'''

room1dieMessage = '''    Welp, that was quick. "
    You died!'''

rockRoom = '''    The orc is stunned, but regains control. He begins
    running towards you again. Will you:   '''

choicesOfRockRoom = '''    A. Run
    B. Throw another rock
    C. Run towards a nearby cave'''

rockRoomdieMessage = '''    You decided to throw another rock, as if the first
    rock thrown did much damage. The rock flew well over the
    orcs head. You missed. \n\nYou died!'''

caveRoom = '''    You were hesitant, since the cave was dark and
    ominous. Before you fully enter, you notice a shiny sword on
    the ground. Do you pick up a sword. Y/N?'''

askNext = "    What do you do next?"

swordOptions = '''    A. Hide in silence
    B. Fight
    C. Run'''

caveRoomdieMessage1 = '''    Really? You're going to hide in the dark? I think 
    orcs can see very well in the dark, right? Not sure, but 
    I'm going with YES, so...\n\nYou died!'''

caveRoomSurvived = '''    You laid in wait. The shimmering sword attracted
    the orc, which thought you were no match. As he walked
    closer and closer, your heart beat rapidly. As the orc
    reached out to grab the sword, you pierced the blade into
    its chest. \n\nYou survived!'''

caveRoomdieMessage2 = '''    You should have picked up that sword. You're
    defenseless. \n\nYou died!'''

caveRoomRun = '''    As the orc enters the dark cave, you sliently 
    sneak out. You're several feet away, but the orc turns 
    around and sees you running.'''

runRoom = '''    You run as quickly as possible, but the orc's 
    speed is too great. You will:'''

choicesOfRunRoom = '''    A. Hide behind boulder
    B. Trapped, so you fight
    C. Run towards an abandoned town'''

runRoomDieMessage1 = '''    You're easily spotted.
    \n\nYou died!'''

runRoomDieMessage2 = '''    You're no match for an orc.
    \n\nYou died!'''

townRoom = '''    While frantically running, you notice a rusted 
    sword lying in the mud. You quickly reach down and grab it, 
    but miss. You try to calm your heavy breathing as you hide 
    behind a delapitated building, waiting for the orc to come 
    charging around the corner. You notice a purple flower 
    near your foot. Do you pick it up? Y/N'''

townRoomMessage = '''    You hear its heavy footsteps and ready yourself for
    the impending orc.'''

townRoomSurvived = '''    You quickly hold out the purple flower, somehow
    hoping it will stop the orc. It does! The orc was looking
    for love.
    \n\nThis got weird, but you survived!'''

townRoomDieMessage = '''    Maybe you should have picked up the flower.
    \n\nYou died!'''


# # # # # # # # # # #  # #  # Create audio for messages  # # # # # # # # # # # # # #
## Hence below code need to run once only.
## Just run in python console as " from GameMessages import * "
## This will create and save all audio files.
## Then we can  comment this code because while AdventureTextGameWithSound.py script access messages from this module,
## if we not commented them it will again run all these and that is not needed.
## Also it will take too time.

# from gtts import gTTS  #Import modules for text to speech conversion
# # os.system("mpg321 room1.mp3")
# # a = subprocess.run("mpg321 room1.mp3", shell=True, stderr=subprocess.DEVNULL, stdout= subprocess.DEVNULL)
#
# # Audio for room1
# tts = gTTS(text=room1, lang='en')
# tts.save("room1.mp3")
#
# # Audio for choicesOfRoom1
# tts = gTTS(text=choicesOfRoom1, lang='en')
# tts.save("choicesOfRoom1.mp3")
#
# # Audio for room1dieMessage
# tts = gTTS(text=room1dieMessage, lang='en')
# tts.save("room1dieMessage.mp3")
#
# # Audio for rockRoom
# tts = gTTS(text=rockRoom, lang='en')
# tts.save("rockRoom.mp3")
#
# # Audio for choicesOfRockRoom
# tts = gTTS(text=choicesOfRockRoom, lang='en')
# tts.save("choicesOfRockRoom.mp3")
#
# # Audio for rockRoomdieMessage
# tts = gTTS(text=rockRoomdieMessage, lang='en')
# tts.save("rockRoomdieMessage.mp3")
#
# # Audio for caveRoom
# tts = gTTS(text=caveRoom, lang='en')
# tts.save("caveRoom.mp3")
#
# # Audio for askNext
# tts = gTTS(text=askNext, lang='en')
# tts.save("askNext.mp3")
#
# # Audio for swordOptions
# tts = gTTS(text=swordOptions, lang='en')
# tts.save("swordOptions.mp3")
#
# # Audio for caveRoomdieMessage1
# tts = gTTS(text=caveRoomdieMessage1, lang='en')
# tts.save("caveRoomdieMessage1.mp3")
#
# # Audio for caveRoomSurvived
# tts = gTTS(text=caveRoomSurvived, lang='en')
# tts.save("caveRoomSurvived.mp3")
#
# # Audio for caveRoomdieMessage2
# tts = gTTS(text=caveRoomdieMessage2, lang='en')
# tts.save("caveRoomdieMessage2.mp3")
#
# # Audio for caveRoomRun
# tts = gTTS(text=caveRoomRun, lang='en')
# tts.save("caveRoomRun.mp3")
#
# # Audio for runRoom
# tts = gTTS(text=runRoom, lang='en')
# tts.save("runRoom.mp3")
#
# # Audio for choicesOfRunRoom
# tts = gTTS(text=choicesOfRunRoom, lang='en')
# tts.save("choicesOfRunRoom.mp3")
#
# # Audio for runRoomDieMessage1
# tts = gTTS(text=runRoomDieMessage1, lang='en')
# tts.save("runRoomDieMessage1.mp3")
#
# # Audio for runRoomDieMessage2
# tts = gTTS(text=runRoomDieMessage2, lang='en')
# tts.save("runRoomDieMessage2.mp3")
#
# # Audio for townRoom
# tts = gTTS(text=townRoom, lang='en')
# tts.save("townRoom.mp3")
#
# # Audio for townRoomMessage
# tts = gTTS(text=townRoomMessage, lang='en')
# tts.save("townRoomMessage.mp3")
#
# # Audio for townRoomSurvived
# tts = gTTS(text=townRoomSurvived, lang='en')
# tts.save("townRoomSurvived.mp3")
#
# # Audio for townRoomDieMessage
# tts = gTTS(text=townRoomDieMessage, lang='en')
# tts.save("townRoomDieMessage.mp3")
