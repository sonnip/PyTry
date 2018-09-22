import time
import random

door_greetings = {'1': "This is Edwards room.", '2' : "You enter into a dimly lit room."}

def get_reply( check ):
    while check != '1' and check != '2':
        check = input("You are not so good with numbers are you? 1 or 2? ")
    return check

def end():
    print()
    print()
    time.sleep(4)
    print('THE END')
    print()
    print('Do you want to start over?')
    print('1. Start again.')
    print('2. No, thank you.')
    reply = input(' >')
    get_reply(reply)
    if reply == '1':
        start()
    else:
        print('Bye!')


friends = []

def new_friend ( name ):
    friends.append(name)
    print('You made a new friend!')

def print_friends():
    print('Your friends are ')
    for f in friends:
        print(f)
    print()

def vamps_death():
    print()
    print('Fool. They are much faster than you.')
    print()
    print()
    print()
    time.sleep(1)
    print('GAME OVER')

def leave_dungeon():
    print('You say "Goodbye" and leave the dungeon.')
    print(('The next morning you wake up and ask yourself:'))
    print('"Did that really just happen??"')



def door_one( name ):
        print('{}'.format(door_greetings['1']))
        print('There is beautiful vampire contemplating life.')
        nvm = input('"What is the purpose of your visit?" ')
        print('"Nevermind. It doesnt matter. You are here now. Are you going to stay a while?')
        print('What do you do?')
        print('1. Smile and nod.')
        print('2. Scream and run.')

        reply = input(' >')

        reply = get_reply(reply)

        if reply == '1':
            print(' "Cool. Its nice to have some company. My name is Edward." ')
            print()
            new_friend('Edward')
            print_friends()
            print(' "Come, I want to introduce you to the others."')
            time.sleep(2)
            print()
            print()
            door_two( name )

        else:
            print('You turn around and run through a random door.')
            door_two( name )

def door_two( name ):
    print('{}'.format(door_greetings['2']))
    print()
    print('When your eyes adjust to the darkness you suddenly see that there is three vampires looking at you.')
    print()
    time.sleep(1)
    print('What do you do?')
    print('1. Bow and introduce yourself.')
    print('2. Stare at them.')

    reply = input(' >')

    reply = get_reply(reply)

    if reply == '1':
            print('You bow respectfully and say "Greetings, my name is {}"' .format(name))
            print()
            time.sleep(1)
            print('The vampires appreciate your respectful introduction.')
            print()
            time.sleep(1)
            print('The tallest of the vampires steps forward.')
            time.sleep(2)
            print('"Welcome {}. My name is Roberta and these are my sisters Tavia and Maitane."' .format(name))
            print()
            time.sleep(1)
            new_friend('Roberta')
            new_friend('Tavia')
            new_friend('Maitane')
            print()
            print_friends()
            print()
            time.sleep(2)
            print('"We are very hungry but you seem friendly so we wont drink your blood."')
            print()
            time.sleep(1)
            leave_dungeon()


    elif reply == '2':
            print('You stare at the vampires. Thats very rude actually.')
            time.sleep(2)
            print()
            print('"You shouldnt have disturbed us. We are very hungry."')
            print()
            print('You will roll a dice to determine whether you will survive this encounter or not.')
            time.sleep(5)
            print()
            dice = random.randint(1, 6)
            print('You got a {}'.format(dice))
            print()
            time.sleep(1)
            if dice >= 5:
                    print('Lucky you. They let you go. Be more respectful next time.')
                    print()
                    leave_dungeon()
            elif dice >= 3:
                    print('They are not sure what to do with you. Do you have any friends to protect you?')
                    time.sleep(1)
                    if len(friends) > 0:
                            print('Your friend {} steps forward and speaks to the vampire sisters in a foreign language.'.format(friends[0]))
                            print()
                            print('They dont seem happy but they let you go.')
                            print()
                            leave_dungeon()
                    else:
                            print('You are on your own.')
                            time.sleep(2)
                            vamps_death()
            else:
                    print('Unlucky.')
                    print()
                    time.sleep(2)
                    print('You try to run.')
                    time.sleep(2)
                    print('You roll the dice again to see if you make it.')
                    time.sleep(5)
                    dice = random.randint(1, 6)
                    print()
                    print('You got a {}'.format(dice))
                    print()
                    time.sleep(2)
                    if dice >= 5:
                        print('You see a small door to your right. You run down the hidden path as fast as you can and escape.')
                    elif dice >= 3:
                        print('Your run for your life but you dont see that there is a hole in the ground.')
                        print()
                        print('You fall for ')
                        for i in range(30):
                            print(i)
                            time.sleep(0.2)
                        print('You fell down 30m and died.')
                        print()
                        print()
                        print()
                        time.sleep(4)
                        print('GAME OVER')
                    else:
                        time.sleep(2)
                        vamps_death()


def start():

    #regime = input("Do you prefer night or day? ")
    name = input("What is your name? ")

    #print("Your name is {} and your are awake at {}." .format(name, regime))
    print()
    print("Welcome to the Dungeon {}!" .format(name))
    print()

    door = input("Do you wish to enter through door 1 or 2? ")
    print("")

    door = get_reply(door)


    if door == '1':
        door_one( name )
    else:
        door_two( name )


start()
end()
