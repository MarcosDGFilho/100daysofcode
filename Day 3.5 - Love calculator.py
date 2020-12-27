# %%
print("Welcome to the Love Calculator!")
name1 = input("What's your name? \n")
name2 = input("What's their name? \n")

names = name1+name2

tCount = names.lower().count("t")
rCount = names.lower().count("r")
uCount = names.lower().count("u")
eCount = names.lower().count("e")
lCount = names.lower().count("l")
oCount = names.lower().count("o")
vCount = names.lower().count("v")
eCount = names.lower().count("e")

dozens = (tCount+rCount+uCount+eCount)*10
units  = (lCount+oCount+vCount+eCount)

trueLove = dozens+units

if trueLove < 10 or trueLove > 90:
    print(f"Your score is {trueLove}. You go together like coke and mentos")
elif 40 <= trueLove <= 50:
    print(f"Your score is {trueLove}. You go alright together")
else:
    print(f'Your score is {trueLove}.')
# %%
