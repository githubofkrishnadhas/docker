import sys
import random
from colorama import init, Fore

# Initialize colorama
init()

def print_with_random_color(text):
    """
    Print text with a randomly selected color.
    """
    color = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN])
    print(color + text)

# Add default print statement with instructions
print("Welcome! To print text with random colors, used the following syntax inside:")
print("python app.py 'Your text here'")
print("Enjoy the colorful output!")
print("As a docker image use like: docker run -it <imagename>")
print("Eg: docker run -it colorama-print-app")
print("Enter your input once prompted.if empty input is provided default statement is printed.")

# Check if a command-line argument is provided
if len(sys.argv) > 1:
    input_text = sys.argv[1]
else:
    # Read from standard input
    input_text = input("Enter your text: ")

# Validate user input
if input_text.strip():
    print_with_random_color(input_text)
else:
    # Perform sample function call with default string
    default_text = "Welcome to Colorama print app!!"
    print_with_random_color(default_text)
