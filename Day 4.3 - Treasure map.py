#%%
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map  = [row1, row2, row3 ]
print(f"{row1}\n{row2}\n{row3}")
print('''Here are the coordinates to each square

_11_|_12_|_13_
_21_|_22_|_23_
_31_|_32_|_33_

''')
position = input("Where do you want to put the treasure? ")
hor = int(position[0]) - 1
ver = int(position[1]) - 1
map[hor][ver] = '💰'

print("Your treasure has been buried!!")
print(f"{row1}\n{row2}\n{row3}")
