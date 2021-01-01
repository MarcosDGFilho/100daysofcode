# %%
import questionary
import math
from questionary import Validator, ValidationError, prompt, question


class NameValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text),
            )

class NumValidator(Validator):
    def validate(self, number):
        #print(f'document.text = {document.text}')
        try:
            x = int(number.text)
        except:
            raise ValidationError(
                message="Please enter an positive integer",
                #cursor_position=len(number.text)
        )

class ShiftCipher:
    def __init__(self, N = 13):
        if N % 25 == 0 :
            N = 0
        elif N > 25:
            N = N - (25*math.floor(N/25))
        self.original_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.cipher_alphabet = self.original_alphabet[N:]
        self.cipher_alphabet.extend(self.original_alphabet[0:N])
    def encrypt_message(self, message):
        encrypted = ''
        message = message.lower()
        for letter in message:
            if self.original_alphabet.count(letter) > 0:
                index = self.original_alphabet.index(letter)
                encrypted += self.cipher_alphabet[index]
            else:
                encrypted += letter
        return encrypted

    def decrypt_message(self, message):
        decrypted = ""
        #lowercase the message as alphabets are lowercase
        message = message.lower()
        for letter in message:
            if self.original_alphabet.count(letter) > 0:
                #if the letter exists in original alphabet, find the index and add decrypted form
                index = self.cipher_alphabet.index(letter)
                decrypted += self.original_alphabet[index]
            else:
                #if it does not exist in original alphabet, do not change the character 
                decrypted += letter
        return decrypted



while True:
    main_menu = questionary.select("What you want to do?", 
    choices=[
        "Encode a text.",
        "Decode a text.",
        "Exit the program."
        
    ]).ask()
    if main_menu == "Encode a text.":
        text = questionary.text("Please type your text:", validate=NameValidator).ask().lower()
        shift = int(questionary.text("Please input a shift number:", validate=NumValidator).ask())
        #text = ShiftCipher(N=shift).encrypt_message(text)
        questionary.print(f"Your encrypted text is: {ShiftCipher(N=shift).encrypt_message(message=text)}",
        style="bold italic fg:ansired")
        pass
    elif main_menu == "Decode a text.":
        text = questionary.text("Please type your text:", validate=NameValidator).ask().lower()
        shift = int(questionary.text("Please input a shift number:", validate=NumValidator).ask())
        questionary.print(f"Your encrypted text is: {ShiftCipher(N=shift).decrypt_message(message=text)}",
        style="bold italic fg:ansired")
        pass
    else:
        break


#minha_cifra = ShiftCipher(N=shift)
#print(minha_cifra.encrypt_message(message=text))
#print(minha_cifra.decrypt_message(message=text))
