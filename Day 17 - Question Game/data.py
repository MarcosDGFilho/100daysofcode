# %%
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.",
        "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


# %%
new_question_data = [

    {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "In the 1988 film 'Akira', Tetsuo ends up destroying Tokyo.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "Clefairy was intended to be Ash's starting Pokémon in the pilot episode of the cartoon.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "medium", "question": "The animated film 'Spirited Away' won the Academy Award for Best Animated Feature at the 75th Academy Awards in 2003.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "Studio Ghibli is a Japanese animation studio responsible for the films 'Wolf Children' and 'The Boy and the Beast'.", "correct_answer": "False", "incorrect_answers": ["True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "In Kill La Kill, the weapon of the main protagonist is a katana. ", "correct_answer": "False", "incorrect_answers": ["True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "The anime 'Lucky Star' follows the story of one girl who is unaware she is God.", "correct_answer": "False", "incorrect_answers": ["True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "No Game No Life first aired in 2014.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "Gosho Aoyama Made This Series: (Detective Conan \/ Case Closed!)", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "In the 'Melancholy of Haruhi Suzumiya' series, the narrator goes by the nickname Kyon.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "medium", "question": "The anime Attack on Titan was directed by Tetsur\u014d Araki, the same person who directed the anime Highschool of the Dead.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "In Pokémon, Ash's Pikachu refuses to go into a pokeball.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "hard", "question": "Throughout the entirety of 'Dragon Ball Z', Goku only kills two characters: a miniboss named Yakon and Kid Buu.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "In the 'Toaru Kagaku no Railgun' anime,  espers can only reach a maximum of level 6 in their abilities.", "correct_answer": "False", "incorrect_answers": [
        "True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "The name of the attack 'Kamehameha' in Dragon Ball Z was named after a famous king of Hawaii.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "Kiznaiver is an adaptation of a manga.", "correct_answer": "False", "incorrect_answers": ["True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "hard", "question": "Druid is a mage class in 'Log Horizon'.", "correct_answer": "False", "incorrect_answers": ["True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "medium", "question": "In 'JoJo's Bizarre Adventure', Father Enrico Pucchi uses a total of 3 stands in Part 6: Stone Ocean.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "In the 'To Love-Ru' series, Golden Darkness is sent to kill Lala Deviluke.", "correct_answer": "False", "incorrect_answers": ["True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "medium", "question": "In 'To Love-Ru: Darkness', Yami reveals her real name is Eve.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "hard", "question": "In the 'To Love-Ru' series, Peke is considered a female robot.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy", "question": "In Chobits, Hideki found Chii in his apartment.", "correct_answer": "False", "incorrect_answers": ["True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "hard", "question": "In the 'Kagerou Daze' series, Shintaro Kisaragi is prominently shown with the color red.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "hard", "question": "The character Plum from 'No Game No Life' is a girl.", "correct_answer": "False", "incorrect_answers": ["True"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "medium", "question": "In Full Metal Panic!, Whispered are those who are capable of creating Black Technology.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "hard", "question": "The protagonist in 'Humanity Has Declined' has no discernable name and is simply referred to as 'I' for most of the series.", "correct_answer": "True", "incorrect_answers": ["False"]}

]
#new_question_data_clean = []
# for i in new_question_data:
#     temp_dict = {}
#     temp_dict['text'] = i['question']
#     temp_dict['answer'] = i['correct_answer']
#     new_question_data_clean.append(temp_dict)


new_question_data_clean = [
    {"text": "In the 1988 film 'Akira', Tetsuo ends up destroying Tokyo.",
     "answer": "True"},
    {"text": "Clefairy was intended to be Ash's starting Pokémon in the pilot episode of the cartoon.",
        "answer": "True"},
    {"text": "The animated film 'Spirited Away' won the Academy Award for Best Animated Feature at the 75th Academy Awards in 2003.",
        "answer": "True"},
    {"text": "Studio Ghibli is a Japanese animation studio responsible for the films 'Wolf Children' and 'The Boy and the Beast'.",
        "answer": "False"},
    {"text": "In Kill La Kill, the weapon of the main protagonist is a katana. ",
        "answer": "False"},
    {"text": "The anime 'Lucky Star' follows the story of one girl who is unaware she is God.",
        "answer": "False"},
    {"text": "No Game No Life first aired in 2014.", "answer": "True"},
    {"text": "Gosho Aoyama Made This Series: (Detective Conan \\/ Case Closed!)",
        "answer": "True"},
    {"text": "In the 'Melancholy of Haruhi Suzumiya' series, the narrator goes by the nickname Kyon.",
        "answer": "True"},
    {"text": "The anime Attack on Titan was directed by Tetsurō Araki, the same person who directed the anime Highschool of the Dead.",
        "answer": "True"},
    {"text": "In Pokémon, Ash's Pikachu refuses to go into a pokeball.",
        "answer": "True"},
    {"text": "Throughout the entirety of 'Dragon Ball Z', Goku only kills two characters: a miniboss named Yakon and Kid Buu.",
        "answer": "True"},
    {"text": "In the 'Toaru Kagaku no Railgun' anime,  espers can only reach a maximum of level 6 in their abilities.",
        "answer": "False"},
    {"text": "The name of the attack 'Kamehameha' in Dragon Ball Z was named after a famous king of Hawaii.",
        "answer": "True"},
    {"text": "Kiznaiver is an adaptation of a manga.", "answer": "False"},
    {"text": "Druid is a mage class in 'Log Horizon'.",
        "answer": "False"},
    {"text": "In 'JoJo's Bizarre Adventure', Father Enrico Pucchi uses a total of 3 stands in Part 6: Stone Ocean.",
        "answer": "True"},
    {"text": "In the 'To Love-Ru' series, Golden Darkness is sent to kill Lala Deviluke.",
        "answer": "False"},
    {"text": "In 'To Love-Ru: Darkness', Yami reveals her real name is Eve.",
        "answer": "True"},
    {"text": "In the 'To Love-Ru' series, Peke is considered a female robot.",
        "answer": "True"},
    {"text": "In Chobits, Hideki found Chii in his apartment.",
        "answer": "False"},
    {"text": "In the 'Kagerou Daze' series, Shintaro Kisaragi is prominently shown with the color red.",
        "answer": "True"},
    {"text": "The character Plum from 'No Game No Life' is a girl.",
        "answer": "False"},
    {"text": "In Full Metal Panic!, Whispered are those who are capable of creating Black Technology.",
        "answer": "True"},
    {"text": "The protagonist in 'Humanity Has Declined' has no discernable name and is simply referred to as 'I' for most of the series.",
        "answer": "True"}]
