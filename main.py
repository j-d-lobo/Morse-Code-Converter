from colorama import Style
import pandas as pd

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

input_string = input("Enter the text you would like to convert: ") # bingus spoingus

INPUT_STRING = input_string.upper() # Converts the input string to uppercase so we don't run into errors w/ lowercase characters

output_list = [] # Empty string to hold the output

for char in INPUT_STRING:
    output_list.append(MORSE_CODE_DICT[char]) # Adds the value of the corresponding key to the output string
    # ['-...', '..', '-.', '--.', '..-', '...', '/', '...', '.--.', '---', '..', '-.', '--.', '..-', '...'] = bingus spoingus

delimiter = " "
output_string = delimiter.join(output_list) # Puts a space between list elements and joins them as a string

print(output_string) # -... .. -. --. ..- ... / ... .--. --- .. -. --. ..- ... much easier to read without the ' ' and ,