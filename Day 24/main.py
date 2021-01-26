# %%
from docx import Document
from docx2python import docx2python

starting_letter = docx2python(
    'C:/Users/Quinhos2020/Documents/GitHub/100daysofcode/Day 24/Input/Letters/starting_letter.docx')

with open('C:/Users/Quinhos2020/Documents/GitHub/100daysofcode/Day 24/Input/Letters/Names/invited_names.txt', 'r') as names:
    lines = names.readlines()
    for line in lines:
        print(line)
        carta = Document()
        convidado = line.replace('\n', '')
        carta.add_paragraph(starting_letter.text.replace("[name]", convidado))
        carta.save(
            f'C:/Users/Quinhos2020/Documents/GitHub/100daysofcode/Day 24/Output/ReadyToSend/{convidado}.docx')
    print("All cards were printed correctly!")
