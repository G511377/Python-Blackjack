import random

# Global Variables
global handSum
global dealerHandSum
global numAces

# vvv Funky Unc Functions vvv

# Draw n cards, recalculate hand sum, peek at your hand
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

def roundFinish():
    global dealerHandSum
    global handSum

    # Dealer time 2
    while dealerHandSum < 17:
        dealerDraw(1)

    print("The dealer's hand is", dealerHand, "and the sum of his cards is", dealerHandSum)

# If the player busts, they lose. If the player and the dealer both bust, the player wins 1x their bet.
    if handSum > 21:
        if dealerHandSum > 21 and handSum > 21:
            print("You and the dealer both bust, you get your bet back.")
            return
        print("You busted and the dealer didn't! You lose your bet!")
        return

# The dealer bust, the player wins 2x their bet
    if dealerHandSum > 21:
        print("The dealer busts! You win your bet back +, winnings, !")
        return

# The player and dealer tied, the player wins 1x their bet.
    if dealerHandSum == handSum:
        print("You and the dealer tied, you get your bet back")
        return

# The player lost to the dealer, the player is returned nothing.
    if dealerHandSum > handSum:
        print("You lose this round and your bet!")
        return

# The player beats the dealer, the player wins 2x their bet. If the player ended on a blackjack, they win 2.5x their bet.
    if dealerHandSum < handSum and handSum <= 21:
        if handSum == 21:
            print("You win with a blackjack and get +, winnings ,!")
            return
        print("You win this round and get +, winnings ,!")
        return

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
hand = []
dealerHand = []

# Assign value to cards and calculate the value of the cards in hand
card_values = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10}
for n in range(2, 11):
     card_values[str(n)] = n

handSum = sum(card_values[card.value] for card in hand)
dealerHandSum = sum(card_values[card.value] for card in dealerHand)

# Dealer 1: Take two cards from the deckClone, reveal one. 
dealerDraw(2)
print("The dealer has a(n)", dealerHand[0], "face up, and a card face down.")
print(dealerHandSum)

# Player 1: Take two cards from the deckClone, remove them and put them in hand. 
draw(2)

# Hit or Stand?
hos()

# If busted -> see if dealer busts -> if he does, get your chips back OR if he doesn't, you lose your chips. 
# If stand, see if dealer beats you -> if he does, lose your chips. OR if he busts or does not, win chips + interest

roundFinish()