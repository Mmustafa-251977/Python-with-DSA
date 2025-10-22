#Lets begin with the basic code of Hello World code in python.
# this module contains Only print statement with escape sequence 
print("hello world")

# let's  per form more python code with print method
# lets print the two lines of the code 

print("Hello ")
print("Happy Coding !!")

# But we cannot use multiple print statement for multiple lines so there are some Escape sequences that are used for the print the multiple lines in single print statement 

#  To print the new line code in the python 
print("\nthis is the the sentence \nthis is used to go for the next line ")
print("\nTwinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nWhen the blazing sun is gone,\nWhen he nothing shines upon,\nThen you show your little light,\nTwinkle, twinkle, all the night.\nThen the trav'ller in the dark,\nThanks you for your tiny spark,\nHe could not see which way to go,\nIf you did not twinkle so.\nIn the dark blue sky you keep,\nAnd often thro' my curtains peep,\nFor you never shut your eye,\nTill the sun is in the sky.\n'Tis your bright and tiny spark,\nLights the trav'ller in the dark:\nTho' I know not what you are,\nTwinkle, twinkle, little star.")

#There are more types of the the escape sequence in the python 
# Let's dive into escape characters in depth.
# Common sequences: \n (newline), \t (tab), \\ (backslash), \' (single quote), \" (double quote)

# \n - Newline
print ("Hello \nWorld")

# \t - tab 
print("Hello \tWorld")

# \\ - Backslash

print("Hello \\World")

# \' - single quote 

print("\'Life is a difficult game. You can win it only by retaining your birthright to be a person.\'")

# \" - double quote 

print("\"Dream is not that which you see while sleeping it is something that does not let you sleep.\"")


# \r: Carriage return (moves the cursor to the beginning of the current line, potentially overwriting previous text).

# Raw string (useful for Windows paths, regex patterns)
print(r"Raw string: C:\new_folder\test.txt")
import time
print("Initial message...")
time.sleep(2)
print("\rNew message overwrites the old one.")

# \r ensures that the "Progress" message is updated on the same line, creating a visual progress bar effect. 

# """ - Triple quote is used for the highlight one word in sentnece 

print("""This is the "Triple quote" in the line """)

# sep and end - these are used for the seprate the string contents in between the lines

print ("This", "is", "my","name", sep=" " ,end="!")
print("\napple","banana","grapes", sep="\n", end="..")
print("\nHello", "World", sep="---", end="!\n")


# f- 'f' before a string denotes an f-string, also known as a formatted string literal. Introduced in Python 3.6, f-strings provide a concise and readable way to embed expressions and variables directly within string literals.

name = "Alice"
sentnce= f"Hello {name}\nWelcome to Python!"
print(sentnce)

# Unicode escapes
print("Unicode examples: \u2602 \u00A9")

# Including both single and double quotes using triple quotes
print('''She said, "It's a beautiful day!"''')