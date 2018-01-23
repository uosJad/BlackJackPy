from random import shuffle

class Player:

    '''
    @param isDealer Bool, true if is dealer
    '''
    def __init__(self, isDealer):
        self.isDealer = isDealer
        self.cards = []
        

    def giveCards(self, cardListToAdd):
        self.cards.extend(cardListToAdd)
        
    def getScore(self):
        val = 0
        aCount = 0
        for i in range(0, len(self.cards)):
            if self.cards[i].value == 'A':
                aCount += 1
            elif self.cards[i].value == 'K':
                val += 10
            elif self.cards[i].value == 'Q':
                val += 10
            elif self.cards[i].value == 'J':
                val += 10
            else:
                val += int(self.cards[i].value)
        
        for i in range(0, aCount):
            if val + 11 > 21:
                val += 1
            else:
                val += 11

        return val

class Card:

    def __init__(self, value, suite, isFaceUp):
        self.value = value
        self.suite = suite
        self.isFaceUp = isFaceUp

class Deck:

    def __init__(self):
        self.cards = []
        for i in range(1, 14):
            for j in range (0, 4):
                if i == 1:
                    self.cards.append(Card('A', j, True))
                elif i == 11:
                    self.cards.append(Card('J', j, True))
                elif i == 12:
                    self.cards.append(Card('Q', j, True))
                elif i == 13:
                    self.cards.append(Card('K', j, True))
                else:
                    self.cards.append(Card(str(i), j, True))

    def shuffleDeck(self):
        shuffle(self.cards)

    def getTopCard(self):
        return self.cards.pop();
