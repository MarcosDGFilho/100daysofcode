#imports
from random import randint
from questionary import Validator, ValidationError, prompt, question
import questionary

class NumValidator(Validator):
    def validate(self, number):
        #print(f'document.text = {document.text}')
        try:
            x = int(number.text)
        except:
            raise ValidationError(
                message="Please enter an positive integer",
                #cursor_position=len(number.text)
        )



#This function checks if the guess made is equal to the secret number, if it's correct
#then it'll return True, otherwise it'll return False
def CheckGuess(guess):
    if guess == secret_number:
        questionary.print(f"You did it! The secret number was {secret_number}", style="bold italic fg:darkblue")
        return True
    else:
        if guess > secret_number:
            questionary.print(f"Try a lower number", style="bold italic fg:darkred")
        else:
            questionary.print(f"Try a higher number", style="bold italic fg:darkred")
        return False

tryAgain = True
gameOn   = True



print("Welcome to Guess the number, you'll have to guess a number between 0 and 100!")



#Game running from now on
while gameOn == True:
    list = []
    for i in range(101):
        list.append(str(i))
    lowestGuess  = 0
    highestGuess = 100
    #creating a random number and selecting difficulty level
    secret_number = randint(0,100)
    difficulty = questionary.select("Which difficulty would you like to play on?", 
    choices=["Easy", "Hard"]).ask()
    if difficulty == "Easy":
        total_lives = 10
    else:
        total_lives = 5


    #play until lives are set to 0
    while total_lives > 0:
        guess = int(questionary.text("Make a guess:", validate=NumValidator).ask())
        CheckGuess(guess)
        if guess != secret_number:
            total_lives -= 1
            print(f"Health left: {total_lives}")
            if total_lives < 1:     
                questionary.print(f"You lost! The secret number was {secret_number}. Better luck next time", style="bold italic fg:darkred")    #ask if player wants to play again
            if lowestGuess < guess < secret_number:
                lowestGuess = guess
            elif highestGuess > guess > secret_number:
                highestGuess = guess
            print(f'The secret number is between {lowestGuess} and {highestGuess}')
            for _ in list[:lowestGuess]:
                print(f"-",end='')
            print(lowestGuess,end='')
            for _ in list[lowestGuess:highestGuess]:
                print("-",end='')
            print(highestGuess,end='')
            for _ in list[highestGuess+1:]:
                print(f"-",end='')
            print('')


        else:
            break


    #ask if player wants to go another round, if he says no prints the goodbye
    play_again = questionary.select("Would you like to play again?",
    choices = ["Yes", "No"]).ask()
    if play_again == "No":
        gameOn = False

print ("""



████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗             
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║             
   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║             
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║             
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝             
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝              
                                                                                       
███████╗ ██████╗ ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗ ██╗
██╔════╝██╔═══██╗██╔══██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝ ██║
█████╗  ██║   ██║██████╔╝    ██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗██║
██╔══╝  ██║   ██║██╔══██╗    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║╚═╝
██║     ╚██████╔╝██║  ██║    ██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
                                                                                       """)

    

#%%

# %%
