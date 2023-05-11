
from pyfiglet import Figlet
import sys
import random

def main():
    # Get command-line arguments
    arguments = sys.argv

    # Create a new instance of the Figlet font renderer
    figlet = Figlet()

    # Get a list of available fonts from the Figlet instance
    fonts = figlet.getFonts()

    # Check the number and type of command-line arguments
    if len(arguments) == 1:
        # If no arguments were given, prompt the user for input
        userinput = input("Input: ")
        # Choose a random font from the available fonts
        random_font = random.choice(fonts)
        # Set the font of the Figlet instance to the random font
        setfont = figlet.setFont(font=random_font)
        # Render the user's input using the selected font
        print(figlet.renderText(userinput))

    elif len(arguments) == 3 and ("-f" in arguments or "--f" in arguments) and arguments[2] in fonts:
        # If the correct arguments were given, prompt the user for input
        userinput = input("Input: ")
        # Set the font of the Figlet instance to the specified font
        setfont = figlet.setFont(font=arguments[2])
        # Render the user's input using the specified font
        print(figlet.renderText(userinput))

    else:
        # If the wrong number or type of arguments were given, exit with an error message
        sys.exit("Invalid usage")

# Call the main function when the script is run
main()
