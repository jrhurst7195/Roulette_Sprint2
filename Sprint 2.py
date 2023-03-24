#Jonathan Hurst
#Roullete wheel game
#lowercase help https://www.w3schools.com/python/ref_string_lower.asp
#My friend Aiden Folds on some of the Def()

x = 1
if x == 0:
    hello_world()
if not x:
    print("")
#couldn't figure out how to incorporate not ^^^
    

import random

print("Welcome to the FGCU Casino!!")
print("I see you are wanting to play some roulette.")
print("Let me explain the rules to you real quick.")
print("The wheel goes from the number 0 to 36.")
print("Around half of the values are black while the others are red.")
print("You can bet on an exact number, whether the number will", end=" ")
print("be even or odd, and also red or black", end=".")
#print w end ^^^
print("If you win you double your bet but if you lose your bet it is - whatever you bet from balance!")
print("We are starting you out at", 50 * 2, "chips on the house but use it wisely.")
                               # *  ^^^

def get_bet():
    while True:
        bet = input("What would you like to bet on? (even, odd, red, black, number between 1 and 36): ")
        if bet in ["even", "odd", "red", "black"] or (bet.isdigit() and 0 <= int(bet) <= 36):
            return bet
        else:
            print("Invalid bet. Please try again.")

def get_bet_amount(balance):
    while True:
        bet_amount = int(input("How much would you like to bet? (1-" + str(balance) + "): "))
        if 1 <= bet_amount <= balance:
            return bet_amount
        else:
            print("Invalid bet amount. Please try again.")

def spin_wheel():
    return random.randint(0, 36)

def get_outcome(bet, result):
    if bet == "even":
        if result == 0:
            return "lose"
        elif result % 2 == 0:
            return "win"
        else:
            return "lose"
    elif bet == "odd":
        if result == 0:
            return "lose"
        elif result % 2 == 1:
            return "win"
        else:
            return "lose"
    elif bet == "red":
        if result == 0:
            return "lose"
        elif (result <= 10 or 19 < result <= 28):
            return "lose"
        else:
            return "win"
    elif bet == "black":
        if result == 0:
            return "lose"
        elif (11 <= result <= 18 or 29 <= result <= 36):
            return "lose"
        else:
            return "win"
    elif bet == bet:
        if result != bet:
            return "lose"
        else:
            return "win"
    else:
        if result == bet:
            return "win"
        else:
            return "lose"
    
#if / else's   ^^^^

def play_game(balance):
    while True:
        print("You have", balance, "chips.")
        bet = get_bet()
        bet_amount = get_bet_amount(balance)
        result = spin_wheel()
        for wheel_spin_effect in range(1,37):
            #for in range ^^^
            print(wheel_spin_effect)
        print("The wheel landed on", result)
        outcome = get_outcome(bet, result)
        if outcome == "win":
            print(" Wow!" * 2, "You won", bet_amount, "chips.")
            #str * ^^^
            balance += bet_amount
        else:
            print("Sorry, you lost", bet_amount, "chips.")
            balance -= bet_amount
        if balance == 0:
            print("Game over. You ran out of money.")
            play_again = input("Would you like to buy in for another 100 chips? (y/n) ")
            if play_again.lower() != "y":
                #(!=) ^^
                print("Thank you for playing Roulette! Your final balance is", balance, "chips.", sep=' ')
                # print w sep=' ' ^^^
                break
            else:
                balance += 10 ** 2
                # ** ^^^
        else:
            continue

def main():
    balance = int(10000 / 100)
    # / ^^^
    while True:
        play_game(balance)
        play_again = input("Did you have a postive experience here at FGCU Casino? (y/n) ")
        if play_again.lower() != "y":
            print("Sorry to hear that.")
            break
        else:
            print("Great!")
            break
    print("Goodbye!" + " We hope you play again!")

if __name__ == "__main__":
    main()
