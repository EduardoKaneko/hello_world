import random

money = 100

# For example, in games of chance that involve rolling dice, you should print out the result of those dice rolls. 
# You should also print whether the player won or lost the game, and how much money they won or lost.

# Write your game of chance functions here
def flip_coin(guess, bet):
    money = 100
    num = random.randint(1, 2)
    if (guess == "Tails" and num == 2) or (guess == "Heads" and num == 1):
        bet = bet * 2
        money = money + bet
        return "You won: " + str(bet) + "." + "You now have: " + str(money)
    else:
        bet = bet/2 
        money = money - bet
    return "You lost: " + str(-bet)+ "." + "You now have: " + str(money)

print(flip_coin("Tails", 20))






# Call your game of chance functions here
