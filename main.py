# Written by Garrett H.

import random

# Global Variables
global handSum
global dealerHandSum
global numAces
global chips
global investedChips

# vvvvvvvvvv START OF FUNCTIONS vvvvvvvvvv

# Draw n cards, recalculate hand sum, peek at your hand

def checkFailure():
    global chips
    print()
    if chips == 0:
        choice = input("You're out of chips! Good try, but not much luck today, try again? y/n --> ").casefold()
        if choice == 'y':
            print("Goodluck, get back in there!")
            chips = 500
        if choice == 'n':
            print("Alright, good games... GUARDS! To the cellar with this one...")
            exit()

# Function to draw cards for the player
def draw(n):
    global handSum

    # Checking if the deck is empty before we draw
    if len(deckClone) <= 0:
        print("You ran out of cards... Bye.")
        exit()

    for i in range(n):
        randomCard = random.choice(deckClone)
        deckClone.remove(randomCard)
        hand.append(randomCard)

    handSum = sum(card_values[card.value] for card in hand)

    # Check for Aces and add to numAces
    global numAces
    numAces = 0

    # Tracks the number of aces in hand
    for i in range(len(hand)):
        if hand[i].value == "Ace":
            numAces = numAces + 1

    # If handSum is greater than 21, check for Aces and turn them from 11 to 1. Subtract 10 from handSum and remove 1 from numAces.
    for i in range(numAces):
        if handSum > 21 and numAces > 0:
            numAces = numAces - 1 
            handSum = handSum - 10

    peek()

# Function to draw cards for the dealer
def dealerDraw(n):
    global dealerHandSum

    # Checking if the deck is empty before the dealer draws
    if len(deckClone) <= 0:
        print("This is really awkward, but the dealer left his deck at home. The house is fresh out of decks too, so I guess the game is off?")
        exit()

    for i in range(n):
        randomCard = random.choice(deckClone)
        deckClone.remove(randomCard)
        dealerHand.append(randomCard)    

    dealerHandSum = sum(card_values[card.value] for card in dealerHand)

     # Check for Aces and add to numAces
    global numAces
    numAces = 0

    # Tracks the number of aces in hand
    for i in range(len(dealerHand)):
        if dealerHand[i].value == "Ace":
            numAces = numAces + 1

    # If handSum is greater than 21, check for Aces and turn them from 11 to 1. Subtract 10 from handSum and remove 1 from numAces.
    for i in range(numAces):
        if dealerHandSum > 21 and numAces > 0:
            numAces = numAces - 1 
            dealerHandSum = dealerHandSum - 10

# Show your cards and sum
def peek():
    print("In hand you have the following cards:", hand)
    print("The sum for your cards in hand is:", handSum)
     
# Hit or stand?
def hos():
     looping = True
     while looping:
        print()
        choice = input("Hit or Stand...? --> ").casefold()
        if choice == 'hit':
            draw(1)
            if handSum > 21:
                print("Busted!")
                looping = False
        elif choice == 'stand':
            looping = False
        else:
            print("Hit or Stand!")

# Handles winning or losing
def roundFinish():
    global dealerHandSum
    global handSum
    global chips
    global investedChips

    print()

    # Dealer time 2
    while dealerHandSum < 17:
        dealerDraw(1)

    print("The dealer's hand is", dealerHand, "and the sum of their cards is", dealerHandSum)

# If the player busts, they lose. If the player and the dealer both bust, the player wins 1x their bet.
    if handSum > 21:
        if dealerHandSum > 21 and handSum > 21:
            print("You and the dealer both bust, you get your bet back.")
            chips += investedChips
            return
        print("You busted and the dealer didn't! You lose your bet!")
        checkFailure()
        return

# The dealer bust, the player wins 2x their bet
    if dealerHandSum > 21:
        print("The dealer busts! You win your bet back +", investedChips, "!")
        chips += investedChips * 2
        return

# The player and dealer tied, the player wins 1x their bet.
    if dealerHandSum == handSum:
        print("You and the dealer tied, you get your bet back")
        chips += investedChips
        return

# The player lost to the dealer, the player is returned nothing.
    if dealerHandSum > handSum:
        print("You lose this round and your bet!")
        checkFailure()
        return

# The player beats the dealer, the player wins 2x their bet. If the player ended on a blackjack, they win 2.5x their bet.
    if dealerHandSum < handSum and handSum <= 21:
        if handSum == 21:
            print("You win with a blackjack and get +", int(investedChips * 1.5), "!")
            chips += investedChips * 2.5
            return
        print("You win this round and get +", investedChips, "!")
        chips += int(investedChips * 2)
        return

# ^^^^^^^^^^ END OF FUNCTIONS ^^^^^^^^^^

# Creating the base deck of cards
class Card:
    def __init__(self, value, color,):
        self.value = value
        self.color = color
    
    def __repr__(self):
            return f"{self.value} of {self.color}"

# colors and values allow for the deck list to initialize with one of each card
colors = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
values = ['Ace'] + [str(n) for n in range(2,11)] + ['Jack', 'Queen', 'King']

# initializing the deck
deck = [Card(value, color) for value in values for color in colors]

# deckClone is used rather than deck so we can remove cards, will be important to reset deckClone at the end of the round
deckClone = deck.copy()

# Fade in from black, Blackjack!

chips = 500

print("Welcome to Blackjack! If you get 3000 chips, you win!")

# Looping until the player has >3000 chips
while chips < 3000 and chips != 0:

# Reset the hands and shuffle the cards back into the deck.

    # Readying the hands and the deck
    hand = []
    dealerHand = []
    deckClone = deck.copy()

    print()
    '''
    If we're playing until success, then add this back and remove the uncommented print line below
    if(chips == 0):
        print("We see that you ran out of chips, but we play till success! We've given you 50 chips on the house.")
        chips = 50
    else:
        print("-- You have,", chips, "chips!")
    '''
    print("-- You have,", chips, "chips!")
    

# Take the bet from the player
    while True:
        tempChips = chips
        bet = input("Place your bet! {50, 100, 250, 500, 1000, 1500} --> ")
        try:
            investedChips = int(bet)
        except ValueError:
            print("Make sure to enter an integer! Try that again for me...")
            continue

        if investedChips in (50, 100, 250, 500, 1000, 1500):
            tempChips -= investedChips
            if tempChips < 0:
                print("Your bet is invalid! Choose again.")
            else:
                print("Your placed bet is", investedChips, "chips.")
                print()
                chips -= investedChips
                break
        else:
            print("Invalid bet! Please choose 50, 100, 250, 500, 1000, 1500.")

# Assign value to cards and calculate the value of the cards in hand
    card_values = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10}
    for n in range(2, 11):
        card_values[str(n)] = n

    handSum = sum(card_values[card.value] for card in hand)
    dealerHandSum = sum(card_values[card.value] for card in dealerHand)

# Dealer 1: Take two cards from the deckClone, reveal one. 
    dealerDraw(2)
    print("The dealer has a(n)", dealerHand[0], "face up, and a card face down.")

# Player 1: Take two cards from the deckClone, remove them and put them in hand. 
    draw(2)

# Hit or Stand?
    hos()

# Handle the end of the round
    roundFinish()

# if they're free and have >=3000 chips, they win!
if chips >= 3000:
    print("The doors unlock and you're free... Go on, you earned this.")

if chips <= 0:
    print("Well if you're out of chips, you can't play. But we also can't let you leave unless you win, so you're going to the cellar with the other losers.")