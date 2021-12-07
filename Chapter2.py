# miguel jusino


#
def ch2(user):
    print("While walking home after the party you see troll police.they accuse you of murder")
    # options
    print("A - stay ")
    print("B - run ")
    choose = input("Choose Option A or B. ")
    # reward if you choose "A" and "B
    if choose.upper().strip() == 'A':
        print("on to the next level ")
        user.coins += 2
        user.xp -= 2
        user.wood = 0
        user.food = 0
    else:
        print("You tried to escape but failed ")
        print("on to the next level ")
        user.coins -= 2
        user.xp += 3
        user.wood = 0
        user.food = 0

    user.uinfo()
    print("\n\n\n")
