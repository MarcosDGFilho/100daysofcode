# %% 
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
nameAsCSV = input("Give me everybody's name separated by a comma.")
names = nameAsCSV.split(',')
luckyOne = random.randint(0,len(names)-1)
print(f'{names[luckyOne]} is going to buy the meal today!')

##Pode-se usar também random.choice() para escolher
##um elemento aleatório dentro de uma lista
##random.choice(names) escolheria um nome entre
##todos os nomes da lista.