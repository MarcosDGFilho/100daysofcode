# %%
import random
#tryAgain = True

while True:
    playerMove     = 0 ##Rock = +1, Paper = +2, Scissor = +3
    computerMove   = 0 ##the result of the match is determined by playerMove - computerMove 
    print("\nWelcome to Janken\n")
    playerMove = int(input('''
    .-----------------------.
    |Please select your move|
    |1: Rock                |
    |2: Paper               |
    |3: Scissors            |
    .-----------------------.

    '''))
    if playerMove == 1 or playerMove == 2 or playerMove == 3:
        if playerMove == 1:
            playerMoveName = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
            '''
        elif playerMove == 2:
            playerMoveName =  '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
            '''
        elif playerMove == 3:
            playerMoveName = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
            '''
        computerMove = random.randint(1,3)
        if computerMove == 1:
            computerMoveName = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
            '''
        elif computerMove == 2:
            computerMoveName =  '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
            '''
        elif computerMove == 3:
            computerMoveName = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
            '''
        matchResult = playerMove - computerMove
        if matchResult == 0:
            print(f"Your move:\n{playerMoveName}.\n\nThe computer's move:\n {computerMoveName}\n")
            print ("It was a draw! Would you like to try again?")
            x = input("Yes or No? (y/n)")
            if x == 'n' or x == 'N':
                print("Goodbye!")
                break
            else:
                print("Good luck next match!")
        elif matchResult == 1 or matchResult == -2:
            print(f"Your move was {playerMoveName}. The computer move was {computerMoveName}")
            print ("You won, congratulations! Would you like to try again?")
            x = input("Yes or No? (y/n)")
            if x == 'n' or x == 'N':
                print("Goodbye!")
                break
            else:
                print("Good luck next match!")
        elif matchResult == 2 or matchResult == -1:
            print(f"Your move was {playerMoveName}. The computer move was {computerMoveName}")
            print ("You lost, better luck next time! Would you like to try again?")
            x = input("Yes or No? (y/n)")
            if x == 'n' or x == 'N':
                print("Goodbye!")
                break
            else:
                print("Good luck next match!")   
    else:
        print("Invalid input!")
print("Thank you for playing!")
# %%
