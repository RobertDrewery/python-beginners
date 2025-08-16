#Guessing Game based on numbers 1-10:

import random

number_to_guess = random.randint (1, 10)
tries = 0

while tries < 3:
  guess = int(input('Guess the number (1-10): '))
  tries = tries + 1

  if guess == number_to_guess: 
    print('You guessed it!')
    break
  else: 
    print('Wrong, try again')

if guess != number_to_guess:
  print('GAME OVER. The correct number was' , number_to_guess)
  