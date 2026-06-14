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
fun_facts = [
    {
        "country": "Portugal",
        "fact": "Lisbon is older than Rome! The Phoenicians settled there around 1200 BCE, making it one of the oldest cities in Europe — Rome wasn't founded until around 753 BCE."
    },
    {
        "country": "Portugal",
        "fact": "Portugal produces over 70% of the world's cork exports and is home to the world's largest cork forest. Cork handbags, wallets and accessories are popular souvenirs!"
    },
    {
        "country": "Portugal",
        "fact": "Livraria Bertrand in Lisbon, founded in 1732, holds the Guinness World Record for the oldest operating bookstore in the world — it's still open today!"
    },
    {
        "country": "Brazil",
        "fact": "Brazil is the world's largest coffee producing country, filling an estimated 66 million 60kg bags of coffee in a single year. Coffee is central to daily life there!"
    },
    {
        "country": "Brazil",
        "fact": "Brazil has the largest Japanese population outside of Japan, mostly living in Sao Paulo. This has led to events like the annual Japan Festival, the biggest celebration of Japanese culture in Latin America!"
    },
    {
        "country": "Brazil",
        "fact": "Brazil's capital, Brasilia, was purpose-built and designed in the shape of an airplane when viewed from above. It only became the capital in 1961, replacing Rio de Janeiro."
    },
    {
        "country": "Mozambique",
        "fact": "Mozambique has over 40 languages spoken within its borders, making most Mozambicans naturally multilingual. Portuguese serves as the common language between all these different groups."
    },
    {
        "country": "Mozambique",
        "fact": "The rallying cry of Mozambique's independence movement — 'A luta continua!' (the struggle continues) — is still used by activist movements around the world fighting for equal rights today."
    },
    {
        "country": "Angola",
        "fact": "Music genres Kizomba, Kuduro and Semba all originated in Angola and are now enjoyed worldwide. Next time you hear Kizomba at a party, you'll know where it came from!"
    },
    {
        "country": "The Lusophone World",
        "fact": "Portuguese is spoken by around 260 million people across 4 continents and 9 countries, making it the most spoken language in the Southern Hemisphere — more than Spanish or French!"
    }
]
#dictionary contatining fun facts that will show inbetween each lesson
def main():
    print("Welcome to Unoligua, the language learning game! In this game, you will be able to practice and learn a new language through various exercises and activities. You will earn points for completing exercises and lose lives for making mistakes. The goal is to earn as many points as possible while keeping your lives intact. Let's get started!")
    config.enter_to_continue()
    print("Unolingua will be teaching you Portuguese, a beautiful and widely spoken language originating from Portugal. Portuguese is the official language of 9 different countries, with the biggest population of native Portuguese speakers being in Brazil, Angola and Portugal. It is a Romance language that evolved from Latin and has many similarities to Spanish and Italian. Learning Portuguese will open up a world of opportunities for you, whether it's for travel, work, or simply to connect with people from different cultures. Let's dive into the first lesson and start learning Portuguese together!")
    config.enter_to_continue()
    print("Before we start, you will receive experience(xp) points based on how well you do on each exercise and the type of exercise it is. You will also have 5 lives, and you will lose a life for each mistake you make. If you lose all your lives, the lesson will start over and you regain all your lives. So, make sure to pay attention and do your best to earn as many points as possible while keeping your lives intact. Good luck and have fun learning Portuguese with Unoligua!")
    config.enter_to_continue()
    # Explanatory text for Unolingua
    greetings_and_farewell_lesson()
    show_fun_fact()
    print("Now let's go to our next lesson!")
    numbers_and_dates_lesson()
    show_fun_fact()
    print("Now let's go to our next lesson!")
    directions_and_transportation_lesson()
    show_fun_fact()
    print("Now let's go to our next lesson!")
    locations_and_shopping_lesson()
    show_fun_fact()
    common_phrases_lesson()
    print("Congratulations on finishing Unolingua! I hope Unolingua felt like a tangible first step in grasping the beautiful Portuguese language. I recommend you don't stop your Portuguese journey here. Here are some resources that you can use to continue your Portuguese speaking journey:")
    config.enter_to_continue()
    print("Firstly, you can always use Duolingo. Unolingua was a passion project heavily inspired by Duolingo so I would recommend you go there first." \
    "I also recommend Memrise. It is an app similar to Duo but it uses spaced repitition which helps with retention.")
    config.enter_to_continue()
    print("Some websites I would recommend are Loecsen and PortuguesePod101. PortuguesePod101 also has a youtube channel and a podcast which is incredibly useful for pronunciation and just learning how the language is actually spoken.")
    config.enter_to_continue()
    print("Finally, for sites I would recommend for live practice. I would recommend italki and preply. Both have Portuguese tutors who can help you with conversation practice.")
    config.enter_to_continue()
    print("Once again, thank you so much for trying out Unolingua. Unolingua was submitted as a final project for Code in Place 2026. It is my first proper python project. However, I do understand that it is not perfect and there is a lot of room for growth. I appreciate everyone that tried Unolingua out and wish the best of luck to all of you!")

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
            if config.user_lives == 0 or greetings_and_farewell.broken_loop == True:
                print("You have lost all your lives. The lesson will now start over. Don't worry, you can do it! Just pay attention and try your best to earn points while keeping your lives intact. Good luck!")
                config.user_lives = 5
                greetings_and_farewell.broken_loop = False
                break
            #if statment checks for whether the lives are finished or the break loop variable for match a word is true so that the lesson can restart
        else:
            break
        #breaks because the user has completed the exercises without losing all lives
    print(f"Congratulations on completing the first lesson! You have earned a total of {config.user_xp}xp")
    config.enter_to_continue()
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
                numbers_and_dates.broken_loop = False
                break
            #if statment checks for whether the lives are finished or the break loop variable for match a word is true so that the lesson can restart
        else:
            break
        #breaks because the user has completed the exercises without losing all lives
    print(f"Congratulations on completing the second lesson! You have earned a total of {config.user_xp}xp")
    config.enter_to_continue()
#function of gameloop of directions and transportation
def directions_and_transportation_lesson():
    while True:
        #ensures that this loops repeats when you lose all lives
        directions_and_transportation.dt_lesson_plan()
        #displays gf lesson plan first
        dt_exercise_list = [directions_and_transportation.d_multiple_choice, directions_and_transportation.t_multiple_choice, directions_and_transportation.dt_fill_in_the_blanks, directions_and_transportation.dt_fill_in_the_blanks, directions_and_transportation.dt_match_the_word, directions_and_transportation.dt_build_a_sentence, directions_and_transportation.dt_build_a_sentence]
        #list of all functions being used so that the functions can be shuffled and not used in order
        random.shuffle(dt_exercise_list)
        #shuffles the list so that functions are not in the same order as in the module file
        for exercise in dt_exercise_list:
            exercise()
            config.enter_to_continue()
            #for loop runs through all the functions in the list
            if config.user_lives == 0 or directions_and_transportation.broken_loop == True:
                print("You have lost all your lives. The lesson will now start over. Don't worry, you can do it! Just pay attention and try your best to earn points while keeping your lives intact. Good luck!")
                config.user_lives = 5
                directions_and_transportation.broken_loop = False
                break
            #if statment checks for whether the lives are finished or the break loop variable for match a word is true so that the lesson can restart
        else:
            break
        #breaks because the user has completed the exercises without losing all lives
    print(f"Congratulations on completing the third lesson! You have earned a total of {config.user_xp}xp")
    config.enter_to_continue()
#function of gameloop of locations and shopping 
def locations_and_shopping_lesson():
    while True:
        #ensures that this loops repeats when you lose all lives
        locations_and_shopping.ls_lesson_plan()
        #displays gf lesson plan first
        ls_exercise_list = [locations_and_shopping.l_multiple_choice, locations_and_shopping.s_multiple_choice, locations_and_shopping.ls_fill_in_the_blanks, locations_and_shopping.ls_fill_in_the_blanks, locations_and_shopping.ls_match_the_word, locations_and_shopping.ls_build_a_sentence, locations_and_shopping.ls_build_a_sentence]
        #list of all functions being used so that the functions can be shuffled and not used in order
        random.shuffle(ls_exercise_list)
        #shuffles the list so that functions are not in the same order as in the module file
        for exercise in ls_exercise_list:
            exercise()
            config.enter_to_continue()
            #for loop runs through all the functions in the list
            if config.user_lives == 0 or locations_and_shopping.broken_loop == True:
                print("You have lost all your lives. The lesson will now start over. Don't worry, you can do it! Just pay attention and try your best to earn points while keeping your lives intact. Good luck!")
                config.user_lives = 5
                locations_and_shopping.broken_loop = False
                break
            #if statment checks for whether the lives are finished or the break loop variable for match a word is true so that the lesson can restart
        else:
            break
        #breaks because the user has completed the exercises without losing all lives
    print(f"Congratulations on completing the fourth lesson! You have earned a total of {config.user_xp}xp")
    config.enter_to_continue()
#function of gameloop for common phrases
def common_phrases_lesson():
    while True:
        #ensures that this loops repeats when you lose all lives
        common_phrases.c_lesson_plan()
        #displays gf lesson plan first
        c_exercise_list = [common_phrases.c_multiple_choice, common_phrases.c_multiple_choice, common_phrases.c_fill_in_the_blanks, common_phrases.c_fill_in_the_blanks, common_phrases.c_match_the_word, common_phrases.c_build_a_sentence, common_phrases.c_build_a_sentence]
        #list of all functions being used so that the functions can be shuffled and not used in order
        random.shuffle(c_exercise_list)
        #shuffles the list so that functions are not in the same order as in the module file
        for exercise in c_exercise_list:
            exercise()
            config.enter_to_continue()
            #for loop runs through all the functions in the list
            if config.user_lives == 0 or common_phrases.broken_loop == True:
                print("You have lost all your lives. The lesson will now start over. Don't worry, you can do it! Just pay attention and try your best to earn points while keeping your lives intact. Good luck!")
                config.user_lives = 5
                common_phrases.broken_loop = False
                break
            #if statment checks for whether the lives are finished or the break loop variable for match a word is true so that the lesson can restart
        else:
            break
        #breaks because the user has completed the exercises without losing all lives
    print(f"Congratulations on completing the last lesson! You have earned a total of {config.user_xp}xp")
    config.enter_to_continue()
#function that displays fun facts 
def show_fun_fact():
    fact = random.choice(fun_facts)
    #picks a random country for the fun fact
    print("=" * 50)
    #prints an equal sign 50 times to create a barrier and to differentiate from actual content
    print(f"Did you know? [{fact['country']}]")
    print(f"{fact['fact']}")
    #prints the country and a fun fact
    print("=" * 50)
    config.enter_to_continue()

if __name__ == "__main__":
    main()