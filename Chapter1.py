# miguel jusino
# main player and all that I want to go with him through chapters
from user import user
from Chapter2 import ch2
from Chapter3 import ch3
from Chapter4 import ch4
from Chapter5 import ch5


def ch1(user):
    # input("Press enter to start Chapter 1!")

    print("You are dancing at a party. ")

    dance = input("Do you want to keep dancing? yes/no? ")
    # dance loop that is only allowed 3 entry
    dance_count = 0
    while dance.lower().strip() == "yes" and dance_count < 3:
        dance_count += 1
        print("more coins!")
        user.coins += 5
        user.xp += 3
        user.wood = 0
        user.food = 0
        user.uinfo()

        dance = input("Continue dancing? yes/no? ")

    print("on to the next level\n\n\n")
    ch2(user)
    ch3(user)
    ch4(user)
    ch5(user)


ch1(user)
