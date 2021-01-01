#Write your code below this line 👇
#%%
def prime_checker(number):
    if number == 1:
        return True
        #return print(f"1 is a prime number!")
    for i in range(2,number):
        if number % i == 0:
            return False
            #return print(f"{number} is NOT a prime number")
        else:
            return True
            #return print(f"{number} is a prime number.")


#%%

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# %%
import time
t0 = time.time()
for i in range(1,100000):
    prime_checker(i)

t1 = time.time()
print(f"Time required: {t1-t0}")
# %%
