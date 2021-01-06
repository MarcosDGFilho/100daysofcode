import random
import questionary
from questionary import Validator, ValidationError, prompt
from game_data import data

class NameValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text),
            )

def CompareFollowers(p1,p2):
    if p1['follower_count'] > p2['follower_count']:
        print(f"{p1['name']} has {p1['follower_count']-p2['follower_count']}m more followers than {p2['name']}")
        return p1['name']
    else:
        print(f"{p2['name']} has {p2['follower_count']-p1['follower_count']}m more followers than {p1['name']}")
        return p2['name']
        

print("Welcome to Higher or Lower")
gameOn = True
score = 0

while gameOn:
    p1 = random.choice(data)
    p2 = random.choice(data)
    while p1 == p2:
        p2 = random.choice(data)
    
    while True:

        player_choice = questionary.select(f"Which one of these two has more followers?", 
        choices=[p1["name"], p2["name"]]).ask()
        correct_answer = CompareFollowers(p1,p2)
        if correct_answer == p1['name']:
            p2 = random.choice(data)
        else:
            p1 = random.choice(data)
        if correct_answer == player_choice:
            questionary.print("You got it right!", style="bold italic fg:darkblue")
            score += 1
            print(f"Current Score: {score}")
        else:
            questionary.print("You lost!", style="bold italic fg:darkred")
            break
    print(f'Total score: {score}')
    playAgain = questionary.select("Would you like to play again?", choices=["Yes","No"]).ask()
    if playAgain == "No":
        gameOn = False
        print("Good bye!")