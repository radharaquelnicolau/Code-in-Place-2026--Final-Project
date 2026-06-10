"""
This is the greetings and farewells module of Unolingua. This module contains the dictionary with all the greetings and farewells, the different exercises and the different lesson plan for the greetings and farewells will be written. 
"""
import random
#random is used to randomize which word in the dictionary is being tested for this module
greetings = {
    "hello" : "ola",
    "hi" : "oi",
    "good morning" : "bom dia",
    "good afternoon" : "boa tarde",
    "good evening" : "boa noite",
    "how are you?" : "como estás?",
    "I'm fine, thank you." : "estou bem, obrigado.",
}
#dictionary for greetings in portuguese

farewell = {
    "goodbye" : "adeus",
    "goodbye" : "tchau",
    "see you later" : "até logo",
    "see you tomorrow" : "até amanhã",
    "have a nice day" : "tenha um bom dia",
}   
#dictionary for farewells in portuguese

def g_multiple_choice():
    english_greeting = random.choice(list(greetings.keys()))
    #selects a random word from the dictionary in english
    portuguese_greeting = greetings[english_greeting]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_greeting}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(greetings.values())
    #creates a list of the portuguese translations of the greetings to be used as options for the multiple choice question
    random.shuffle(options)
    #shuffles the options so that the correct answer is not always in the same position
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_greeting:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is '{portuguese_greeting}'.")

def f_multiple_choice():
    english_farewell = random.choice(list(farewell.keys()))
    #selects a random word from the dictionary in english
    portuguese_farewell = farewell[english_farewell]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_farewell}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(farewell.values())
    #creates a list of the portuguese translations of the farewells to be used as options for the multiple choice question
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_farewell:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is '{portuguese_farewell}'.")

def gf_fill_in_the_blanks():
    sentences = {
        "_________ estás?" : "como",
        "_________ dia, como estás?" : "bom",
        "Oi, _______ _______, obrigado" : "estou bem",
        "_________ tarde, até logo!" : "boa",
        "_________, tenha um bom dia" : "tchau",
        "_______ noite, até amanhã!" : "boa",
        "tenha um ________ _______" : "bom dia",
        "estou bem, _________": "obrigado",
        "________ logo!" : "até",
    }
    #dictionary of the incomplete sentences with the values being the correct answer to the incomplete sentence
    incomplete_sentence = random.choice(list(sentences.keys()))
    #selects a random incomplete sentence from the dictionary to be used for the fill in the blank exercise
    correct_answer = sentences[incomplete_sentence]
    #saves the correct answer to the incomplete sentence to be used for checking the user's answer
    print(f"Fill in the blank: '{incomplete_sentence}'")
    answer = input("Enter your answer: ")
    #asks the user to fill in the blank and saves their answer to be checked against the correct answer
    if answer == correct_answer:
        #checks if the user's answer is correct by comparing it to the correct answer saved from the dictionary
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is '{correct_answer}'.")

def gf_match_the_word():
    english_words = list(greetings.keys()) + list(farewell.keys())
    portuguese_words = list(greetings.values()) + list(farewell.values())
    #creates a list of all the english words and all the portuguese words from both the greetings and farewells dictionaries to be used for the match the word exercise
    random.shuffle(english_words)
    random.shuffle(portuguese_words)
    #shuffles both lists so that the correct answers are not always in the same position
    print("Match the English word with its Portuguese translation:")
    for i, english_word in enumerate(english_words):
        print(f"{i + 1}. {english_word}")
        #prints out all the english words numbered through enumerate(english_words)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    for j, portuguese_word in enumerate(portuguese_words):
        print(f"{j + 1}. {portuguese_word}")
        #prints out all the portuguese words numbered through enumerate(portuguese_words)
        #the j + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0