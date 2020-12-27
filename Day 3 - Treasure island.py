print("Welcome to Treasure Island. Your mission is to find the treasure.")
c1 = input("You're at a cross road. Which way would you like to go left or right? ")
if c1 == 'right' or c1 == 'r' or c1 ==  'Right' or c1 == 'RIGHT':
    print("\nThe right way was the wrong way. Game over.")
else:
    c2 = input("\nYou come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat, or 'swim' to swim across. ")
    if c2 == 'swim' or c2 == 's' or c2 == 'SWIM' or c2 == 'Swim':
        print("\nYou tried to swim across the lake. Your legs begin to cramp, and you end up drowing. Game over. ")
    else:
        c3 = input("\nYou arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose?")
        if c3 == 'yellow' or c3 == 'Yellow' or c3 == 'YELLOW' or c3 == 'Y' or c3 == 'y':
            print("\nCongratulations you've found the treasure chest!")
            print('''\n
            
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
            
            ''')
        else:
            print("\n As you open the door, a trap triggers and shoots an arrow straight through your head. Game over.")