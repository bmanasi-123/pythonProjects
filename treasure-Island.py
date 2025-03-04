#treasure-Island

print('''
    Welcome to TREASURE ISLAND !!
Your Mission is to find the Treasure 
        Are You Ready 
''')

start = input("Type play to start\n|-->")
if start:
    choice = input('''
    You're at a cross road , where do you want to go ?
                Type left or right 
    |-->''')
    if choice.lower() == 'left':
        choice = input('''
    You've came to a lake , there is a island middle of the lake ?
        Type 'wait' to wait for a boat or 'swim' to swim across 
    |-->''')
        if choice.lower() == 'wait':
            choice = input('''
    You've arrived at the island unharmed . There is a house having 3 doors.
        One Red , One Blue , One yellow ; Type the colour to choose
    |-->''')
            if choice.lower() == 'yellow':
                print('You wins the Treasure !!')
            elif choice.lower() == 'red':
                print('The room was full of fire . Game Over !!')
            elif choice.lower() == 'blue':
                print("There was a hungry Beast . Game Over !!")
            else:
                print("You choose a door that doesn't exist . Game Over !!")
        else:
            print("Ooops! You have attacked by a sea creature, Game Over !!")
    else:
        print("Ooops! You fall in to  a whole, Game Over !!")