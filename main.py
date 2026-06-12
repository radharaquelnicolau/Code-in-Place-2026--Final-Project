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
    print("Unolingua will be teaching you Portuguese, a beautiful and widely spoken language originating from Portugal. Portuguese is the official language of 9 different countries, with the biggest population of native Portuguese speakers being in Brazil, Angola and Portugal. It is a Romance language that evolved from Latin and has many similarities to Spanish and Italian. Learning Portuguese will open up a world of opportunities for you, whether it's for travel, work, or simply to connect with people from different cultures. Let's dive into the first lesson and start learning Portuguese together!")
    print(f"Before we start, you will receive experience(xp) points based on how well you do on each exercise and the type of exercise it is. You will also have 5 lives, and you will lose a life for each mistake you make. If you lose all your lives, the lesson will start over. So, make sure to pay attention and do your best to earn as many points as possible while keeping your lives intact. Good luck and have fun learning Portuguese with Unoligua!")
    greetings_and_farewell_lesson()
"""     while True:
        greetings_and_farewell.gf_lesson_plan()
        gf_exercise_list = [greetings_and_farewell.g_multiple_choice, greetings_and_farewell.f_multiple_choice, greetings_and_farewell.gf_fill_in_the_blanks, greetings_and_farewell.gf_fill_in_the_blanks, greetings_and_farewell.gf_match_the_word, greetings_and_farewell.gf_build_a_sentence, greetings_and_farewell.gf_build_a_sentence]
        random.shuffle(gf_exercise_list)
        for exercise in gf_exercise_list:
            exercise()
            config.enter_to_continue()
            if config.user_lives == 0 or greetings_and_farewell.broken_loop == True:
                print("You have lost all your lives. The lesson will now start over. Don't worry, you can do it! Just pay attention and try your best to earn points while keeping your lives intact. Good luck!")
                config.user_lives = 5
                break
        else:
            break
    print(f"Congratulations on completing the first lesson! You have earned a total of {config.user_xp}xp and have {config.user_lives} lives remaining.") """


def greetings_and_farewell_lesson():
    while True:
        greetings_and_farewell.gf_lesson_plan()
        gf_exercise_list = [greetings_and_farewell.g_multiple_choice, greetings_and_farewell.f_multiple_choice, greetings_and_farewell.gf_fill_in_the_blanks, greetings_and_farewell.gf_fill_in_the_blanks, greetings_and_farewell.gf_match_the_word, greetings_and_farewell.gf_build_a_sentence, greetings_and_farewell.gf_build_a_sentence]
        random.shuffle(gf_exercise_list)
        for exercise in gf_exercise_list:
            exercise()
            config.enter_to_continue()
            if config.user_lives == 0 or greetings_and_farewell.broken_loop == True:
                print("You have lost all your lives. The lesson will now start over. Don't worry, you can do it! Just pay attention and try your best to earn points while keeping your lives intact. Good luck!")
                config.user_lives = 5
                break
        else:
            break
        print(f"Congratulations on completing the first lesson! You have earned a total of {config.user_xp}xp and have {config.user_lives} lives remaining.")
    

if __name__ == "__main__":
    main()