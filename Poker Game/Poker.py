import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('S', 'D', 'H', 'C')

  def __init__ (self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __str__ (self):
    if self.rank == 11:
      rank = 'J'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 14:
      rank = 'A'
    else:
      rank = self.rank
    return str(rank) + self.suit
    
  def __cmp__ (self, other):
    if (self.rank < other.rank):
      return -1
    elif (self.rank > other.rank):
      return 1
    else:
      return 0


## This class forms the initial deck
class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        c = Card (rank, suit)
        self.deck.append (c)

  def shuffle (self):
    random.shuffle (self.deck)

  def __len__ (self):
    return len (self.deck)

  def deal (self):
    if len(self) == 0:
      return None
    else:
      return self.deck.pop(0)

  def __str__ (self):
    result = ''
    for c in self.deck:
      result = result + str(c) + '\n'
    return result

class Poker (object):
  
  def __init__ (self, handsplayed):
    self.deck = Deck()
    self.deck.shuffle()
    self.hands = []
    numCards_in_Hand = 5
    handsplayed= int(handsplayed)
    

    for i in range (handsplayed):
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)
      
  def play (self):
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i], reverse = True, key=lambda c:c.rank)
      hand = ''
      for card in sortedHand:
        hand = hand +  str (card) + ' '
      print ('Hand ' + str(i+1) + ': ' + hand)
    
    total = []
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i], reverse = True, key=lambda c:c.rank)
      
      ### prints if the hand is a royal flush
      pts = self.isRoyal(sortedHand)
      if (pts > 0):
        print ('Hand ' + str(i+1) + ': ' + 'Royal Flush')
        total.append(pts)
        continue
      ### prints if the hand is a straight flush
      pts = self.isStraightFlush(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'Straight Flush')
        total.append(pts)
        continue
      ### prints if the hand is four of a kind
      pts = self.isFour(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'Four of a Kind')
        total.append(pts)
        continue
      ### prints if the hand is a full house
      pts = self.isFull(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'Full House')
        total.append(pts)
        continue
      ### prints if the hand is a flush
      pts = self.isFlush(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'Flush')
        total.append(pts)
        continue
      ### prints if the hand is a straight
      pts = self.isStraight(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'Straight')
        total.append(pts)
        continue
      ### prints if the hand is a three of a kind
      pts = self.isThree(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'Three of a Kind')
        total.append(pts)
        continue
      ### prints if the hand is a two pair
      pts = self.isTwo(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'Two Pair')
        total.append(pts)
        continue
      ### prints if the hand is a one pair
      pts = self.isOne(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'One Pair')
        total.append(pts)
        continue
      ### prints if the hand is a high card
      pts = self.isHigh(sortedHand)
      if (pts > 0):  
        print ('Hand ' + str(i+1) + ': ' + 'High Card')
        total.append(pts)
        continue
      
    win = self.getWinner(total)
    print ('Hand ' + str(win+1) + ' wins.')
   
  ### checks if the hand is a royal flush
  def isRoyal (self, hand):
    if hand[0].suit==hand[1].suit and hand[1].suit==hand[2].suit and hand[2].suit==hand[3].suit and hand[3].suit==hand[4].suit:
      if hand[0].rank-1==hand[1].rank and hand[1].rank-1==hand[2].rank and hand[2].rank-1==hand[3].rank and hand[3].rank-1==hand[4].rank:
        if hand[0].rank == 14:
          return 10 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
        else:
          return 0
      else:
        return 0
    else:
      return 0
  
  ### checks if the hand is a straight flush
  def isStraightFlush (self, hand):
    if hand[0].suit==hand[1].suit and hand[1].suit==hand[2].suit and hand[2].suit==hand[3].suit and hand[3].suit==hand[4].suit:
      if hand[0].rank-1==hand[1].rank and hand[1].rank-1==hand[2].rank and hand[2].rank-1==hand[3].rank and hand[3].rank-1==hand[4].rank:
        return 9 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
      else:
        return 0
    else:
      return 0
  ### checks if the hand is a four of a kind
  def isFour (self, hand):
    if hand[0].rank==hand[3].rank:
      return 8 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    elif hand[1].rank==hand[4].rank:
      return 8 * 13^5 + hand[1].rank * 13^4 + hand[2].rank * 13^3 + hand[3].rank * 13^2 + hand[4].rank * 13 + hand[0].rank
    else:
      return 0
  ### checks if the hand is a full house
  def isFull (self, hand):
    if hand[0].rank==hand[2].rank and hand[3].rank==hand[4].rank:
      return 7 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    elif  hand[0].rank==hand[1].rank and hand[2].rank==hand[4].rank:
      return 7 * 13^5 + hand[2].rank * 13^4 + hand[3].rank * 13^3 + hand[4].rank * 13^2 + hand[0].rank * 13 + hand[1].rank
    else:
      return 0
  ### checks if the hand is a flush
  def isFlush (self, hand):
    if hand[0].suit==hand[1].suit and hand[1].suit==hand[2].suit and hand[2].suit==hand[3].suit and hand[3].suit==hand[4].suit:
      return 6 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    else:
      return 0
  ### checks if the hand is a straight   
  def isStraight (self, hand): 
    if hand[0].rank-1==hand[1].rank and hand[1].rank-1==hand[2].rank and hand[2].rank-1==hand[3].rank and hand[3].rank-1==hand[4].rank:
      return 5 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    else:
      return 0
  ### checks if the hand is a three of a kind    
  def isThree (self, hand): 
    if hand[0].rank==hand[2].rank or hand[1].rank==hand[3].rank or hand[2].rank==hand[4].rank:
      return 4 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    elif hand[1].rank==hand[3].rank:
      return 4 * 13^5 + hand[1].rank * 13^4 + hand[2].rank * 13^3 + hand[3].rank * 13^2 + hand[0].rank * 13 + hand[4].rank
    elif hand[2].rank==hand[4].rank:
      return 4 * 13^5 + hand[2].rank * 13^4 + hand[3].rank * 13^3 + hand[4].rank * 13^2 + hand[0].rank * 13 + hand[1].rank
    else:
      return 0
  ### checks if the hand is a two pair
  def isTwo (self, hand):
    if hand[0].rank==hand[1].rank and hand[2].rank==hand[3].rank:
      return 3 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    elif hand[0].rank==hand[1].rank and hand[3].rank==hand[4].rank:  
      return 3 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[3].rank * 13^2 + hand[4].rank * 13 + hand[2].rank
    elif hand[1].rank==hand[2].rank and hand[3].rank==hand[4].rank:
      return 3 * 13^5 + hand[1].rank * 13^4 + hand[2].rank * 13^3 + hand[3].rank * 13^2 + hand[4].rank * 13 + hand[0].rank
    else:
      return 0
  ### checks if the hand is a pair
  def isOne (self, hand):
    if hand[0].rank==hand[1].rank:
      return 2 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    elif hand[1].rank==hand[2].rank:
      return 2 * 13^5 + hand[1].rank * 13^4 + hand[2].rank * 13^3 + hand[0].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    elif hand[2].rank==hand[3].rank: 
      return 2 * 13^5 + hand[2].rank * 13^4 + hand[3].rank * 13^3 + hand[0].rank * 13^2 + hand[1].rank * 13 + hand[4].rank
    elif hand[3].rank==hand[4].rank:
      return 2 * 13^5 + hand[3].rank * 13^4 + hand[4].rank * 13^3 + hand[0].rank * 13^2 + hand[1].rank * 13 + hand[2].rank
    else:
      return 0
  ### checks if the hand is a high card 
  def isHigh (self, hand):
    pts = 1 * 13^5 + hand[0].rank * 13^4 + hand[1].rank * 13^3 + hand[2].rank * 13^2 + hand[3].rank * 13 + hand[4].rank
    return pts
  
  ## Determine the winner of the game
  def getWinner(self, total):
    max = 0
    for num in total:
      if num > max:
        max = num
    winner = total.index(max)
    return winner
    
def main():
  handsplayed = input("Enter the number of hands to play: ")
  game = Poker(handsplayed)
  game.play()
  

main()