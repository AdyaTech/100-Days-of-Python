# Introduction
Cho-han is a dice game played in gambling houses of feudal Japan. Two six-sided dice are rolled in a cup, and gamblers must guess if the sum is even (cho) or odd (han). The house takes a small cut of all winnings. The simple random number generation and basic math used to determine odd or even sums make this project especially suitable for beginners.

# How does Clickbait work?
The random.randint(1, 6) call returns a random integer between 1 and 6, making it ideal for representing a six-sided die roll. However, we also need to display the Japanese words for the numbers one to six. Instead of having an if statement followed by five elif statements, we have a dictionary, stored in JAPANESE_NUMBERS, that maps the integers 1 to 6 to strings of the Japanese words.

# What did we learn?
Carrot in a Box helps us to understand about:

1. random module
2. About randint
