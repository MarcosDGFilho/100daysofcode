# %%
bill          = float(input(f'What was the bill? '))
eaters        = int(input(f'How many people to split the bill? '))
tipPercentage = int(input(f'What percentage would you like to give? 10, 12 or 15? '))
if tipPercentage == 10 or tipPercentage == 12 or tipPercentage == 15: 
    finalBill     = bill*(tipPercentage/100)+bill
    eachPay       = finalBill/eaters
    print(f'Each person should pay: {eachPay} ')
else:
    print("Invalid tip value!")
# %%
