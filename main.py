##Black Jack One Hit Mode
## started 1/8/20 
import random ## for adding a deck shuffler
##Starting deck to always have a constant deck and having no aces for simplicity sake        Update: took out 1's and put in aces and face cards
player1 =[]
dealer = []
while True:
    startingDeck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","K","K","K","K","Q","Q","Q","Q","J","J","J","J","a","a","a","a"]
    options = ["2","3","4","5","6","7","8","9","10"]
    deck = startingDeck
    currentDeck = []
    
    def shuffleDeck(deck): 
        shufflingDeck = []
        for x in range(0,len(startingDeck)):
            shufflingDeck.insert(random.randint(0,x),a[0])
            deck.pop(0)
        return(shufflingDeck)
    #starts the hands off different for each play by simulating taking the top card and putting in in the players/computers hand
    def startingHands(currentDeck):
        hand = []
        for x in range(0, 2):
            hand.append(currentDeck[-1]) ## gets the item from the back of the list and puts it in the list
            currentDeck.pop(-1)
        return(hand)
    ### sets the current deck to a newly shuffled deck so that the deck is new everytime Adding the condition that the list can not have more than 5 cards makes a new deck
    if len(currentDeck) < 5:
        currentDeck = shuffleDeck(deck)    
    if len(player1) == 0:
        player1 = startingHands(currentDeck)
        dealer = startingHands(currentDeck)
    def countingCards(a,options):
        a.sort() 
        total = 0 
        for cards in a:
            if cards in options:
                total += int(cards)
            else:
                if cards == "K" or cards == "Q" or cards == "J":
                    total += 10
                else:
                    if total + 11 > 21:
                        total += 1
                    else:
                        total += 11
        return(total)
    print("Your hand is " + str(player1))
    print("The dealers face up card is " + str(dealer[0]))
    hitStay = input("Do you want to Hit or stay?  ")
    if hitStay.lower() == 'hit':
        player1.append(currentDeck[-1])
        currentDeck.pop(-1)
        
    elif hitStay.lower() == "stay":
        playerTotal = countingCards(player1,options)
        dealerTotal = countingCards(dealer,options)
        while dealerTotal < 17: 
                dealer.append(currentDeck[-1])
                currentDeck.pop(-1)
                dealerTotal = countingCards(dealer,options)
         ## The ending of the game
        if playerTotal == dealerTotal or playerTotal > 21 and dealerTotal > 21:
            print("You had " + str(playerTotal) + " and the dealer had " + str(dealerTotal) + ". There is a tie")
        elif playerTotal == 21 or playerTotal > dealerTotal and playerTotal <= 21 or dealerTotal > 21 :
            print("You had " + str(playerTotal) + " and the dealer had " + str(dealerTotal) + ". You win. ")
        elif dealerTotal == 21 or dealerTotal > playerTotal or playerTotal > 21:
            print("You had " + str(playerTotal) + " and the dealer had " + str(dealerTotal) + ". You lost. ")
            #then sets the players hand to be empty so the cards wouldn't be infinite
        player1 = []
        dealer = []
        #making the ability to quit the game
        anotherGame = input(str("Do you want to play another game? "))
        if anotherGame.lower() == "no":
            break