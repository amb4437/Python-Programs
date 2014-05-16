import random

class Card(object):

  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

  SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')

  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    
  def __str__(self):
    if self.rank == 1:
      rank = 'Ace'
    elif self.rank == 11:
      rank = 'Jack'
    elif self.rank == 12:
      rank = 'Queen'
    elif self.rank == 13:
      rank = 'King'
    else:
      rank = self.rank
    return str(rank) + ' of ' + self.suit.lower()
    
    
class Deck(object):
  
  def __init__(self):
    self._cards= []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        c = Card(rank, suit)
        self._cards.append(c)
        
  def shuffle(self):
    random.shuffle(self._cards)
    
  def deal(self):
    if len(self) == 0:
      return None
    else:
      return self._cards.pop(0)
      
  def __len__(self):
    return len(self._cards)
    
  def __str__(self):
    result = ''
    for c in self._cards:
      result = result + str(c) + '\n'
    return result
  
  

class Player(object):
  ##This class represents a player in a blackjack game
  def __init__(self, cards):
    self._cards = cards

  def __str__(self):
    result = ", ".join(map(str, self._cards))
    result +="\n " + str(self.getPoints()) + " points"
    return result

  def hit(self, card):
    self._cards.append(card)

  def getPoints(self):
    count = 0
    for card in self._cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    for card in self._cards:
      if count<= 21:
        break
      elif card.rank == 1:
        count -= 10

    return count

  def hasBlackjack(self):
    return len(self._cards) == 2 and self.getPoints() == 21


class Dealer(Player):

  def __init__(self, cards):
    Player.__init__(self, cards)
    self._showOneCard= True

  def __str__(self):
    if self._showOneCard:
      return str(self._cards[0])
    else:
      return Player.__str__(self)

  def hit(self, deck):
    self._showOneCard = False
    while self.getPoints() < 17:
      self._cards.append(deck.deal())

  def getPoints(self):
    count = 0
    for card in self._cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    for card in self._cards:
      if count<= 21:
        break
      elif card.rank == 1:
        count -= 10

    return count



class Blackjack(object):

  def __init__(self):
    self._deck = Deck()
    self._deck.shuffle()
    self._player = Player([self._deck.deal(), self._deck.deal()])
    self._dealer = Dealer([self._deck.deal(), self._deck.deal()])

  def play(self):
    print "Player:\n", self._player
    print "Dealer:\n", self._dealer

    while True:
      choice = raw_input("Do you want a hit? [y/n]: ")
      if choice in ("Y", "y"):
        self._player.hit(self._deck.deal())
        points= self._player.getPoints()
        print "Player:\n", self._player
        if points >= 21:
          break
      else:
        break
    playerPoints= self._player.getPoints()
    if playerPoints> 21:
      print "You bust and lose"
    else:
      self._dealer.hit(self._deck)
      print "Dealer:\n", self._dealer
      dealerPoints = self._dealer.getPoints()
    
      if dealerPoints > 21:
        print "Dealer busts and you win"
      elif dealerPoints> playerPoints:
        print "Dealer wins"
      elif dealerPoints < playerPoints and playerPoints <= 21:
        print "You win"
      elif dealerPoints == playerPoints:
        if self._player.hasBlackjack() and not self._dealer.hasBlackjack():
          print "You win"
      elif not self._player.hasBlackjack() and self._dealer.hasBlackjack():
        print "Dealer wins"
      else:
        print "There is a tie"

def main():
  game = Blackjack()
  game.play()

main()
