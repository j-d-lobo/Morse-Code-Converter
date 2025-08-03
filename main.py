import os
import sys
from colorama import Style, Fore
from banner import banner

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

RunStatus = True
# ========================================================================================================================
# MAIN LOOP 
# ========================================================================================================================
while(RunStatus):
    print(f"{Style.BRIGHT + Fore.CYAN}{banner}{Style.RESET_ALL}")

    input_string = input(f"Enter the text you would like to convert: {Style.BRIGHT + Fore.GREEN}") # bingus spoingus

    INPUT_STRING = input_string.upper() # Converts the input string to uppercase so we don't run into errors w/ lowercase characters

    output_list = [] # Empty string to hold the output

    for char in INPUT_STRING:
        output_list.append(MORSE_CODE_DICT[char]) # Adds the value of the corresponding key to the output string
        # ['-...', '..', '-.', '--.', '..-', '...', '/', '...', '.--.', '---', '..', '-.', '--.', '..-', '...'] = bingus spoingus

    delimiter = " "
    output_string = delimiter.join(output_list) # Puts a space between list elements and joins them as a string

    print(f"{Style.RESET_ALL}--> {Style.BRIGHT + Fore.GREEN}{output_string}{Style.RESET_ALL}") # -... .. -. --. ..- ... / ... .--. --- .. -. --. ..- ... much easier to read without the ' ' and ,

    # ====================================================================================================================
    # CONTINUE CHECK LOOP 
    # ====================================================================================================================
    ContinueCheck = True
    while(ContinueCheck):
        action = input(f"Would you like to continue? (Y/N): {Style.BRIGHT + Fore.RED}")

        ACTION = action.upper()
        if ACTION == "Y":
            ContinueCheck = False # Exits the Continue Check loop
            os.system("cls") # Clears Command Prompt
            break
        elif ACTION == "N": 
            ContinueCheck = False # Exits the Continue Check loop
            RunStatus = False # Sets the RunStatus variable to False making it so the main loop doesn't run again
            break
        else: 
            print(f"{Style.RESET_ALL}Invalid Input!")
    # ====================================================================================================================
    # END OF CONTINUE CHECK LOOP
    # ====================================================================================================================

# ========================================================================================================================
# END OF MAIN LOOP
# ========================================================================================================================
