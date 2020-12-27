# %%
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))
bmi    = weight/((height/100)**2)

if bmi <= 18.5:
    print(f"Your BMI is: {bmi}. You are currently underweight.")
elif 18.5 < bmi <= 25:
    print(f"Your BMI is: {bmi}. You have a normal weight.")
elif 25 < bmi <= 30:
    print(f"Your BMI is: {bmi}. You are currently overweight.")
elif 30 < bmi <= 35:
    print(f"Your BMI is: {bmi}. You are currently obese.")
else:
    print(f"Your BMI is: {bmi}. You are currently clinically obese.")
# %%
