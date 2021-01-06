import random
from questionary import select

def Compare(pos1, pos2):
    if pos2 > pos1:
        correct_answer = "Higher"
    else:
        correct_answer = "Lower"
    answer = select(f"Is {pos2} higher or lower than {pos1}?", choices=["Higher", "Lower"]).ask()
    if answer == correct_answer:
        return True
    else:
        return False

data = [1,2,3,4,5,6]
score = 0

while True:
    random.shuffle(data)
    pos1 = data[0]
    pos2 = data[1]
    if Compare(pos1,pos2) == False:
        print("You got it wrong!")
    else:
        print("You got it right")
    #for number in data[2:]:
    break
        
        