# miguel jusino
def ch3(user):
    print("police are taking you to the king! ")
    #  options
    print("A - attempt to get out of handcuffs ")
    print("B - Try asking to let you go! ")
    choose = input("Choose Option A or B. ")
    # rewards if chosen "A" or "B"
    if choose.upper().strip() == 'A':
        print("The handcuffs were too strong you were seen trying to escape and was rushed to the king ")
        user.coins += 0
        user.xp += 3
        user.wood = 0
        user.food = 0
    else:
        print("The officer said no and you were taken to the king ")
        user.coins += 2
        user.xp += 0
        user.wood = 0
        user.food = 0

    print("The king received information on what you did and kicks you out of Troll land from a portal ")

    user.uinfo()
    print("\n\n\n")
