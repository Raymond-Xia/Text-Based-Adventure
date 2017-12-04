 # Raymond Xia

import time
import random

# Global inventory list
inventory = {'flashlight':False, 'keycode':False, 'rope':False, 'hook':False, 'grapplingHook':False, 'diamonds':False}

# Global list to keep track of events in the environment that have happened
environment = {'lights':True, 'poweredTracks':False, 'cartOnTrack':False, 'poweredCart':False, 'gateOpen':False}

# Global variable for your name 
name = ""

# Title screen function

def titleScreen():
    print (" ________     ________     ___   ___    _________")
    print ("| \\_______\  | \_______\  | \_\ | \_\  | \_______\\")
    print ("| |   _____| | |   __   | | |  || |  | | |   _____|")
    print ("| |  |       | |  |__|  | | |  || |  | | |  |____")
    print ("| |  |____   | |   __   | | |  || |  | | |   ____|")
    print ("| |  |____\\  | |  || |  |  \ \  \/  /  | |  |_____")    
    print (" \\|________|  \|__| \|__|   \_\____/    \|________|")
    
    time.sleep(1)

# Introduction/Regain Conciousness function
                                                                                                
def intro():
    global name
    if name == "":
        print ("\n\"Ughhh...\"")
        time.sleep(1)
        name = input("What was my name again? ").capitalize()
        print (name + ": \"Where am I?\"")
        time.sleep(1)
        print ("You can't remember anything.")
        time.sleep(1)
    else:
        print ("\n" + name + ": \"Ughhh...\"")
        time.sleep(1)
        
    print ("\nYou get up and look around.")
    time.sleep(1)

# 75% Chance function

def chance75():
    percent= random.randrange(1,101)
    if percent <= 75:
        return True
    else:
        return False

# 1% Chance Function

def chance1():
    percent = random.randrange(1,101)
    if percent == 1:
        return True
    else:
        return False

# Cave room

def cave():
    if inventory ['flashlight'] == False:
        print ("\nYou're in a large cave, but you can't see anything. ")
        time.sleep(1)
        print ("You see light far down a narrow tunnel. You look up and see long vines leading to the surface 10m up. ")
        time.sleep(1)
        path1 = 0
        while path1 != "1" and path1 != "2":
            print ("\n 1) Go down the tunnel \n 2) Climb the vines")
            path1 = input()
            if path1 == "1":
                print ("\nYou go down the tunnel towards the light.")
                time.sleep(1)
                largeRoom()
            elif path1 == "2":
                print ("\nYou grab onto the vines and begin climbing your way up.")
                time.sleep(1)
                print ("As you are about to reach the surface...")
                time.sleep(1)
                # 1% chance to climb up the vines safely and skip the whole game
                if chance1():
                    print ("You safely pull yourself up!")
                    time.sleep(1)
                    print ("\nYou look up at the starry night sky. The full moon beams down on the landscape. As you catch your breath, you stand up and breathe in the crisp cold air.")
                    time.sleep(3)
                    mountainSide()
                else:
                    print ("The vines rip and you plummet back down knocking yourself out!")
                    time.sleep(1)
                    intro()
                    cave()

    else:
        print ("\nYou're in a large cave.")
        time.sleep(1)
        if inventory ['grapplingHook'] == False:
            print ("\nYou see light far down a narrow tunnel. You look up and see long vines leading to the surface 10m up. ")
            time.sleep(2)
            print ("\nWith the flashlight, you can see there is a hole in the ground leading down to a minecart track.")
            time.sleep(2)
            path2 = 0
            while path2 != "1" and path2 != "2" and path2 != "3":
                print ("\n 1) Go down the tunnel \n 2) Climb the vines \n 3) Jump down the hole")
                path2 = input()
                if path2 == "1":
                    print ("\nYou go down the tunnel towards the light.")
                    time.sleep(1)
                    largeRoom()
                elif path2 == "2":
                    print ("\nYou grab onto the vines and begin climbing your way up.")
                    time.sleep(2)
                    print ("As you are about to reach the surface...")
                    time.sleep(1)
                    if chance1():
                        print ("You safely pull yourself up!")
                        time.sleep(1)
                        print ("\nYou look up at the starry night sky. The full moon beams down on the landscape. As you catch your breath, you stand up and breathe in the crisp cold air.")
                        time.sleep(3)
                        mountainSide()
                    else:
                        print ("The vines rip and you plummet back down knocking yourself out!")
                        time.sleep(2)
                        intro()
                        cave()
                elif path2 == "3":
                    print ("\nYou jump down the hole and land on the minecart tracks.")
                    time.sleep(2)
                    tunnel()
        else:
            print ("\nYou see light far down a narrow tunnel. You look up and see long vines leading to the surface 10m up. ")
            time.sleep(2)
            print ("With the flashlight, you can see a hole in the ground leading down to a minecart track.")
            time.sleep(2)
            print ("\nYou could probably use your grappling hook to climb up through the hole in the ceiling.")
            time.sleep(2)
            path3 = 0
            while path3 != "1" and path3 != "2" and path3 != "3" and path3 != "4":
                print ("\n 1) Go down the tunnel \n 2) Climb the vines \n 3) Jump down the hole in the ground \n 4) Use your grappling hook to climb to the surface")
                path3 = input()
                if path3 == "1":
                    print ("\nYou go down the tunnel towards the light.")
                    time.sleep(1)
                    largeRoom()
                elif path3 == "2":
                    print ("\nYou grab onto the vines and begin climbing your way up.")
                    time.sleep(2)
                    print ("As you are about to reach the surface...")
                    time.sleep(1)
                    if chance1:
                        print ("You safely pull yourself up!")
                        time.sleep(1)
                        print ("\nYou look up at the starry night sky. The full moon beams down on the landscape. As you catch your breath, you stand up and breathe in the crisp cold air.")
                        time.sleep(3)
                        mountainSide()
                    else:
                        print ("The vines rip and you plummet back down knocking yourself out!")
                        time.sleep(2)
                        intro()
                        cave()
                elif path3 == "3":
                    print ("\nYou jump down the hole and land on the minecart tracks.")
                    time.sleep(2)
                    tunnel()
                elif path3 == "4":
                    print ("\nYou swing the grappling hook through the opening in the ceiling and climb up the rope to the surface.")
                    time.sleep(3)
                    print ("\nYou look up at the starry night sky. The full moon beams down on the landscape. As you catch your breath, you stand up and breathe in the crisp cold air.")
                    time.sleep(3)
                    mountainSide()

# Large Room room
                
def largeRoom():
    if environment ['lights'] == True or inventory ['flashlight'] == True:
        print ("\nYou are in a large room with steel supports holding up the low ceiling. \nIt is dimly lit by flickering lights wired along the ceiling. They seem to lead into a room blocked by a heavy metal door.")
        time.sleep(2)
        if inventory ['keycode'] == False:
            path1_1 = 0
            charges = 0
            while path1_1 != "1" and path1_1 != "3" and charges != 3:
                print("\n 1) Try opening the door \n 2) Try forcing the door open \n 3) Go back to the cave")
                path1_1 = input()
                if path1_1 == "1":
                    print ("\nThe door is locked by a two-digit keypad.")
                    keypad()
                elif path1_1 == "2":
                    charges += 1
                    if charges < 3:
                        print ("\nYou back up and violently charge the door with brute force. The door does not budge.")
                        time.sleep(1)
                    else:
                        print ("\nYour impatience has paid off. You actually manage to bust the door down.")
                        time.sleep(2)
                        inventory ['keycode'] = True
                        lockedRoom()
                elif path1_1 == "3":
                    print ("\nYou walk back down the tunnel.")
                    time.sleep(1)
                    cave()
                    
        else:
            path1_2 = 0
            while path1_2 != "1" and path1_2 != "2":
                print("\n 1) Open the door \n 2) Go back to the cave")
                path1_2 = input()
                if path1_2 == "1":
                    print ("\nYou open the door and walk in.")
                    time.sleep(2)
                    lockedRoom()
                elif path1_2 == "2":
                    print ("\nYou walk back down the tunnel.")
                    time.sleep(1)
                    cave()
    else:
        print ("\nYou can't see anything.")
        time.sleep(1)
        # Randomly occuring event
        if chance75():
            print ("\nAs you are wandering in the darkness, a swarm of vampire bats swoop down and attack you!")
            time.sleep(2)
            print ("You run back into the room.")
            time.sleep(1)
            lockedRoom()
        else:
            path2 = 0
            while path2 != "1" and path2 != "2":
                print("\n 1) Open the door \n 2) Try to find your back to the cave")
                path2 = input()
                if path2 == "1":
                    print ("\nYou open the door and walk in.")
                    time.sleep(1)
                    lockedRoom()
                elif path2 == "2":
                    print ("\nYou try to find your way to the tunnel.")
                    time.sleep(1)
                    print ("\nWhile you are searching the dark room for the tunnel, you trip and bang your head off a steel support, knocking yourself out.")
                    time.sleep(3)
                    intro()
                    largeRoom()

# Locked Door Keypad function
    
def keypad():
    print (" _______________")
    print ("|  ___________  |")
    print ("| |  _  |  _  | |")
    print ("| | | | | | | | |")
    print ("| | |_| | |_| | |")
    print ("| |_____|_____| |")                 
    print ("| | 1 | 2 | 3 | |")
    print ("| |___|___|___| |")
    print ("| | 4 | 5 | 6 | |")
    print ("| |___|___|___| |")
    print ("| | 7 | 8 | 9 | |")          
    print ("| |___|___|___| |")
    print ("|_______________|")
    time.sleep(1)
    print ("\nThe only possible combinations can be from 0 to 99.")
    time.sleep(2)
    combo = random.randrange(0,100)
    cracking = True
    while cracking:
        guess = input("\nTry guessing the combination or 'stop' to stop cracking the code: ")
        if guess == "stop":
            cracking = False
            largeRoom()
        elif int(guess) > combo:
            print ("A HIGH beep plays and a light flashes red.")
            time.sleep(1)
        elif int(guess) < combo:
            print ("A LOW buzz plays and a light flashes red.")
            time.sleep(1)
        else:
            print ("\nThe door clicks and flashes green.")
            inventory ['keycode'] = True
            time.sleep(2)
            cracking = False
            path = 0
            while path != "1" and path != "2":
                print ("\n 1) Open door \n 2) Go back to the cave")
                path = input()
                if path == "1":
                    print ("\nYou open the door and walk in.")
                    time.sleep(1)
                    lockedRoom()
                elif path == "2":
                    print ("\nYou walk back down the tunnel.")
                    time.sleep(1)
                    cave()    

# Locked Room room

def lockedRoom():
    path1 = 0
    path2 = 0
    if inventory ['flashlight'] == False:
        print ("\nYou are in a small room with a flashlight on a workbench and an electrical breaker box on the wall.")
        time.sleep(2)
    else:
        print ("\nYou are in a small room with a workbench and an electrical breaker box on the wall.")
        time.sleep(2)
        
    path1_1 = 0
    while inventory ['flashlight'] == False and path1 != "3" and path1_1 != "3":
        print ("\n 1) Take the flashlight \n 2) Open the electrical breaker box \n 3) Exit the room")
        path1 = input()
        if path1 == "1":
            print ("\nYou pick up the flashlight. It turns on, brightly lighting up the area in front of you.")
            inventory ['flashlight'] = True
            time.sleep(2)
        elif path1 == "2":
            print ("\nYou swing open the cover.")
            time.sleep(1)
            print ("Inside is large series of switches.")
            time.sleep(1)
            print ("One is labelled 'Lights'. Another one is labelled 'Tracks'.")
            time.sleep(2)
            path1_1 = 0
            while path1_1 != "3":
                print ("\n 1) Flip the switch labelled 'Lights' \n 2) Flip the switch labelled 'Tracks' \n 3) Close the box")
                path1_1 = input()
                if path1_1 == "1":
                    if environment ['lights'] == True:
                        environment ['lights'] = False
                        print ("\nThe flickering ceiling lights go out, leaving you in complete darkness. You can still feel your way around the room.")
                        time.sleep(2)
                    else:
                        environment ['lights'] = True
                        print ("\nThe flickering lights power on, lighting up the two rooms.")
                        time.sleep(1)
                elif path1_1 == "2":
                    if environment ['poweredTracks'] == False:
                        environment ['poweredTracks'] = True
                        print ("\nYou hear the faint hum of something powering up far away.")
                        time.sleep(1)
                        if environment ['cartOnTrack'] == True:
                            environment ['poweredCart'] = True
                            print ("\nYou hear the loud rumble of a minecart rolling along the track.")
                            time.sleep(2)
                    else:
                        environment ['poweredTracks'] = False
                        print ("\nYou hear the faint sound of something powering down far away.")
                        time.sleep(1)
                elif path1_1 == "3":
                    print ("\nYou close the box.")
                    time.sleep(1)
                    lockedRoom()        
        elif path1 == "3":
            if environment ['lights'] == True:
                print ("\nYou walk back out the door.")
                time.sleep(1)
                largeRoom()
            else:
                print ("\nYou blindly wander your way back out the door.")
                time.sleep(1)
                largeRoom()

    while inventory ['flashlight'] == True and path2 != "2":
        print ("\n 1) Open the electrical breaker box \n 2) Exit the room")
        path2 = input()
        if path2 == "1":
            print ("\nYou swing open the cover.")
            time.sleep(1)
            print ("Inside is a large series of switches.")
            time.sleep(1)
            print ("One is labelled 'Lights'. Another one is labelled 'Tracks'.")
            time.sleep(2)
            path2_1 = 0 
            while path2_1 != "3":
                print ("\n 1) Flip the switch labelled 'Lights' \n 2) Flip the switch labelled 'Tracks' \n 3) Close the box")
                path2_1 = input()
                if path2_1 == "1":
                    if environment ['lights'] == True:
                        environment ['lights'] = False
                        print ("\nThe flickering ceiling lights go out.")
                        time.sleep(1)
                    else:
                        environment ['lights'] = True
                        print ("\nThe flickering lights power on, lighting up the two rooms.")
                        time.sleep(1)
                elif path2_1 == "2":
                    if environment ['poweredTracks'] == False:
                        environment ['poweredTracks'] = True
                        print ("\nYou hear the faint hum of something powering up far away.")
                        time.sleep(1)
                        if environment ['cartOnTrack'] == True:
                            environment ['poweredCart'] = True
                            print ("\nYou hear the loud rumble of a minecart rolling along the track.")
                            time.sleep(2)
                    else:
                        environment ['poweredTracks'] = False
                        print ("\nYou hear the faint sound of something powering down far away.")
                        time.sleep(1)
                elif path2_1 == "3":
                    print ("\nYou close the box.")
                    time.sleep(1)
            
        elif path2 == "2":
            print ("\nYou walk back out the door.")
            time.sleep(1)
            largeRoom() 

# Tunnel room

def tunnel():
    if environment ['poweredTracks'] == True and environment ['poweredCart'] == False and environment ['gateOpen'] == False:
        print ("\nA low humming sound is coming from the tracks.")
        time.sleep(2)
    elif environment ['poweredCart'] == True:
        print ("\nYou hear the rumbling of a minecart speeding down the track in the distance.")
        time.sleep(2)
        print ("\nBOOOOOM!")
        time.sleep(1)
        print ("\nA large explosion echoes through the tunnel, rattling the tracks and causing dust to fall from the ceiling.")
        time.sleep(3)
        environment ['gateOpen'] = True
        environment ['poweredCart'] = False
        environment ['cartOnTrack'] = False
    print ("\nYou are in a long tunnel leading left and right.")
    time.sleep(1)
    path = 0
    while path != "1" and path != "2" and path != "3":
        print ("\n 1) Go left \n 2) Go right \n 3) Climb back up the hole")
        path = input()
        if path == "1":
            print ("\nYou go to the left and follow the tracks.")
            time.sleep(1)
            leftTunnel()
        elif path == "2":
            print ("\nYou go to the right and follow the tracks.")
            time.sleep(1)
            rightTunnel()
        elif path == "3":
            print ("\nYou jump up and climb back up the hole.")
            time.sleep(1)
            cave()

# Left side of the long tunnel room
      
def leftTunnel():
    print ("\nYou are in an small area scattered with minecarts.")
    time.sleep(1)
    path1 = 0
    path2 = 0
    while path1 != "3" and path2 != "2":
        if environment ['cartOnTrack'] == False and environment ['gateOpen'] == False:
            print ("\n 1) Search the minecarts \n 2) Push a minecart onto the tracks \n 3) Go back down the tracks")
            path1 = input()
            if path1 == "1":
                print ("\nYou look in the minecarts.")
                time.sleep(1)
                print ("The carts are filled with explosives. They are too heavy for you to lift.")
                time.sleep(2)
                if inventory ['rope'] == False:
                    print ("\nYou find a long rope in one of the carts.")
                    inventory ['rope'] = True
                    time.sleep(2)
                    if inventory ['hook'] == True:
                        print ("You attach the the hook to the rope to create a makeshift grappling hook.")
                        inventory ['grapplingHook'] = True
                        time.sleep(2)
            elif path1 == "2":
                print ("\nYou push a heavy minecart onto the tracks.")
                environment ['cartOnTrack'] = True
                time.sleep(1)
                if environment ['poweredTracks'] == False:
                    print ("\nThe wheels screech as you try to push it along the tracks. It does not move.")
                    time.sleep(2)
                else:
                    print ("\nThe cart smoothly rolls along the tracks.")
                    time.sleep(2)
                    print ("\nIt slowly starts picking up speed and barrels down the powered tracks towards the right end of the tunnel at full speed.")
                    environment ['poweredCart'] = True
                    time.sleep(3)
            elif path1 == "3":
                print ("\nYou walk back down the tracks.")
                time.sleep(1)
                tunnel()
        else:
            print ("\n 1) Search the minecarts \n 2) Go back down the tracks")
            path2 = input()
            if path2 == "1":
                print ("\nYou look in the minecarts.")
                time.sleep(1)
                print ("The carts are filled with explosives. They are too heavy for you to lift.")
                time.sleep(2)
                if inventory ['rope'] == False:
                    print ("\nYou find a long rope in one of the carts.")
                    inventory ['rope'] = True
                    time.sleep(2)
            elif path2 == "2":
                print ("\nYou walk back down the tracks.")
                time.sleep(1)
                tunnel()

# Right side of the long tunnel room
        
def rightTunnel():
    if environment ['gateOpen'] == False:
        print ("\nYou reach a dead end. The tunnel is blocked off by a large metal gate.")
        time.sleep(2)
        print ("There seems to be a storage room on the other side.")
        time.sleep(1)
        path1 = 0
        while path1 != "2":
            print ("\n 1) Try opening the gate \n 2) Go back down the tracks")
            path1 = input()
            if path1 == "1":
                print ("\nYou can't open this gate yourself.")
                time.sleep(1)
            elif path1 == "2":
                print ("\nYou walk back down the tracks.")
                time.sleep(1)
                tunnel()
    else:
        print ("\nYou are by what used to be a metal gate.")
        time.sleep(1)
        print ("There is a large hole blown in the center of the gate. The area is littered with twisted scrap metal.")
        time.sleep(2)
        path2 = 0
        while path2 != "1" and path2 != "2":
            print ("\n 1) Go through the gate \n 2) Go back down the tracks")
            path2 = input()
            if path2 == "1":
                print ("\nYou walk through the gate.")
                time.sleep(1)
                storageRoom()
            elif path2 == "2":
                print ("\nYou walk back down the tracks.")
                time.sleep(1)
                tunnel()

# Storage Room room
                
def storageRoom():
    print ("\nYou are in a large storage room filled with crates.")
    time.sleep(1)
    path = 0
    while path != "2":
        print ("\n 1) Search the crates \n 2) Go back through the gate")
        path = input()
        if path == "1":
            print ("\nYou look through the crates.")
            time.sleep(1)
            if inventory ['hook'] == False and inventory ['diamonds'] == False:
                print ("\nYou find a metal hook and a crate full of diamonds. You take as many as you can carry with you.")
                inventory ['hook'] = True
                inventory ['diamonds'] = True
                time.sleep(3)
                if inventory ['rope'] == True:
                    print ("\nYou attach the hook to the rope to create a makeshift grappling hook.")
                    inventory ['grapplingHook'] = True
                    time.sleep(2)
                print ("\nThe rest of the crates are filled with various precious metals. They are too heavy for you to carry.")
                time.sleep(2)
            else:
                print ("The crates are filled with various precious metals. They are too heavy for you to carry.")
                time.sleep(2)
        elif path == "2":
            print ("You go back through the gate.")
            rightTunnel()
            time.sleep(1)

# Mountain Side room
            
def mountainSide():
    print ("\nYou are on the side of a mountain leading down into a large valley.")
    time.sleep(2)
    print ("There is a small town in the valley.")
    time.sleep(1)
    print ("Towards the snowy peak of the mountain is a temple.")
    time.sleep(2)
    toBeContinued()

# To Be Continued? function
    
def toBeContinued():
    print (" ________  ________    ________  ________")
    print ("|__    __||   __   |  |   __   ||   _____|")
    print ("   |  |   |  |  |  |  |  |__| _||  |____")
    print ("   |  |   |  |  |  |  |   __ |_ |   ____|")
    print ("   |  |   |  |__|  |  |  |__|  ||  |_____")
    print ("   |__|   |________|  |________||________|")
    print ("")
    print (" ________  ________  ___   __  ________  __  ___   __  __    __  ________  ______      ______")
    print ("|   __   ||   __   ||   \ |  ||__    __||  ||   \ |  ||  |  |  ||   _____||   __  `, ,*  __  *,")
    print ("|  |  |__||  |  |  ||    \|  |   |  |   |  ||    \|  ||  |  |  ||  |____  |  |  |  ' |__|  /  |")
    print ("|  |   __ |  |  |  ||  |\    |   |  |   |  ||  |\    ||  |  |  ||   ____| |  |  |  |     ,* ,*")
    print ("|  |__|  ||  |__|  ||  | \   |   |  |   |  ||  | \   ||  |__|  ||  |_____ |  |__,  ,    |__|")
    print ("|________||________||__|  \__|   |__|   |__||__|  \__||________||________||______,'     |__|")
    
# Main function

def main():
    titleScreen()
    intro()
    cave()
    

if __name__ == "__main__":
    main()










# This was the second part of the game I meant to include but had to cut out because I ran out of time. Why did I leave this here? Because I wasted a few days on it and would feel bad if I deleted it.

#def mountainSide():
    #print ("\nYou are on the side of a mountain leading down into a large valley.")
    #time.sleep(3.5)
    #print ("There is a small town in the valley.")
    #time.sleep(3)
    #print ("Towards the snowy peak of the mountain is a temple.")
    #time.sleep(5)
    #path = 0
    #while path != "1" and path != "3":
        #print ("\n 1) Go down the mountain to the town \n 2) Go up the mountain to the temple \n 3) Jump back down the hole into the cave")
        #path = input()
        #if path == "1":
            #print ("\nYou start descending down the mountain.")
            #time.sleep(1)
            #print ("\nSuddenly a large gust of wind throws you off your feet and you tumble down mountain!")
            #cabinKO()
            
        #elif path == "2":
            #print ("\nYou start climbing your way up the mountain.")
            #if environment ['night'] == True:
                #print ("\nThe temperture drops and you start freezing. It is too cold in the night. You climb back down.")
            #else:
                #print ("You make it to the entrance of the temple and walk in.")
                #temple()

        #elif path == "3":
            #print ("\nYou jump back down the hole, unable to see the ground through the darkness.")
            #print ("The 10m drop catches you off guard and you knock yourself out.")
            #intro()
            #cave()

#def cabinKO():
    #global name
    #print ("\n...")
    #time.sleep(2)
    #print ("\n" + name + ": \"Ughhh...\"")
    #time.sleep(1)
    #print ("You have a massive headache. ")
    #time.sleep(1)
    #print (name + ": \"W-where am I?\"")
    #time.sleep(1)
    #print ("You hear a door slam.")
    #time.sleep(1)
    #print ("...")
    #time.sleep(1)
    #print ("\nYou wake up and look around.")
    #print ("You don't have your flashlight or grappling hook anymore.")
    #cabin()

#def cabin():
    #print ("\nYou are in an empty wooden cabin. There's no one else in the room.")
    #time.sleep(1)
    #path = 0
    #while path != "2":
        #print ("\n 1) Look out the window \n 2) Go outside")
        #path = input()
        #if path == "1":
            #print ("\nYou walk up to the window and take a look outside.")
            #time.sleep(1)
            #print ("\nYou're in outskirts of the village in the valley. Mountains can be seen in the background behind the buildings. It's already afternoon.")
        #elif path == "2":
            #print ("\nYou open the door and walk outside onto the porch.")
            #time.sleep(1)
            #cabinPorch()

#def cabinPorch():
    #print ("\nYou look up at the afternoon sun in the middle of the sky.")
    #time.sleep(1)
    #print ("\n 1) Take a look around the village \n 2) Go back in cabin")
    #path = input()
    #if path == "1":
        #print ("\nYou walk through the village passing various buildings.")
        #village()
    #elif path == "2":
        #print ("\nYou open the door and walk back in.") 
        #cabin()
           
#def villageCenter():
    #print ("You are in the center of the village. There's a mansion in the middle of the village.")
    #print ("\n 1) Knock on the door to the mansion \n 2) Go back to the cabin")
    #path = input()
    #if path == "1":
        #print ("")
    #elif path == "2":
        #print ("You walk back to the cabin.")
        #cabin()
            
#def mountainPeak():
    #print ("The chest is in the middle of a large sheet of ice covering the top of the mountain.")
    #print ("Do you: \n 1) Go to open the chest \n 2) Go back down the mountain \n 3) Jump off the mountain")
    #path = input()
    #if path == "1":
        #print ("As you appoach the chest...")
        #time.sleep(1)
        #print ("The ice cracks and you freefall down the vast darkness of the mountain!")
        #time.sleep(1)
    #elif path == "2":
        #print ("\nYou go back down the side of the mountain.")
        #mountainSide()
    #elif path == "3":
        #print ("\nYou run towards the edge of the mountain and dive over the cliff.")
        #time.sleep(1)
        #print ("You hit the ground and die.")
        #print ("...What did you expect?")
        #time.sleep(3)
        #intro()


#def village1():
    #print ("\nThe citizens start to notice your unfamiliar face. They stare at you nervously as you pass them. Some shoot you dirty looks.")
    #print ("\nThe doors of an official-looking building burst open as a woman arguing with two men in suits comes out.")
    #print ("You sees you through the crowd.")
    #print ("\nWoman: Hey, there he is!")
    #print ("The cops start running towards you.")
    #print ("\n 1) Fight \n 2) Put your hands up")
    #path = input()
    #if path == "1":
        #print ("")
    #elif path == "2":
        #print ("You stay calm and slowly raise your hands.")
        #print ("They grab your hands and handcuff you.")
