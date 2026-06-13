"""
This is the main file for Unoligua. This is where the logic and the 
game loop of the program will be implemented. This file will import 
the other modules and then use the functions from those modules to 
create the game. The main function will be the entry point of the 
program and will call the other functions to run the game. The game
 will consist of various exercises in the different modules to help 
 users learn the language. The program will also include a scoring 
 system to track the user's progress and provide feedback on their 
 performance. Overall, this file will serve as the central hub for 
 the Unoligua program, coordinating all the different components and 
 ensuring a smooth and engaging user experience.
"""
import random
#random will be used to mix the different exercise types for each module currently since each module is not finished, it is currenlty not in use.
import config
#config keeps track of scores and lives. it also contains the press enter to continue function which will be used for functionality in all the files 
import greetings_and_farewell
import numbers_and_dates
import directions_and_transportation
import locations_and_shopping
import common_phrases
#these imports are the different language modules have the different exercise types for each module, they will be used to create the different exercises for the user to practice and learn the language.
def main():
    print("Welcome to Unoligua, the language learning game! In this game, you will be able to practice and learn a new language through various exercises and activities. You will earn points for completing exercises and lose lives for making mistakes. The goal is to earn as many points as possible while keeping your lives intact. Let's get started!")
    config.enter_to_continue()
    print("Unolingua will be teaching you Portuguese, a beautiful and widely spoken language originating from Portugal. Portuguese is the official language of 9 different countries, with the biggest population of native Portuguese speakers being in Brazil, Angola and Portugal. It is a Romance language that evolved from Latin and has many similarities to Spanish and Italian. Learning Portuguese will open up a world of opportunities for you, whether it's for travel, work, or simply to connect with people from different cultures. Let's dive into the first lesson and start learning Portuguese together!")
    config.enter_to_continue()
    print("Before we start, you will receive experience(xp) points based on how well you do on each exercise and the type of exercise it is. You will also have 5 lives, and you will lose a life for each mistake you make. If you lose all your lives, the lesson will start over and you regain all your lives. So, make sure to pay attention and do your best to earn as many points as possible while keeping your lives intact. Good luck and have fun learning Portuguese with Unoligua!")
    config.enter_to_continue()
    # Explanatory text for Unolingua
    greetings_and_farewell_lesson()
    print("Now let's go to our next lesson!")
    numbers_and_dates_lesson()

#function for gameloop of greetings and farewell
def greetings_and_farewell_lesson():
    while True:
        #ensures that this loops repeats when you lose all lives
        greetings_and_farewell.gf_lesson_plan()
        #displays gf lesson plan first
        gf_exercise_list = [greetings_and_farewell.g_multiple_choice, greetings_and_farewell.f_multiple_choice, greetings_and_farewell.gf_fill_in_the_blanks, greetings_and_farewell.gf_fill_in_the_blanks, greetings_and_farewell.gf_match_the_word, greetings_and_farewell.gf_build_a_sentence, greetings_and_farewell.gf_build_a_sentence]
        #list of all functions being used so that the functions can be shuffled and not used in order
        random.shuffle(gf_exercise_list)
        #shuffles the list so that functions are not in the same order as in the module file
        for exercise in gf_exercise_list:
            exercise()
            config.enter_to_continue()
            #for loop runs through all the functions in the list
            if config.user_lives == 0 or numbers_and_dates.broken_loop == True:
                print("You have lost all your lives. The lesson will now start over. Don't worry, you can do it! Just pay attention and try your best to earn points while keeping your lives intact. Good luck!")
                config.user_lives = 5
                break
            #if statment checks for whether the lives are finished or the break loop variable for match a word is true so that the lesson can restart
        else:
            break
        #breaks because the user has completed the exercises without losing all lives
    print(f"Congratulations on completing the first lesson! You have earned a total of {config.user_xp}xp")

#function of gameloop of numbers and dates
def numbers_and_dates_lesson():
    while True:
        #ensures that this loops repeats when you lose all lives
        numbers_and_dates.nd_lesson_plan()
        #displays gf lesson plan first
        nd_exercise_list = [numbers_and_dates.n_multiple_choice, numbers_and_dates.d_multiple_choice, numbers_and_dates.nd_fill_in_the_blanks, numbers_and_dates.nd_fill_in_the_blanks, numbers_and_dates.nd_match_the_word, numbers_and_dates.nd_build_a_sentence, numbers_and_dates.nd_build_a_sentence]
        #list of all functions being used so that the functions can be shuffled and not used in order
        random.shuffle(nd_exercise_list)
        #shuffles the list so that functions are not in the same order as in the module file
        for exercise in nd_exercise_list:
            exercise()
            config.enter_to_continue()
            #for loop runs through all the functions in the list
            if config.user_lives == 0 or numbers_and_dates.broken_loop == True:
                print("You have lost all your lives. The lesson will now start over. Don't worry, you can do it! Just pay attention and try your best to earn points while keeping your lives intact. Good luck!")
                config.user_lives = 5
                break
            #if statment checks for whether the lives are finished or the break loop variable for match a word is true so that the lesson can restart
        else:
            break
        #breaks because the user has completed the exercises without losing all lives
    print(f"Congratulations on completing the first lesson! You have earned a total of {config.user_xp}xp")


if __name__ == "__main__":
    main()