# miguel jusino
# this is the user that is in all chapters
class adventurer:
    def __init__(self, coins, xp, wood, food):
        self.coins = coins
        self.xp = xp
        self.wood = wood
        self.food = food
    # this is the shortcut for all user inventory on progression
    def uinfo(self):
        print("You have ", self.coins, " coins!")
        print("You have ", self.xp, " XP!")
        print("You have ", self.wood, " Wood!")
        print("You have ", self.food, " Food!")


# global mycoins
# global myxp
# global mywood
# global myfood
# global user

# this is the start up inventory
mycoins = 5
myxp = 0
mywood = 0
myfood = 4
# this helps us define all of this into a simple word
user = adventurer(mycoins, myxp, mywood, myfood)
