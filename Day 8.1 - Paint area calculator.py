#Write your code below this line 👇
# %%
from math import ceil


def paint_calc(height, width, coverage):
    area = height * width
    return (print(f"You will need {ceil(area/coverage)} buckets of paint for this job"))

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = int(input("What's the coverage of your paint?: "))
paint_calc(height=test_h, width=test_w, coverage=coverage)
