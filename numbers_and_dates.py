"""
This is the numbers and dates module of Unolingua. This module contains the dictionary with all the numbers and dates, the different exercises and the different lesson plan for the numbers and dates will be written. 
"""
broken_loop = False
#variable that verifies whether the loop for the match the word game has broken so that the game can end
import random
#random is used to randomize which word in the dictionary is being tested for this module
from tabulate import tabulate 
#imports function that allows you to draw tables in terminal
import config
#imports scores, lives and functionality into the module and main
numbers = {
    "one" : "um",
    "two" : "dois",
    "three" : "três",
    "four" : "quatro",
    "five" : "cinco",
    "six" : "seis",
    "seven" : "sete",
    "eight" : "oito",
    "nine" : "nove",
    "ten" : "dez",
}
#dictionary for numbers in portuguese
dates = {
    "today" : "hoje",
    "tomorrow" : "amanhã",
    "yesterday" : "ontem",
    "monday" : "segunda-feira",
    "tuesday" : "terça-feira",
    "wednesday" : "quarta-feira",
    "thursday" : "quinta-feira",
    "friday" : "sexta-feira",
    "saturday" : "sábado",
    "sunday" : "domingo",
    "weekend" : "fim de semana",
    "weekday" : "dia de semana",
}

#dictionary for dates in portuguese
"""Numbers(n) Multiple Choice Exercise"""
def n_multiple_choice():
    english_numbers = random.choice(list(numbers.keys()))
    #selects a random word from the dictionary in english
    portuguese_numbers = numbers[english_numbers]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_numbers}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(numbers.values())
    #creates a list of the portuguese translations of the numbers to be used as options for the multiple choice question
    random.shuffle(options)
    #shuffles the options so that the correct answer is not always in the same position
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_numbers:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        config.user_xp += 5
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately, that is incorrect. The correct answer is '{portuguese_numbers
}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
"""Dates(f) Multiple Choice Exercise"""
def d_multiple_choice():
    english_dates = random.choice(list(dates.keys()))
    #selects a random word from the dictionary in english
    portuguese_dates = dates[english_dates]
    #saves the portuguese translation of the selected english word
    print(f"What is the Portuguese translation of '{english_dates}'?")
    #ask the user to select the correct portuguese translation of the selected english word
    options = list(dates.values())
    #creates a list of the portuguese translations of the dates to be used as options for the multiple choice question
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        #prints out all the options numbered through enumerate(options)
        #the i + 1 is to make sure that the options are correctly numbered starting from 1 instead of 0
    answer = int(input("Enter the number of your answer: "))
    #asks user for the number and convert the number to int value so that operations can be performed
    if options[answer - 1] == portuguese_dates:
    #checks that if the number the user gave corresponds to the correct index of the portuguese translation
        config.user_xp += 5
        print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
    else:
        config.user_lives -= 1
        print(f"Unfortunately, that is incorrect. The correct answer is '{portuguese_dates}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
""" Fill in the blanks exercise for both numbers and dates (nd)"""
def nd_fill_in_the_blanks():
    incomplete_sentences = {
        "___ de semana" : "fim",
        "meio de ______" : "semana",
        "até ______!" : "amanhã",
        "segunda-_____" : "feira",
        "__ lápis" : "um",
        "dois ____": "dias",
        "__, dois, três" : "um",
        "____ sete" : "seis"
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
""" Match the word exercise for both numbers and dates (nd)"""
def nd_match_the_word():
    big_english_words_list = list(numbers.keys()) + list(dates.keys())
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
        if word in numbers:
            portuguese_words.append(numbers[word])
        else:
            portuguese_words.append(dates[word])
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
        if portuguese_answer == numbers.get(word) or portuguese_answer == dates.get(word):
            #checks if the pair is correct based on the numbers dictionary
            config.user_xp += 5
            print(f"Correct! You now have {config.user_xp}xp! You still have {config.user_lives} lives")
        else:
            config.user_lives -= 1
            print(f"Unfortunately that is not correct. The correct answer is '{numbers.get(word) or dates.get(word)}'. You now have {config.user_lives} lives and {config.user_xp}xp.")
            if config.user_lives == 0:
                broken_loop = True
                break
            #if loops check for whether the lives have finished and then changes the broken loop to true and breaks the loop
""" Build a Sentence exercise for both numbers and dates (nd)"""
def nd_build_a_sentence():
    sentences = {
        "I am good today" : "estou bem hoje",
        "weekday" : "dia de semana",
        "One weekend" : "Um fim de semana",
        "yesterday" : "ontem",
        "good night, see you on wednesday" : "boa noite, até quarta-feira",
        "six seven" : "seis sete"
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
""" Lesson plan for numbers and dates (nd)"""
def nd_lesson_plan():
    print("Welcome to our seccond lesson!")
    print("In this lesson, we will be learning about numbers and dates in Portuguese.")
    #introduces the user to the second lesson of unolingua
    config.enter_to_continue()
    #function to make sure that only by pressing enter, will the user continue
    print("Here are numbers 1-10 in Portuguese:")
    for english, portuguese in numbers.items():
        print(f"{english} : {portuguese}")
        #prints each english word with is portuguese translation
    config.enter_to_continue()
    #ensures that next word only shows when pressed enter
    print('Note: 1 and 2 have different spellings depending on the gender of the word (in portuguese, words have gramatical gender). So for example "um lápis" (one pencil) and "uma caneta" (one pen). "um" (masculine) changes to "uma"(feminine). Another example is "dois dias" (two days) and "duas semanas" (two weeks). "dois" (masculine) changes to "duas" (feminine)')
    config.enter_to_continue()
    print("Additionally 'um' and 'uma' also serve as indefinite articles (like a and an) in Portuguese. For example 'um rapaz' (a boy) e 'uma menina' (a girl)")
    config.enter_to_continue()
    print("Note: To spot grammatical gender in Portuguese, check the ending of each word. Feminine words usually end with an -a. Some exceptions we have learned this far are 'dia'(masculine), 'tarde'(feminine), 'noite'(feminine) and 'amanhã'(masculine)")
    config.enter_to_continue()
    print("And here is how you can talk about the days of the week in Portuguese:")
    for english, portuguese in dates.items():
        print(f"{english} : {portuguese}")
    config.enter_to_continue()
    print("Note: When speaking informally, the days of the week (Monday to Friday) are abbreviated so that instead of saying 'Segunda-feira' for Monday, you only say 'Segunda' or 'Terça' for Tuesday, so on and so forth")
    print("Fun Fact: The literal translation of 'Segunda-feira, Terça-feira, Quarta-feira, Quinta-feira and Sexta-feira' to english is 'Second fair, third fair, fourth fair, fifth fair, and sixth fair'. The reason as to why it is like this is because a bishop, Martinho de Braga, did not like the association the days of the week had with the gods in roman culture and decided to change the names during Holy Week with the first fair starting on Sunday.")
    config.enter_to_continue()
    print("Now let's practice what we have learned with some exercises! Please be mindful of the following:")
    print("Please make sure that your answers are all in lowercase and that you don't leave any space (except between words) when answering")
    config.enter_to_continue()
    print("Please make sure that your keyboard can allow you to type with accents such as á and ã. Many answers require these and it is important for you to be able to type in order to not get flagged as a wrong answer. Additionally not writing with the accents is considered a spelling mistake so it helps you learn the different accents used in basic everyday language.")
    config.enter_to_continue()
