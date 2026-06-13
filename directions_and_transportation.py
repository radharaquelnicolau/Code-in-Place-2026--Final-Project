"""
This is the directions and transportations module of Unolingua. This module contains the dictionary with all the directions and transportations, the different exercises and the different lesson plan for the directions and transportations will be written. 
"""
broken_loop = False
#variable that verifies whether the loop for the match the word game has broken so that the game can end
import random
#random is used to randomize which word in the dictionary is being tested for this module
from tabulate import tabulate 
#imports function that allows you to draw tables in terminal
import config
#imports scores, lives and functionality into the module and main
directions = {
    "turn right" : "vire à direita",
    "turn left" : "vire à esquerda",
    "continue straight ahead" : "continue sempre em frente",
    "go straight ahead" : "siga em frente",
    "behind" : "atrás",
    "next to" : "ao lado de",
    "between" : "entre",
    "in front" : "em frente"
}
#dictionary for directions in portuguese
transportation = {
    "the bus" : "o autocarro",
    "the taxi" : "O táxi",
    "the subway" : "O metro",
    "the bicycle" : "a bicicleta",
    "ship" : "o navio",
    "plane" : "avião",
    "car" : "carro",
    "by foot" : "a pé"
}   
#dictionary for transportations in portuguese
"""Directions(d) Multiple Choice Exercise"""
def d_multiple_choice():
    english_direction = random.choice(list(directions.keys()))
    #selects a random word from the dictionary in english
    portuguese_direction = directions[english_direction]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_direction}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(directions.values())
    #creates a list of the portuguese translations of the directions to be used as options for the multiple choice question
    random.shuffle(options)
    #shuffles the options so that the correct answer is not always in the same position
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_direction:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        config.user_xp += 5
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately, that is incorrect. The correct answer is '{portuguese_direction
}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
""" transportation(f) Multiple Choice Exercise"""
def t_multiple_choice():
    english_transportation = random.choice(list(transportation.keys()))
    #selects a random word from the dictionary in english
    portuguese_transportation = transportation[english_transportation]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_transportation}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(transportation.values())
    #creates a list of the portuguese translations of the transportations to be used as options for the multiple choice question
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_transportation:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        config.user_xp += 5
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately, that is incorrect. The correct answer is '{portuguese_transportation}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
""" Fill in the blanks exercise for both directions and transportations (dt)"""
def dt_fill_in_the_blanks():
    incomplete_sentences = {
        "siga __ ______" : "em frente",
        "ao ____ de" : "lado",
        "_____ o carro e a bicicleta" : "entre",
        "__ frente do navio" : "em",
        "vire à _______" : "direita",
        "____ _ esquerda" : "vire à",
        "________ sempre em frente" : "continue",
    }
    #dictionary of the incomplete sentences with the values being the correct answer to the incomplete sentence
    incomplete_sentence = random.choice(list(incomplete_sentences.keys()))
    #selects a random incomplete sentence from the dictionary to be used for the fill in the blank exercise
    correct_answer = incomplete_sentences[incomplete_sentence]
    #saves the correct answer to the incomplete sentence to be used for checking the user's answer
    print(f"Fill in the blank: '{incomplete_sentence}'")
    answer = input("Enter your answer: ")
    #asks the user to fill in the blank and saves their answer to be checked against the correct answer
    if answer == correct_answer:
        #checks if the user's answer is correct by comparing it to the correct answer saved from the dictionary
        config.user_xp += 10
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately that is not correct. The correct answer is '{correct_answer}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
""" Match the word exercise for both directions and transportations (dt)"""
def dt_match_the_word():
    big_english_words_list = list(directions.keys()) + list(transportation.keys())
    #makes a big list with all the english words from both dictionaries
    english_words = []
    #empty list to add the five words that will be used for this exercise
    random.shuffle(big_english_words_list)
    #shuffles the big list to increase randomness of chosen words
    for i in range(5):
        word = random.choice(big_english_words_list)
        #saves randomly chosen word in a variable
        english_words.append(word)
        #adds word to the llist that will be used for the exercise
        big_english_words_list.remove(word)
        #removes word from the big word list to avoid repition
    portuguese_words = []
    #empty list that will contain the correct answers
    for word in english_words:
        if word in directions:
            portuguese_words.append(directions[word])
        else:
            portuguese_words.append(transportation[word])
    #for loop checks each word in the english list and adds portuguese translation based on which dictionary the word is in
    random.shuffle(english_words)
    random.shuffle(portuguese_words)
    #shuffles both english and portuguese lists so that the words and the answers are not together
    headers = ["English", "Portuguese"]
    #headers for the table
    print(tabulate(list(zip(english_words, portuguese_words)), headers=headers, tablefmt="simple_grid"))
    #prints table using complete list data
    print("Match the english words to the portuguese words. Please type carefully as the spelling matters!")
    for word in english_words:
        portuguese_answer = input(f"{word}: ")
        #asks users to write the pair of both english and portuguese words
        if portuguese_answer == directions.get(word) or portuguese_answer == transportation.get(word):
            #checks if the pair is correct based on the directions dictionary
            config.user_xp += 5
            print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
        else:
            config.user_lives -= 1
            print(f"Unfortunately that is not correct. The correct answer is '{directions.get(word) or transportation.get(word)}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
            if config.user_lives == 0:
                broken_loop = True
                break
            #if loops check for whether the lives have finished and then changes the broken loop to true and breaks the loop
""" Build a Sentence exercise for both directions and transportations (dt)"""
def dt_build_a_sentence():
    sentences = {
        "the car is next to the bus" : "o carro está ao lado do autocarro",
        "continue straight" : "continue sempre em frente",
        "The car is in front of three bicycles" : "O carro está em frente de três bicicletas",
        "I will go by foot" : "eu vou a pé",
        "good evening, I am behind the taxi" : "boa noite, estou atrás do táxi"
    }
    #dictionary of the  sentences with the values being the correct translation to the sentence
    sentence = random.choice(list(sentences.keys()))
    #selects a random incomplete sentence from the dictionary to be used for the fill in the blank exercise
    correct_answer = sentences[sentence]
    #saves the correct answer to the sentence to be used for checking the user's answer
    print(f"Translate this to portuguese: {sentence}'")
    answer = input("Enter your answer: ")
    #asks the user to fill in the blank and saves their answer to be checked against the correct answer
    if answer == correct_answer:
        #checks if the user's answer is correct by comparing it to the correct answer saved from the dictionary
        config.user_xp += 10
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately that is not correct. The correct answer is '{correct_answer}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
""" Lesson plan for directions and transportations (dt)"""
def dt_lesson_plan():
    print("Welcome to our third lesson!")
    print("In this lesson, we will be learning about directions and modes of transportation in Portuguese.")
    #introduces the user to the first lesson of unolingua
    config.enter_to_continue()
    #function to make sure that only by pressing enter, will the user continue
    print("Here are the most common directions in Portuguese:")
    for english, portuguese in directions.items():
        print(f"{english} : {portuguese}")
        #prints each english word with is portuguese translation
    config.enter_to_continue()
    #ensures that next word only shows when pressed enter
    print('Note: vire -> turn, ' \
          "siga -> follow," \
          "sempre -> always," \
          "These are the separate meaning of some of the words used when explaining directions")
    config.enter_to_continue()
    print("Some example sentences include: " \
    "the car is next to the bus -> o carro está ao lado do autocarro," \
    "The car is in front of three bicycles -> O carro está em frente de três bicicletas," \
    "I am behind the taxi -> estou atrás do táxi" \
    "I am between the car and the bicycle -> Estou entre o carro e a bicicleta")
    config.enter_to_continue()
    print("Note: I am in Portuguese can be written as 'eu (I) estou(am)' or simply 'estou' because the first person pronoun can be dropped in a sentence in portuguese")
    config.enter_to_continue()
    print("And here are the most common transportations in Portuguese:")
    for english, portuguese in transportation.items():
        print(f"{english} : {portuguese}")
    config.enter_to_continue()
    print("Note: The definite articles in portugese are 'O(masculine singular), A(feminine singular), Os(masculine plural), As(feminine plural)'. These articles can make contractions with prepositions such as de(of) to form 'do = de + o', 'da = de + a', 'dos = de + os', 'das = de + as'")
    config.enter_to_continue()
    print("Now let's practice what we have learned with some exercises! Please be mindful of the following:")
    print("Please make sure that your answers are all in lowercase and that you don't leave any space (except between words) when answering")
    print("Please make sure that your keyboard can allow you to type with accents such as á and ã. Many answers require these and it is important for you to be able to type in order to not get flagged as a wrong answer. Additionally not writing with the accents is considered a spelling mistake so it helps you learn the different accents used in basic everyday language.")
    config.enter_to_continue()
