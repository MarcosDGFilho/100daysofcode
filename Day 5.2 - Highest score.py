#%%
studentScores = input("Input a list of student scores ").split()
for n in range(0, len(studentScores)):
    studentScores[n] = int(studentScores[n])
print(studentScores)

#%%
highestScore = studentScores[0]
for i in range(0, len(studentScores)):
    testResult = highestScore - studentScores[i] 
    #print(f'Test result: {testResult}')
    #print(f'Highest score: {highestScore}')
    if testResult <= 0:
        highestScore = studentScores[i]
print(f'The highest score in class is: {highestScore}')
# %%
