# miguel jusino
def ch4(user):
    print("The portal took you to an empty cave ")

    print("you find an exit and see that you are in the human world ")
    # option and rewards you enter "food" or other word
    food = input("Do you want to get food or resources first? ")
    if food.lower().strip() == 'food':
        print("you gained 10 food ")
        user.food += 10
    else:
        print("you gained 10 resources\n\n\n")
        user.wood += 10
