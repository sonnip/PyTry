import time
import random

def get_reply( check ):
    while check != '1' and check != '2':
        check = input("You are not so good with numbers are you? 1 or 2? ")
    return check

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
    print('You try to run.')
    time.sleep(2)
    print()
    print('Fool. They are much faster than you.')
    print()
    print()
    print()
    time.sleep(1)
    print('GAME OVER')




#regime = input("Do you prefer night or day? ")
name = input("What is your name? ")

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
            print()
            new_friend('Edward')
            print_friends()
            print(' "Come I want to introduce you to my friends."')
            time.sleep(2)
            print()
            print()
            door = '2'

        else:
            door = '2'
            print('You turn around and run through a random door.')

if door == '2':
    print('You enter into a dimly lit room.')
    print()
    print('When your eyes adjust to the darkness you suddenly see that there is three vampires staring at you.')
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
            print('The vampires appreciate your respectful introduction.')
            print()
            print('The tallest of the vampires steps forward')
            print('"Welcome {}. My name is Roberta and these are my sisters Tavia and Maitane."' .format(name))
            new_friend('Roberta')
            new_friend('Tavia')
            new_friend('Maitane')
            print_friends()

    elif reply == '2':
            print('You stare at the vampires. Thats very rude actually.')
            time.sleep(2)
            print()
            print('"You shouldnt have disturbed us. We are very hungry."')
            print()
            print('You will roll a dice to determine whether you survive this encounter or not.')
            time.sleep(5)
            print()
            dice = random.randint(1, 6)
            print('You got a {}'.format(dice))
            print()
            time.sleep(1)
            if dice >= 5:
                    print('Lucky you. They let you leave. Be more respectful next time.')
            elif dice >= 3:
                    print('They are not sure what to do with you. Do you have any friends to protect you?')
                    time.sleep(1)
                    if len(friends) > 0:
                            print('Your friend {} steps forward and speaks to the vampire sisters in a foreign language.'.format(friends[0]))
                            print('They dont seem happy but they let you leave.')
                    else:
                            print('You are on your own.')
                            time.sleep(2)
                            vamps_death()
            else:
                    print('Unlucky.')
                    time.sleep(2)
                    vamps_death()


