import random
import card

print("Welcome to digital Hi-Lo!")
print("\nInstructions: Guess whether the next card will be higher (H) or lower (L) than the current card. Aces are 11, face cards are 10. For each guess you get correct, your score goes up by one. If you get a score of 5, you win. If at any point you would like to stop playing, type Q.")


def newDeck():
  # creates empty deck
  deck = []
  # creates all possible cards
  for i in range(4):
    for j in range(13):
      deck.append(card.Card(i,j,j))
  # shuffles
  random.shuffle(deck)
  return deck
  

def game():
  score = 0                     # Initialize player's score to zero
  discard_pile = []             # List to keep track of discarded cards
  Deck = newDeck()              # Create and shuffle a new deck of cards
  oldCard = random.choice(Deck) # Select the first card randomly from the deck
  again = 'Hello'               # Placeholder variable 

  while True:                   # Start the game loop

    
    if score == 10:            # Check if player has reached winning score
      print('\n\nCongrats! You Win!')
      print('\nThanks for playing!')
      break                   # Exit the game loop

    print('\nCurrent card:', oldCard)  # Show the current card to the player
    ans = input('Will the next card drawn be higher (H) or lower (L)?') # Ask for player guess

    newCard = random.choice(Deck)      # Draw the next card randomly
    print('\nNew card:', newCard)      # Display the new card
    discard_pile.append(oldCard)       # Add the old card to the discard pile

    if ans.upper() == 'H':             # Player guessed Higher
      if newCard.value > oldCard.value:
        print('\n\nCorrect!')
        score += 1                    # Increase score for correct guess
        print('Score:', score)
      else:
        print('\n\nIncorrect!')
        print('Score:', score)

    elif ans.upper() == 'L':           # Player guessed Lower
      if newCard.value < oldCard.value:
        print('\n\nCorrect!')
        score += 1                    # Increase score for correct guess
        print('Score:', score)
      else:
        print('\n\nIncorrect!')
        print('Score:', score)

    else:                             # Any input other than H or L exits game
      print('Thanks for playing!')
      break                          # Exit the game loop

    oldCard = newCard                 # Update current card for next round
    print("Discard pile:", discard_pile)  # Show cards played so far

game()  # Start the game

    



