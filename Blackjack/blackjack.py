from cards_engine import Player, Deck, show_hand_ascii
import questionary, os
from time import sleep
from questionary import Validator, ValidationError, prompt, question

class NameValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text),
            )

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
clear = lambda: os.system('cls') #clear output

print('''




██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                        



''')


playerScore = 0
houseScore  = 0
gameOn = True

p1 = Player(questionary.text("What is your name?", validate=NameValidator).ask())
decksNumber = questionary.text("With how many decks would you like to play with? (Blackjack is usally played with 5 decks in casinos) ",
validate=NumValidator).ask()

while gameOn == True:
    #actionMenu = True
    #ignorePSC = False
    #ignoreDSC = False
    playerWin = False
    playerLose = False
    playerDraw = False

    #Getting basic info player name and # of decks
    
    antiLoop = 0
    #running game session
    while playerWin == False and playerLose == False and playerDraw == False:
        antiLoop +=1
        if antiLoop > 5:
            print('''
            
            ANTI LOOP IMPEDIU DE EXPLODIR TUDO
            
            ''')
            break
        ##Loading the deck that'll be used in this game session
        deck = Deck(decks=decksNumber)
        questionary.print("Shuffling the deck, please wait a few secons...", style="bold italic fg:darkred")
        sleep(3)
        deck.shuffle()
        gameDeck = deck.cards

        #player must draw 2 cards at the start of the game
        p1.draw(baralho=gameDeck)
        p1.draw(baralho=gameDeck)

        #Player's hand:
        print("This is your hand:")
        show_hand_ascii(p1.hand)

        #Dealer's hand
        print("This is the dealer's hand:")
        dealer = Player("Dealer")
        dealer.draw(baralho=gameDeck)
        #print("This is the dealer's hand:")
        show_hand_ascii(dealer.hand)
        
        if p1.score > 21:
            show_hand_ascii(p1.hand)
            print("You went over 21!")
            playerLose = True
        else: #Player action (Draw, check score or do nothing)
            while True:
                actionMenu = questionary.select("What would you like to do?",
                choices=[
                    "Check scores.",
                    "Draw another card.",
                    "Do nothing."
                ]).ask()
                if actionMenu == "Check scores.":
                    p1.check_score()
                    dealer.check_score()
                elif actionMenu == "Draw another card.":
                    questionary.print("Drawing another card...", style="bold italic fg:darkred")
                    p1.draw(baralho=gameDeck)
                    sleep(2)
                    show_hand_ascii(p1.hand)
                    if p1.score > 21:
                        show_hand_ascii(p1.hand)
                        sleep(2)
                        print("Oh no, you lost!")
                        playerLose = True
                    break
                else:
                    show_hand_ascii(p1.hand)
                    break
        
        while dealer.score < 17:
            print("The dealer is drawing another card.")
            sleep(2)
            dealer.draw(baralho=gameDeck)
            show_hand_ascii(dealer.hand)
        if dealer.score > 21:
            playerWin = True

#Neither the player or the dealer have a score bigger than 21 so far
#So we're checking to see if we should use softScore as our highest score
#To determine who's gonna win.
        print('\n'*100)
        
        questionary.print("Your final hand:", style="bold italic bg:darkred")
        show_hand_ascii(p1.hand)
        questionary.print("Dealers final hand:", style="bold italic bg:darkblue")
        show_hand_ascii(dealer.hand)
        if p1.score < p1.softScore < 22:
            playerEndScore = p1.softScore
        else:
            playerEndScore = p1.score
        if dealer.score < dealer.softScore < 22:
            dealerEndScore = dealer.softScore
        else:
            dealerEndScore = dealer.score
        
        if playerEndScore > dealerEndScore:
            print('''
            

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝
                                                               

            ''')
            sleep(2)
            playerScore += 1
            playerWin = True
        elif playerEndScore == dealerEndScore:
            print('''
            


██████╗ ██████╗  █████╗ ██╗    ██╗██╗
██╔══██╗██╔══██╗██╔══██╗██║    ██║██║
██║  ██║██████╔╝███████║██║ █╗ ██║██║
██║  ██║██╔══██╗██╔══██║██║███╗██║╚═╝
██████╔╝██║  ██║██║  ██║╚███╔███╔╝██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝
                                     



            ''')
            sleep(2)
            playerScore += 1
            houseScore += 1
            playerDraw = True
        else:
            print('''
            
            

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗██╗        ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝██║    ██╗██╔╝
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   ██║    ╚═╝██║ 
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   ╚═╝    ██╗██║ 
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   ██╗    ╚═╝╚██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝        ╚═╝
                                                                               



            ''')
            sleep(2)
            houseScore += 1
            playerLose = True
        print(f'''
Thank you for playing!
The final score was:
{p1.name}: {playerEndScore}
{dealer.name}: {dealerEndScore}
        ''')
        playAgain = questionary.select("Would you like to play again?",
        choices=[
            "Yes",
            "No"
        ]).ask()
        if playAgain == "No":
            gameOn = False
        clear()
sleep(1.66)
print(f"The final score was\nYou:{playerScore}\nThe House:{houseScore}")