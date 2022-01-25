#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import *
from x02_computer import *
from x03_winner import *

if __name__ == "__main__":
  pass

def rockpapersciss0rs():
  output = 0
  a = playerChoice()
  b = computerChoice()
  c = playerWins(b, a)
  if c == 66:
    output = "invalid input"
  elif c == -1: 
    output = "you lost. try again."
  elif c == 2:
    output = "you lost. try again."
  elif c == 0: 
    output = "ahh, a stalemate. try again"
  elif c == 1:
    output = "congrats! you won!"
  elif c == -2:
    output = "congrats! you won!"
  else:
    output = "hell naw spunch bob"
  return output

print(rockpapersciss0rs())

