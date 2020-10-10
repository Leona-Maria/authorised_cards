#TASK 3 - CARD GAME

import time
import random
import csv

p1deck = []
p2deck = []

#Allow players to enter details, which are authenitcated, to ensure that they are authorised players.

P1username = "Louise"
P2username = "Louis"
P1password = "password123"
P2password = "password321"

P1enteredName = input("PLAYER 1 enter your username: ")
while P1enteredName != P1username:
    print("Username not found. This game is for authorised players only.")
    P1enteredName = input("PLAYER 1 enter your username: ")
if P1enteredName == P1username:
    P1enteredPass = input("Enter your password: ")
    while P1enteredPass != P1password:
        print("Wrong password.")
        P1enteredPass = input("PLAYER 1 enter your password: ")
    if P1enteredPass == P1password:
        print("Hello Louise.")
        print(" ")
        P2enteredName = input("PLAYER 2 enter your username: ")
        while P2enteredName != P2username:
            print("Username not found. This game is for authorised players only.")
            P2enteredName = input("PLAYER 2 enter your username: ")
        if P2enteredName == P2username:
            P2enteredPass = input("Enter your password: ")
            while P2enteredPass != P2password:
                print("Wrong password.")
                P2enteredPass = input("PLAYER 2 enter your password: ")
            if P2enteredPass == P2password:
                print("Hello Louis.")

#Shuffles 30 cards in a deck.

time.sleep(2)
print("\nThere are 30 cards in a deck.")
time.sleep(2)
print("\nEach card has a colour - either red (R), black (B), or yellow (Y).")
time.sleep(3)
print("\nEach card has a number from one to ten for each colour.")
time.sleep(3)
print("\nEach card is unique.")
time.sleep(2)
print("\nPlayer 1 will take the top card from the deck.")
time.sleep(3)
print("\nPlayer 2 will take the next card from the deck.")
time.sleep(3)
print("\nIf both players have a card of the same colour, the player with the highest number wins.")
time.sleep(4)
print("\nIf both players have cards with different colours, then the rules are as follows:")
time.sleep(4)
print("Red beats black.")
time.sleep(1)
print("Yellow beats red.")
time.sleep(1)
print("Black beats yellow.")
time.sleep(2)
print("\nThe winner of each round keeps both cards.")
time.sleep(3)
print("\nThe game ends when there are no cards left in the deck.")
time.sleep(4)
print("\nThe winner of the game is the person with the most cards.")
time.sleep(4)
print("\nLet the game begin.")
time.sleep(3)
print("\n*shuffling cards*\n")
time.sleep(4)

cards = ['R01','R02','R03','R04','R05','R06','R07','R08','R09','R10','B01','B02','B03','B04','B05','B06','B07','B08','B09','B10','Y01','Y02','Y03','Y04','Y05','Y06','Y07','Y08','Y09','Y10']
random.shuffle(cards)

#Allows each player to take a card from the top of the deck.

while len(cards) != 0:

    print("PLAYER 1 has taken",cards[0],"from the deck.")
    time.sleep(3)
    print("PLAYER 2 has taken the next card from the deck...")
    time.sleep(4)
    print("It is",cards[1],".")
    time.sleep(1)

#Calculates the winner and allocates both cards to the winner. Play continues until there are no cards left in the deck.

    p1card = cards[0]
    p2card = cards[1]
    p1colour = p1card[0]
    p2colour = p2card[0]

    if p1colour == p2colour:
        p1num = str(p1card[1]+p1card[2])
        p2num = str(p2card[1]+p2card[2])
        if p1num < p2num:
            print("PLAYER 2 WINS\n")
            p2deck.append(p1card)
            p2deck.append(p2card)
        elif p1num > p2num:
            print("PLAYER 1 WINS\n")
            p1deck.append(p1card)
            p1deck.append(p2card)
    if p1colour != p2colour:
        if p1colour == "B":
            if p2colour == "R":
                print("PLAYER 2 WINS\n")
                p2deck.append(p1card)
                p2deck.append(p2card)
            else:
                print("PLAYER 1 WINS\n")
                p1deck.append(p1card)
                p1deck.append(p2card)
        elif p1colour == "R":
            if p2colour == "B":
                print("PLAYER 1 WINS\n")
                p1deck.append(p1card)
                p1deck.append(p2card)
            else:
                print("PLAYER 2 WINS\n")
                p2deck.append(p1card)
                p2deck.append(p2card)
        elif p1colour == "Y":
            if p2colour == "B":
                print("PLAYER 2 WINS\n")
                p2deck.append(p1card)
                p2deck.append(p2card)
            else:
                print("PLAYER 1 WINS\n")
                p1deck.append(p1card)
                p1deck.append(p2card)
        else:
            print("ERROR")

    cards.remove(p1card)
    cards.remove(p2card)
    time.sleep(2)

#Displays which player wins (the player with the most cards).
#Lists all cards held by the winning player.
#Stores the name and quantity of cards of the winning player in an external file.

if len(cards) == 0:
    print("There are no more cards left in the deck.\n")
    time.sleep(2)
    print("It's time to see who has won...\n")
    time.sleep(2)
    print("*counting cards*\n")
    time.sleep(2)
    p1cards = len(p1deck)
    p2cards = len(p2deck)
    if p1cards < p2cards:
        print("With",p2cards,"cards, PLAYER 2 is the winner!")
        print(p2deck)
        f = open("Most Cards.csv","a+")
        p2cards = str(p2cards)
        f.write(P2username)
        f.write(",")
        f.write(p2cards)
        f.write("\n")
        f.close()    
    elif p1cards > p2cards:
        print("With",p1cards,"cards, PLAYER 1 is the winner!")
        print(p1deck)
        f = open("Most Cards.csv","a+")
        p1cards = str(p1cards)
        f.write(P1username)
        f.write(",")
        f.write(p1cards)
        f.write("\n")
        f.close()
    f = open("Most Cards.csv","a+")
    for i in range(4):
        f.write("")
        f.write(",")
        f.write("")
        f.write("\n")
    f.close()
 
#Displays the name and quantity of cards of the 5 players with the highest quantity of cards from the external file.
print("-----TOP 5 SCORES-----")
r = csv.reader(open("Most Cards.csv"))
scores = list(r)

from operator import itemgetter
scores = sorted(scores, key = itemgetter(1), reverse = True)
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[4])

