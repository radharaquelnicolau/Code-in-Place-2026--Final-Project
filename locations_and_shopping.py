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
    "the bus stop" : "a paragem de autocarro",
    "the station" : "a estação",
    "the street" : "rua",
    "the house" : "a casa",
    "the school" : "a escola",
    "where is.....?" : "onde fica?",
    "how do I get to....?" : "como chego a?",
    "the bank" : "o banco",
    "the park" : "o parque"
}
#dictionary for locations in portuguese
shopping = {
    "how much?" : "quanto custa?",
    "I want this." : "eu quero isso",
    "the shop" : "a loja",
    "the supermarket" : "o supermercado",
    "water" : "a água",
    "bread" : "o pão",
    "fruit" : "a fruta",
    "vegetables" : "os vegetais",
    "coffee" : "o café",
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
        "a _______ de autocarro" : "paragem",
        "onde ____ o parque?" : "fica",
        "os ________" : "vegetais",
        "eu _____ isso" : "quero",
        "como _____ à estação" : "chego",
        "a paragem de _________" : "autocarro",
        "____ fica o banco?" : "onde",
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
    global broken_loop
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
        "good morning, where is the station?" : "bom dia, onde fica a estação?",
        "the school is behind the street" : "a escola fica atrás da rua",
        "good afternoon , how much is the bread?" : "boa tarde, quanto custa o pão?",
        "I am next to the park" : "eu estou ao lado do parque",
        "I want this" : "eu quero isso",
        "how do I get to the bank?" : "como chego ao banco?"
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
    print("Welcome to our fourth lesson!")
    print("In this lesson, we will be learning about common locations and shopping vocabulary in Portuguese.")
    #introduces the user to the first lesson of unolingua
    config.enter_to_continue()
    #function to make sure that only by pressing enter, will the user continue
    print("Here are the some common locations in Portuguese:")
    for english, portuguese in locations.items():
        print(f"{english} : {portuguese}")
        #prints each english word with is portuguese translation
    config.enter_to_continue()
    #ensures that next word only shows when pressed enter
    print('Note: The same way bus has two different Portuguese translations, bus stop has two Portuguese translations. In European Portuguese, bus stop is "paragem de autocarro" while in Brazilian Portuguese is "parada de ônibus"')
    config.enter_to_continue()
    print("Note: The letter 'a' not only is used as a definite article but also as preposition that links places, direction, time and final destination (similar to 'by' and 'to'). 'a' the preposition can be contracted with the definite articles 'o' and 'a' as follows: 'a + o' = 'ao' and 'a + a' = 'à'. These contractions are used in place of having these two in a sentence and is the most correct way of writing. ")
    config.enter_to_continue()
    print("And here is the most common shopping vocabulary in Portuguese:")
    for english, portuguese in shopping.items():
        print(f"{english} : {portuguese}")
    config.enter_to_continue()
    print("Note: You can say 'quanto custa?' with an item so you would say 'quanto custa os vegetais?' (how much are the vegetables?) if you are specifically asking about an item and you are not pointing at it. Same thing with 'Eu quero isso.' 'Isso' is a demonstrative equivalent to 'this' or 'that'. You can swap it for the actual item and say 'Eu quero o pão' (I want the bread).")
    config.enter_to_continue()
    print("Now let's practice what we have learned with some exercises! Please be mindful of the following:")
    print("Please make sure that your answers are all in lowercase and that you don't leave any space (except between words) when answering")
    print("Please make sure that your keyboard can allow you to type with accents such as á and ã. Many answers require these and it is important for you to be able to type in order to not get flagged as a wrong answer. Additionally not writing with the accents is considered a spelling mistake so it helps you learn the different accents used in basic everyday language.")
    config.enter_to_continue()
