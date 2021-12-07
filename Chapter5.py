# miguel jusino
def ch5(user):
    print("You see a couple of trees in your way to get back home ")
    # must complete to continue game
    chop = input("You will need to chop them down with your hand. Press R to complete ")
    if chop.lower() == 'r':
        print("Good Job!")
        print("You gained 10 wood")
        user.wood += 10
        user.uinfo()

    # must complete to continue game or fail
    craft = input("You are now home Click W to make bed and food. ")
    if craft.lower() == 'w':
        print("Great!")
        print("you now have a bed and food to eat ")
        user.wood -= 5
        user.food -= 5
        user.uinfo()
    else:
        print("You failed ")
        print("you slept on the cold floor ")

    print("now you must find clues that lead back to troll land")
    input("press enter when done looking for clues ")

    print("You will now explore more to get resources and clues")
    input("when done exploring press enter to gain your new map locations")
    user.xp += 5

    print("end of chapter 5")
