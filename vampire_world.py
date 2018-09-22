import time
import random

def get_reply( check ):
    while check != '1' and check != '2':
        check = input("You are not so good with numbers are you? 1 or 2? ")
    return check

friends = []

def new_friend ( name ):
    friends.append(name)
    print('You made a new friend! Your friends are ')
    for f in friends:
        print(f)



print("The world is beautiful! Enjoy the vampires!")

#regime = input("Do you prefer night or day? ")
#name = input("What is your name? ")

#print("Your name is {} and your are awake at {}." .format(name, regime))
#print("Welcome to the Dungeon {}!" .format(name))

door = input("Do you wish to enter through door 1 or 2? ")
print("")

door = get_reply(door)

if door == '1':
        print('There is beautiful vampire contemplating life.')
        nvm = input(' "What is the purpose of your visit?" ')
        print(' "Nevermind. It doesnt matter. You are here now. Are you going to stay a while?')
        print('What do you do?')
        print('1. Smile and nod.')
        print('2. Scream and run.')

        reply = input(' >')

        reply = get_reply(reply)

        if reply == '1':
            print(' "Cool. Its nice to have some company. My name is Edward." ')
            new_friend('Edward')

        else:
            door = '2'
            print('You turn around and run through a random door.')

if door == '2':
    print('You enter into a dimly lit room.')
    print()
    print('When your eyes adjust to the darkness you suddenly see that there is three vampires staring at you.')




