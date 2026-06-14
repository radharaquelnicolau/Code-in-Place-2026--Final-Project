# Code in Place 2026 Final Project
## Unolingua

Unolingua is a Duolingo-inspired command line program for learning Portuguese, 
submitted as a final project for Code in Place 2026. It was inspired by the 
Quizlet exercise from Week 6 of the course.

## What is Unolingua?

Unolingua is a Python terminal program that teaches beginner Portuguese (European Portuguese). The vocabulary covered is aimed at A1 level and is organised into 5 lessons:

1. Greetings and Farewells
2. Numbers and Dates
3. Directions and Transportation
4. Locations and Shopping
5. Common Phrases

Between lessons, you will also learn fun facts about wider Portuguese-speaking world.

Each lesson begins with a vocabulary sheet and cultural notes, followed by 7 randomised exercises including multiple choice, fill in the blank, match the word and build a sentence.

Like Duolingo, you earn XP for every correct answer and lose lives for mistakes. Each player starts with 5 lives — if you lose them all, the lesson restarts from the beginning. Your XP carries over across all lessons.

## How to run it

Make sure you have Python 3 installed, then install the one dependency(run this command at the terminal):

pip install tabulate
or
pip install -r requirements.txt

Then run:

python main.py

## Notes

- All answers must be typed in lowercase
- Accented characters (á, ã, ê etc.) are required for correct answers
- The program teaches European Portuguese — some vocabulary differs 
  from Brazilian Portuguese

## About

Built by Radha Raquel Nicolau  as a final project for 
[Code in Place 2026](https://codeinplace.stanford.edu/).

Thank you for trying Unolingua. Happy learning!
