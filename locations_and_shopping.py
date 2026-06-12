"""
This is the locations and shoppings module of Unolingua. This module contains the dictionary with all the locations and shopping vocabulary, the different exercises and the different lesson plan for the locations and shopping will be written. 
"""
broken_loop = False
#variable that verifies whether the loop for the match the word game has broken so that the game can end
import random
#random is used to randomize which word in the dictionary is being tested for this module
from tabulate import tabulate 
#imports function that allows you to draw tables in terminal
import config
#imports scores, lives and functionality into the module and main
locations = {
    "hello" : "olá",
    "hi" : "oi",
    "good morning" : "bom dia",
    "good afternoon" : "boa tarde",
    "good evening/night" : "boa noite",
    "how are you?" : "como estás?",
    "I'm fine, thank you, and you?" : "estou bem, obrigado, e você?"
}
#dictionary for locations in portuguese
shopping = {
    "goodbye" : "tchau",
    "see you later" : "até logo",
    "see you tomorrow" : "até amanhã",
    "have a nice day" : "tenha um bom dia",
}   
#dictionary for shopping vocab in portuguese
"""Locations(l) Multiple Choice Exercise"""
def l_multiple_choice():
    english_location = random.choice(list(locations.keys()))
    #selects a random word from the dictionary in english
    portuguese_location = locations[english_location]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_location}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(locations.values())
    #creates a list of the portuguese translations of the locations to be used as options for the multiple choice question
    random.shuffle(options)
    #shuffles the options so that the correct answer is not always in the same position
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_location:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        config.user_xp += 5
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately, that is incorrect. The correct answer is '{portuguese_location}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
"""Shopping(s) Multiple Choice Exercise"""
def s_multiple_choice():
    english_shopping = random.choice(list(shopping.keys()))
    #selects a random word from the dictionary in english
    portuguese_shopping = shopping[english_shopping]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_shopping}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(shopping.values())
    #creates a list of the portuguese translations of the shoppings to be used as options for the multiple choice question
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_shopping:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        config.user_xp += 5
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately, that is incorrect. The correct answer is '{portuguese_shopping}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
""" Fill in the blanks exercise for both locations and shopping (ls)"""
def ls_fill_in_the_blanks():
    incomplete_sentences = {
        "____ estás?" : "como",
        "___ dia, como estás?" : "bom",
        "oi, _____ ___, obrigado" : "estou bem",
        "___ tarde, até logo!" : "boa",
        "_____, tenha um bom dia" : "tchau",
        "___ noite, até amanhã!" : "boa",
        "tenha um ___ ___" : "bom dia",
        "estou bem, ________": "obrigado",
        "___ logo!" : "até",
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
""" Match the word exercise for both locations and shopping (ls)"""
def ls_match_the_word():
    big_english_words_list = list(locations.keys()) + list(shopping.keys())
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
        if word in locations:
            portuguese_words.append(locations[word])
        else:
            portuguese_words.append(shopping[word])
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
        if portuguese_answer == locations.get(word) or portuguese_answer == shopping.get(word):
            #checks if the pair is correct based on the locations dictionary
            config.user_xp += 5
            print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
        else:
            config.user_lives -= 1
            print(f"Unfortunately that is not correct. The correct answer is '{locations.get(word) or shopping.get(word)}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
            if config.user_lives == 0:
                broken_loop = True
                break
            #if loops check for whether the lives have finished and then changes the broken loop to true and breaks the loop
""" Build a Sentence exercise for both locations and shopping (ls)"""
def ls_build_a_sentence():
    sentences = {
        "good morning, how are you?" : "bom dia, como estás",
        "hello, I am fine, thank you" : "olá, estou bem, obrigado",
        "good afternoon, see you soon!" : "boa tarde, até logo!",
        "goodbye, have a nice day" : "tchau, tenha um bom dia",
        "good night, see you tomorrow" : "boa noite, até amanhã",
        "I am fine, thank you and you?" : "estou bem, obrigada, e você?"
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
""" Lesson plan for locations and shoppings (ls)"""
def ls_lesson_plan():
    print("Now let's start with our first lesson!")
    print("In this lesson, we will be learning about common locations and shoppings in Portuguese.")
    #introduces the user to the first lesson of unolingua
    config.enter_to_continue()
    #function to make sure that only by pressing enter, will the user continue
    print("Here are the most common locations in Portuguese:")
    for english, portuguese in locations.items():
        print(f"{english} : {portuguese}")
        #prints each english word with is portuguese translation
    config.enter_to_continue()
    #ensures that next word only shows when pressed enter
    print('Note: when someone asks "Estou bem, obrigado, e você?" you can respond with "Estou bem, obrigado"')
    config.enter_to_continue()
    print("Note: Words like 'obrigado' usually change spelling depending on the gender of who is talking. For example, if a woman is speaking, they say 'obrigada'. However for this program we will be using 'obrigado' througout")
    config.enter_to_continue()
    print("Also, there are two ways of saying you in Portuguese: 'você' and 'tu'. 'Você' is more commonly used in Brazil while 'tu' is more commonly used in Portugal. Additionally 'tu' is considered more informal while 'você' is considered more formal. For this program we will be using 'você' throughout")
    config.enter_to_continue()
    print("And here are the most common shoppings in Portuguese:")
    for english, portuguese in shopping.items():
        print(f"{english} : {portuguese}")
    config.enter_to_continue()
    print("Note: there are two forms of saying goodbye in Portuguese: 'tchau' and 'adeus'. 'Tchau' is for when you know you are meeting the person again while 'adeus' is for when you don't know if you are meeting the person again")
    config.enter_to_continue()
    print("Now let's practice what we have learned with some exercises! Please be mindful of the following:")
    print("Please make sure that your answers are all in lowercase and that you don't leave any space (except between words) when answering")
    print("Please make sure that your keyboard can allow you to type with accents such as á and ã. Many answers require these and it is important for you to be able to type in order to not get flagged as a wrong answer. Additionally not writing with the accents is considered a spelling mistake so it helps you learn the different accents used in basic everyday language.")
    config.enter_to_continue()
