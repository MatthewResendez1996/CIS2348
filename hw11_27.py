#Matthew James Resendez
#1431242
players = {}
mylist = []

def sortDictKeys():
    mylist = sorted(players.keys())
    return mylist

def outputRoster():
    mylist = sortDictKeys()
    print("ROSTER")
    for i in mylist:
        print("Jersey number: " + str(i)
        + ", Rating: " + str(players[i]))

def addPlayer():
    print("Enter a new player's jersey number:")
    jerseynum = int(input())
    while((jerseynum < 0) or (jerseynum > 99)):
        print("Invalid Jersey Number! Please " +
        "enter again!")
        print("Enter a new player's jersey number:")
        jerseynum = int(input())
    print("Enter the player's rating:")
    prating = int(input())
    while((prating < 1) or (prating > 9)):
        print("Invalid Rating! Please enter again!")
        print("Enter the player's rating:")
        prating = int(input())
    players.update({jerseynum : prating})
def removePlayer():
    print("Enter a jersey number:")
    jerseynum = int(input())
    while((jerseynum < 0) or (jerseynum > 99)):
        print("Invalid Jersey Number! Please " +
        "enter again!")
        print("Enter a jersey number:")
        jerseynum = int(input())
    if jerseynum in players.keys():
        del players[jerseynum]
def updatePlayer():
    print("Enter a jersey number:")
    jerseynum = int(input())
    while((jerseynum < 0) or (jerseynum > 99)):
        print("Invalid Jersey Number! Please " +
        "enter again!")
        print("Enter a jersey number:")
        jerseynum = int(input())
    print("Enter a new rating for player:")
    prating = int(input())
    while((prating < 1) or (prating > 9)):
        print("Invalid Rating! Please enter again!")
        print("Enter a new rating for player:")
        prating = int(input())
    players[jerseynum] = prating
def outputPlayerAboveRating():
    print("Enter a rating:")
    rating = int(input())
    while((prating < 1) or (prating > 9)):
        print("Invalid Rating! Please enter again!")
        print("Enter a rating:")
        rating = int(input())
    print("ABOVE 4")
    mylist = sortDictKeys()
    for i in mylist:
        if(players[i] > rating):
            print("Jersey number: " + str(i)
            + ", Rating: " + str(players[i]))
for i in range(1, 6):
    print("Enter player " + str(i) + "'s jersey number:")
    jerseynum = int(input())
    while((jerseynum < 0) or (jerseynum > 99)):
        print("Invalid Jersey Number! Please " +
        "enter again!")
        print("Enter player " + str(i)
        + "'s jersey number:")
        jerseynum = int(input())
    print("Enter player " + str(i) + "'s rating:")
    prating = int(input())
    while((prating < 1) or (prating > 9)):
        print("Invalid Rating! Please enter again!")
        print("Enter player " + str(i) + "'s rating:")
        prating = int(input())
    print()
    players[jerseynum] = prating
outputRoster()
print()
while(True):
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    print("Choose an option:")
    user_choice = input()
    if(user_choice == 'a'):
        addPlayer()
    elif(user_choice == 'd'):
        removePlayer()
    elif(user_choice == 'u'):
        updatePlayer()
    elif(user_choice == 'r'):
        outputPlayerAboveRating()
    elif(user_choice == 'o'):
        outputRoster()
    elif(user_choice == 'q'):
        break
    print()
