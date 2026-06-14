"""
This is the common phrases module of Unolingua. This module contains the dictionary with all the common_phrases, the different exercises and the different lesson plan for the common_phrases will be written. 
"""
broken_loop = False
#variable that verifies whether the loop for the match the word game has broken so that the game can end
import random
#random is used to randomize which word in the dictionary is being tested for this module
from tabulate import tabulate 
#imports function that allows you to draw tables in terminal
import config
#imports scores, lives and functionality into the module and main
common_phrases = {
    "thank you" : "obrigado",
    "you're welcome" : "de nada",
    "excuse me" : "com licença",
    "sorry" : "desculpe",
    "yes" : "sim",
    "no" : "não",
    "what is your name?" : "qual é o seu nome?",
    "my name is..." : "meu nome é",
    "where are you from?" : "de onde você é?",
    "I am from" : "eu sou de",
    "do you speak english?" : "você fala inglês?",
    "I don't understand" : "eu não entendo",
}
#dictionary for common_phrases in portuguese

"""common_phrases(c) Multiple Choice Exercise"""
def c_multiple_choice():
    english_phrases = random.choice(list(common_phrases.keys()))
    #selects a random word from the dictionary in english
    portuguese_phrases = common_phrases[english_phrases]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_phrases}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(common_phrases.values())
    #creates a list of the portuguese translations of the common_phrases to be used as options for the multiple choice question
    random.shuffle(options)
    #shuffles the options so that the correct answer is not always in the same position
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_phrases:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        config.user_xp += 5
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately, that is incorrect. The correct answer is '{portuguese_phrases}'. You now have {config.user_lives} lives and {config.user_xp}xp.")

""" Fill in the blanks exercise for common_phrases (c)"""
def c_fill_in_the_blanks():
    incomplete_sentences = {
        "__ nada" : "de",
        "com _______" : "licença",
        "qual é _ ___ ____" : "o seu nome",
        "o ___ ____ é..." : "meu nome",
        "de onde ____ _" : "você é",
        "__ ___ __..." : "eu sou de",
        "tenha um ___ ___" : "bom dia",
        "você fala ______?" : "inglês",
        "eu ___ _______" : "não entendo",
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
""" Match the word exercise for common_phrases (c)"""
def c_match_the_word():
    big_english_words_list = list(common_phrases.keys())
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
            portuguese_words.append(common_phrases[word])
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
        if portuguese_answer == common_phrases.get(word):
            #checks if the pair is correct based on the common_phrases dictionary
            config.user_xp += 5
            print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
        else:
            config.user_lives -= 1
            print(f"Unfortunately that is not correct. The correct answer is '{common_phrases.get(word)}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
            if config.user_lives == 0:
                broken_loop = True
                break
            #if loops check for whether the lives have finished and then changes the broken loop to true and breaks the loop
""" Build a Sentence exercise for common_phrases (c)"""
def c_build_a_sentence():
    #dictionary of the  sentences with the values being the correct translation to the sentence
    sentence = random.choice(list(common_phrases.keys()))
    #selects a random incomplete sentence from the dictionary to be used for the fill in the blank exercise
    correct_answer = common_phrases[sentence]
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
""" Lesson plan for common_phrases (c)"""
def c_lesson_plan():
    print("Welcome to our last lesson!")
    print("In this lesson, we will be learning about common phrases in Portuguese.")
    #introduces the user to the first lesson of unolingua
    config.enter_to_continue()
    #function to make sure that only by pressing enter, will the user continue
    print("Here are the most common phrases in Portuguese:")
    for english, portuguese in common_phrases.items():
        print(f"{english} : {portuguese}")
        #prints each english word with is portuguese translation
    config.enter_to_continue()
    #ensures that next word only shows when pressed enter
    print("This our last lesson. These are common everyday phrases that every beginner should at least know to get around Portuguese speaking countries. I hoped you enjoyed learning with Unolingua and I hope that you can continue learning Portuguese after Unolingua!")
    config.enter_to_continue()
    print("Please make sure that your answers are all in lowercase and that you don't leave any space (except between words) when answering")
    print("Please make sure that your keyboard can allow you to type with accents such as á and ã. Many answers require these and it is important for you to be able to type in order to not get flagged as a wrong answer. Additionally not writing with the accents is considered a spelling mistake so it helps you learn the different accents used in basic everyday language.")
    config.enter_to_continue()
