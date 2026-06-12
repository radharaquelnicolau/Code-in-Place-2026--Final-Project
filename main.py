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
    greetings_and_farewell.gf_lesson_plan()
    config.enter_to_continue()
    greetings_and_farewell.g_multiple_choice()
    config.enter_to_continue()
    greetings_and_farewell.f_multiple_choice()
    config.enter_to_continue()
    greetings_and_farewell.gf_fill_in_the_blanks()
    config.enter_to_continue()
    greetings_and_farewell.gf_match_the_word()
    config.enter_to_continue()
    greetings_and_farewell.gf_build_a_sentence()
    print(f"Congratulations on completing the first lesson! You have earned a total of {config.user_xp}xp and have {config.user_lives} lives remaining.")


if __name__ == "__main__":
    main()