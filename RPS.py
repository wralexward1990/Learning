#Import modules
import random
from colorama import Fore, Style

#Code Start
while True:
  print(f"{Style.BRIGHT}Welcome to the Rock, Paper, Scissors game!{Style.NORMAL}")

  def get_choices():
    player_choice = input("Rock, Paper, or Scissors? ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

  def check_win(player, computer):
    print(f"{Fore.MAGENTA}You chose {player} and the Computer chose {computer}.{Fore.WHITE}" )
    if player == computer:
      return f"{Fore.GREEN}Tie{Fore.WHITE}"
    elif player == "rock":
      if computer == "scissors":
        return f"{Fore.BLUE}Rock smashes scissors. You win!{Fore.WHITE}"
      else:
        return f"{Fore.RED}Paper covers rock. You lose.{Fore.WHITE}"
    elif player == "scissors":
      if computer == "paper":
        return f"{Fore.BLUE}Scissors cut paper. You win!{Fore.WHITE}"
      else:
        return f"{Fore.RED}Rock smashes scissors. You lose.{Fore.WHITE}"
    elif player == "paper":
      if computer == "rock":
        return f"{Fore.BLUE}Paper covers rock. You win!{Fore.WHITE}"
      else:
        return f"{Fore.RED}Scissors cut paper. You lose.{Fore.WHITE}"

  def play_again():
    play_again = input("Play again? ")
    return play_again.lower() == "yes"

  choices = get_choices()
  result = check_win(choices["player"], choices["computer"])
  print(result)
  if not play_again():
    print("Thanks for playing!")
    break
