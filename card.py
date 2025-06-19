suits = ["\u2660\uFE0F", "\u2665\uFE0F", "\u2666\uFE0F", "\u2663\uFE0F"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Card:
  def __init__(self, suit, rank, value):
    self.suit = suits[suit]
    self.rank = ranks[rank]
    self.value = values[value]

  def __str__(self):
    return "" + self.rank + self.suit

  def __repr__(self):
    return str(self)
    
  def getValue(self):
    return self.value


def getVal(obj):
    return obj.getValue()