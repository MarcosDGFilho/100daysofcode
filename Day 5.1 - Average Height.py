#%%
studentsHeights = input("Input a list of student heights in cm: ").split()
for n in range (0,len(studentsHeights)):
    studentsHeights[n] = int(studentsHeights[n])
print(studentsHeights)

# %%
sumHeights = 0
listLen = 0
for m in studentsHeights:
    listLen += 1
    sumHeights += studentsHeights[listLen-1]
averageHeight = round(sumHeights/listLen)
print(f"The average height of the students is: {averageHeight}cm.")
