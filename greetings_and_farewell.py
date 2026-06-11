"""
This is the greetings and farewells module of Unolingua. This module contains the dictionary with all the greetings and farewells, the different exercises and the different lesson plan for the greetings and farewells will be written. 
"""
import random
#random is used to randomize which word in the dictionary is being tested for this module
from tabulate import tabulate 
#imports function that allows you to draw tables in terminal
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
""" Greetings(g) Multiple Choice Exercise"""
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
""" Farewell(f) Multiple Choice Exercise"""
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
""" Fill in the blanks exercise for both greetings and farewells (gf)"""
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
""" Match the word exercise for both greetings and farewells (gf)"""
def gf_match_the_word():
    big_english_words_list = list(greetings.keys()) + list(farewell.keys())
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
        if word in greetings:
            portuguese_words.append(greetings[word])
        else:
            portuguese_words.append(farewell[word])
    #for loop checks each word in the english list and adds portuguese translation based on which dictionary the word is in
    random.shuffle(english_words)
    random.shuffle(portuguese_words)
    #shuffles both english and portuguese lists so that the words and the answers are not together
    complete_list = list(zip(english_words, portuguese_words))
    #combines the english and portuguese lists into a list of tuples to be used for the match the word exercise
    headers = ["English", "Portuguese"]
    #headers for the table
    print(tabulate(complete_list, headers=headers, tablefmt="simple_grid"))
    #prints table using complete list data
    print("Match the english word to the portuguese word")
    for i in range(5):
        english_answer = input("Enter the English word: ")
        portuguese_answer = input("Enter the Portuguese word: ")
        #asks users to write the pair of both english and portuguese words
        if (english_answer, portuguese_answer) == (english_answer, greetings[english_answer]):
            #checks if the pair is correct based on the greetings dictionary
            print("Correct!")
        elif (english_answer, portuguese_answer) == (english_answer, farewell[english_answer]):
            #checks if the pair is correct based on the farewell dictionary
            print("Correct!")
        else:
            print(f"Wrong! The pair was {english_answer} and {greetings.get(english_answer) or farewell.get(english_answer)}.")