from x01_player import *
from x02_computer import *
from x03_winner import *
from x04_game import *

if __name__ == "__main__":
  pass
count = 0
def Sc0reboard():
  f = (rockpapersciss0rs())
  if f == -1: 
    output = "you lost. try again."
  elif f == 2:
    output = "you lost. try again."
  elif f == 0: 
    output = "ahh, a stalemate. try again"
  elif f == 1:
    output = "congrats! you won!"
  elif f == -2:
    output = "congrats! you won!"
  else:
    output = "hell naw spunch bob"
  return output
