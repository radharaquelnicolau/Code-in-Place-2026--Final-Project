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