#%%
import pandas as pd
import questionary
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
            x = float(number.text)
        except:
            raise ValidationError(
                message="Please enter an positive integer",
                #cursor_position=len(number.text)
        )


bids = []
while True:
    loopList = []
    loopList.append(questionary.text("Please input your name:", validate=NameValidator).ask())
    loopList.append(float(questionary.text("Please input your bid:", validate=NumValidator).ask()))
    bids.append(loopList)
    keep_bidding = questionary.select("Are there another bidders?", choices=["Yes","No"]).ask()
    if keep_bidding == "No":
        break
df = pd.DataFrame(bids,columns=["Name","Price"])

df.sort_values(by=['Price'], inplace=True, ascending=False)

winner = df.iloc[0,0]
bidding = df.iloc[0,1]


questionary.print(f"The winner of this bid was {winner} with a bid of {bidding}", style="bold italic fg:ansired")
