# %%
bill = 0
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L?")
if size == 'S' or size == 's':
    bill = bill + 15
elif size == 'M' or size == 'm':
    bill = bill + 20
elif size == 'L' or size == 'l':
    bill = bill + 25
else:
    print("Invalid pizza size!")

addPep = input("Would you like to add Pepperoni? Y or N?")
if addPep == 'Y' or addPep =='y':
    if size == 'S' or size == 's':
        bill = bill + 2
    else:
        bill = bill + 3

extraCheese = input("Would you like to add extra cheese? Y or N?")
if extraCheese == 'Y' or extraCheese == 'y':
    bill = bill + 1

print(f'Your final bill is: ${bill}.')


# %%
