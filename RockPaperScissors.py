# Rock Paper Scissors Game
# Features: random opponent choice, lowercase input handling, emojis for fun

import random
RPS = input('Rock 🪨, Paper 📄, Scissors✂️ : ') .lower()
random_number = random.randint(1, 3)
if random_number == 1:
  output = 'Rock 🪨 ' 
elif random_number == 2:
  output = 'Paper 📄 '
elif random_number == 3:
  output = 'Scissors ✂️ '
else:
  output = 'error'

#Rock outcomes:
if RPS == 'rock' and random_number == 1:
  result = ' tie'
elif RPS =='rock' and random_number == 2:
  result = ' you lose. Try again.'
elif RPS == 'rock' and random_number == 3:
  result = ' you win!'
#Paper outcomes:
elif RPS == 'paper' and random_number == 1:
  result = ' you Win!'
elif RPS == 'paper' and random_number == 2:
  result = ' tie'
elif RPS == 'paper' and random_number == 3:
  result = ' you lose. Try again.'
#Scissors outcomes:
elif RPS == 'scissors' and random_number == 1:
  result = ' you lose. Try again.'
elif RPS == 'scissors' and random_number == 2:
  result = ' you Win!'
elif RPS == 'scissors' and random_number == 3:
  result = ' tie'
else:
  print('error, wrong input')
  quit()    

#Final Outcome:
print(output + ',' + result)
