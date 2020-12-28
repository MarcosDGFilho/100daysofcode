# %%
for i in range(1,101):
    score = 0
    if i % 3 == 0:
        score += 1
    if i % 5 == 0:
        score += 2
    if score == 1:
        print("Fizz")
    elif score == 2:
        print("Buzz")
    elif score == 3:
        print("FizzBuzz")
    else:
        print(i)

################ "Correct" solution ##############################
for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)