from classes.player import Deck, Player, Card
import modules.menu, time

def runRound():
    deck = Deck()
    deck.shuffleDeck()
    dealer = Player(True)
    user = Player(False)

    initCycle(deck, dealer, user)
    if hitCycle(deck, user) == True:
        dealerCycle(deck, dealer)
    endCycle(deck, dealer, user)

def initCycle(deck, dealer, user):
    cardQueue = [deck.getTopCard(), deck.getTopCard()]
    cardQueue[0].isFaceUp = False
    dealer.giveCards(cardQueue)

    cardQueue2 = [deck.getTopCard(), deck.getTopCard()]
    user.giveCards(cardQueue2)

    print('Dealer\'s cards')
    printCards(dealer.cards)
    print('Your cards')
    printCards(user.cards)
    #print('')

def hitCycle(deck, user):
    #runs hit() if hit
    return modules.menu.runHitMenu(deck, user)


def hit(deck, player):
    player.giveCards([deck.getTopCard()])
    printCards(player.cards)
    #print(player.getScore())
    
    if player.getScore() > 21:
        print('Bust!')
        return False
    else:
        return True


def dealerCycle(deck, dealer):
    dealer.cards[0].isFaceUp = True
    print('Dealer\'s hand')
    printCards(dealer.cards)
    while dealer.getScore() < 17:
        time.sleep(.8)
        print('Dealer hits!')
        hit(deck, dealer)
    time.sleep(.8)
    
def endCycle(deck, dealer, user):
    print('')
    
    if user.getScore() > 21:
        print('You lose')
    elif dealer.getScore() > user.getScore():
        print('You lose.')
    elif dealer.getScore() < user.getScore():
        print('You Win!')
    else:
        print('Draw')
    print('')
    print('Play again?')

'''
@param list of cards
'''
def printCards(cards):
    valueString = ''
    suiteString = ''
    cardTop = ''
    cardBottom = ''
    for i in range(0, len(cards)):

        if cards[i].isFaceUp == False:
            valueString = valueString + u'\u2502' + '  ' + u'\u2502 '
            suiteString = suiteString + u'\u2502' + '  ' + u'\u2502 '
        else:
           
            if str(cards[i].value) != '10':
                valueString = valueString + u'\u2502' + str(cards[i].value) + ' ' + u'\u2502 '
            else:
                valueString = valueString + u'\u2502' + str(cards[i].value) + u'\u2502 '
            


            if cards[i].suite == 0:
                suiteString = suiteString + u'\u2502' + ' ' + u'\u2660' + u'\u2502 '
            elif cards[i].suite == 1:
                suiteString = suiteString + u'\u2502' + ' ' + u'\u2665' + u'\u2502 '
            elif cards[i].suite == 2:
                suiteString = suiteString + u'\u2502' + ' ' + u'\u2666' + u'\u2502 '
            elif cards[i].suite == 3:
                suiteString = suiteString + u'\u2502' + ' ' + u'\u2663' + u'\u2502 '
            else:
                suiteString = suiteString + u'\u2502' + ' x' + u'\u2502 '
            
            #suiteString = suiteString + u'\u2502' + ' ' + str(cards[i].suite) + u'\u2502 '
        cardTop = cardTop + u'\u250c' + u'\u2500' + u'\u2500' + u'\u2510 '
        cardBottom = cardBottom + u'\u2514' + u'\u2500' + u'\u2500' + u'\u2518 '
        
    print(cardTop)
    print(valueString)
    print(suiteString)
    print(cardBottom)
