# %%
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
x = int(random.random()*100)
if x % 2 == 0:
    print("Tails")
else:
    print("Heads")