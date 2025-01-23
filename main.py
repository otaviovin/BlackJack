# Importing necessary modules
import random
from replit import clear
from art import logo

# Function to deal a random card to the player or computer
def deal_card():
  # List of cards with their values, 10 appears four times to represent 10, J, Q, K
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)  # Randomly choose a card
  return card

# Function to calculate the total score of the cards
def calculate_score(cards):
  # If the player has exactly 21 with two cards, it's a Blackjack (score 0)
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  # Adjust for Ace (11) being used as 1 if total score goes over 21
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# Function to compare the user's score with the computer's score and determine the result
def compare(user_score, computer_score):

  # If both scores are over 21, the user loses
  if user_score > 21 and computer_score > 21:
    return "Lose"

  # If scores are the same, it's a draw
  if user_score == computer_score:
    return "Draw. Try it again"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"  # Opponent gets a Blackjack
  elif user_score == 0:
    return "Win with a Blackjack"  # User gets a Blackjack
  elif user_score > 21:
    return "You went over. You lose"  # User exceeds 21
  elif computer_score > 21:
    return "Opponent went over. You win"  # Opponent exceeds 21
  elif user_score > computer_score:
    return "Win"  # User has a higher score
  else:
    return "Lose"  # Computer has a higher score

# Main function to play the game
def play_game():
  print(logo)  # Print the game logo

  user_cards = []  # List to store the user's cards
  computer_cards = []  # List to store the computer's cards
  is_game_over = False  # Flag to indicate if the game is over

  # Deal two cards to both user and computer
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  # Continue the game until it's over
  while not is_game_over:
    user_score = calculate_score(user_cards)  # Calculate the user's score
    computer_score = calculate_score(computer_cards)  # Calculate the computer's score
    print(f"Your cards: {user_cards}, current score is: {user_score}")
    print(f"Computer's first card is: {computer_cards[0]}")  # Show only the first card of the computer

    # Check if the game is over (user or computer has Blackjack, or the user exceeds 21)
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Want to get another card? Yes or No: ")  # Ask the user for a decision
      if user_should_deal == "Yes":
        user_cards.append(deal_card())  # Deal another card to the user
      else:
        is_game_over = True  # End the game if the user chooses "No"

  # The computer will keep drawing cards until its score is at least 17
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  # Display the final hands and scores for both user and computer
  print(f"Your final hand: {user_cards}, final score is: {user_score} ")
  print(f"Computer's final hand: {computer_cards}, final score is: {computer_score}")
  print(compare(user_score, computer_score))  # Print the result of the game

# Ask the user if they want to play the game
while input("Do you want to play Blackjack? Yes or No: ") == "Yes":
  clear()  # Clear the screen for a fresh game
  play_game()  # Start a new game
