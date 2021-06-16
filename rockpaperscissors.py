import random
computer_win_counter = 0
player_win_counter = 0
    


print("Welcome. The Rock, Paper, Scissors tournament is starting now. Best of 5.")
print("\n")
name = input("Player 1, please enter your name: ")
def print_result():
  global computer_win_counter, player_win_counter
  print (name + " won: " + str(player_win_counter) + ": " + " computer won: " + str(computer_win_counter))
def game(name):
  global computer_win_counter, player_win_counter
  options = ["rock", "paper", "scissors"]
  player1 = input(name+", Rock, Paper, Scissors shoot:").lower()

  computerrobotplayer23876 = random.choice(options)

  print(name+" has chosen " +player1)
  print("computerrobotplayer23876, has chosen " +computerrobotplayer23876)

  if player1==computerrobotplayer23876:
    print("tie")
    print_result()

  elif player1=="rock" and computerrobotplayer23876=="scissors":
    print(name+" wins this round")
    player_win_counter = player_win_counter + 1
    print_result()
 
  elif player1=="rock" and computerrobotplayer23876=="paper":
    print("computerrobotplayer23876 wins.")
    computer_win_counter = computer_win_counter + 1
    print_result()
  elif player1=="paper" and computerrobotplayer23876=="rock":
    print(name+" wins this round.")
    player_win_counter = player_win_counter + 1
    print_result()
        
  elif player1=="paper" and computerrobotplayer23876=="scissors":
    print("computerrobotplayer23876 wins this round.")
    computer_win_counter = computer_win_counter + 1
    print_result()
 
  elif player1=="scissors" and computerrobotplayer23876=="rock":
    print("computerrobotplayer23876 wins this round.")
    computer_win_counter = computer_win_counter + 1
    print_result()
   
  elif player1=="scissors" and computerrobotplayer23876=="paper":
    print(name+" wins this round.")
    player_win_counter = player_win_counter + 1
    print_result()
    
for items in range(3):
  game(name)
  print("\n")
 






  



