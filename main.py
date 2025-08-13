# import os
# import sys
# from colorama import Style, Fore
# from banner import banner
from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
from PIL import Image, ImageTk

FONT = "Courier"
GRAY = "#737373"
CYAN = "#5ce1e6"

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

MORSE_TO_EN_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
# print(MORSE_TO_EN_DICT) # Troubleshooting

# # RunStatus = True # Normal Runtime Variable
# RunStatus = False # GUI Testing
# # ========================================================================================================================
# # MAIN LOOP 
# # ========================================================================================================================
# while(RunStatus):
#     print(f"{Style.BRIGHT + Fore.CYAN}{banner}{Style.RESET_ALL}")

#     input_string = input(f"Enter the text you would like to convert: {Style.BRIGHT + Fore.GREEN}") # bingus spoingus

#     INPUT_STRING = input_string.upper() # Converts the input string to uppercase so we don't run into errors w/ lowercase characters

#     output_list = [] # Empty string to hold the output

#     for char in INPUT_STRING:
#         output_list.append(MORSE_CODE_DICT[char]) # Adds the value of the corresponding key to the output string
#         # ['-...', '..', '-.', '--.', '..-', '...', '/', '...', '.--.', '---', '..', '-.', '--.', '..-', '...'] = bingus spoingus

#     delimiter = " "
#     output_string = delimiter.join(output_list) # Puts a space between list elements and joins them as a string

#     print(f"{Style.RESET_ALL}--> {Style.BRIGHT + Fore.GREEN}{output_string}{Style.RESET_ALL}") # -... .. -. --. ..- ... / ... .--. --- .. -. --. ..- ... much easier to read without the ' ' and ,

#     # ====================================================================================================================
#     # CONTINUE CHECK LOOP 
#     # ====================================================================================================================
#     ContinueCheck = True
#     while(ContinueCheck):
#         action = input(f"Would you like to continue? (Y/N): {Style.BRIGHT + Fore.RED}")

#         ACTION = action.upper()
#         if ACTION == "Y":
#             ContinueCheck = False # Exits the Continue Check loop
#             os.system("cls") # Clears Command Prompt
#             break
#         elif ACTION == "N": 
#             ContinueCheck = False # Exits the Continue Check loop
#             RunStatus = False # Sets the RunStatus variable to False making it so the main loop doesn't run again
#             break
#         else: 
#             print(f"{Style.RESET_ALL}Invalid Input!")
#     # ====================================================================================================================
#     # END OF CONTINUE CHECK LOOP
#     # ====================================================================================================================

# # ========================================================================================================================
# # END OF MAIN LOOP
# # ========================================================================================================================

Active_Language = "English"
Translate_Language = "Morse"

# Clear command
def clear():
    Input_box.delete(0, END)
    Output_box.config(state= "normal")
    Output_box.delete(0, END)
    Output_box.config(state= "readonly")

# Switch command
def switch():
    global Active_Language
    global Translate_Language
    if Active_Language == "English":
        Active_Language = "Morse"
        Translate_Language = "English"
        print(Active_Language) # Troubleshooting
    else:
        Active_Language = "English"
        Translate_Language = "Morse"
        print(Active_Language) # Troubleshooting
    clear()
    Input_label.config(text= f"{Active_Language} :")
    Output_label.config(text= f"{Translate_Language} :")


# Convert command
def convert():
    global Active_Language
    output_list = [] # Empty string to hold the output
    Input_string = Input_box.get()
    if Active_Language == "English":
        INPUT = Input_string.upper()
        for char in INPUT:
            output_list.append(MORSE_CODE_DICT[char]) # Adds the value of the corresponding key to the output string
            # ['-...', '..', '-.', '--.', '..-', '...', '/', '...', '.--.', '---', '..', '-.', '--.', '..-', '...'] = bingus spoingus

        delimiter = " "
    else:
        # NOTE: When converting from Morse to English, you have a string like this: -... .. -. --. ..- ... / ... .--. --- .. -. --. ..- ...
        #       That string would convert to bingus spoingus, however instead the converter spits out TEEEEETETTEEETEEE EEEETTETTTEETETTEEETEEE
        #       Why? 
        #           Because it is looking at each - and . as an individual character where a . is an E, and a - is a T
        #       How to fix?
        #           Need to make a step where we make the list group - and .'s as Morse characters so a -... would be a B
        INPUT = Input_string.split(" ") # Splits the string into a list, where each item is what was in the input string separated by " "
        print(INPUT) # Troubleshooting
        for char in INPUT:            
            if char == " ": # Spaces are used to make the Morse translation easier, but they translate to nothing
                pass        # To avoid KeyError: " ", when that value comes up, simply skip it
            else:
                output_list.append(MORSE_TO_EN_DICT[char])
        
        delimiter = ""
    output_string = delimiter.join(output_list)
    Output_box.config(state= "normal")
    Output_box.insert(0, output_string)
    Output_box.config(state="readonly")
    print(output_string) # Troubleshooting
    return output_string

# Table command
def table():
    popup_window = Toplevel(master= window)
    popup_window.title("Morse Code Table")
    popup_window.wm_attributes("-topmost", True)
    popup_window.geometry("750x450+0+0")

    canvas2 = Canvas(popup_window, width= 750, height= 450, bg= "white", highlightthickness= 0)
    img = ImageTk.PhotoImage(Image.open("Day 82\Morse-Code-Converter\morsecode-1.png"))
    canvas2.create_image(375, 225, image= img)
    canvas2.pack(padx= 10, pady= 10)

    popup_window.mainloop() # Without popup_window.mainloop() the canvas is generated but the image is not

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.geometry("1750x750+100+100")
window.minsize(height= 250, width= 250) # Creates a 240px x 240px window
window.config(padx= 50, pady= 50, bg= GRAY) # 50px of padding on each edge of the window 100 in the x, 100 in the y
window.title("Morse Code Converter")

canvas = Canvas(width= 500, height= 500, bg= GRAY, highlightthickness= 0)
Logo = PhotoImage(file= "Day 82\Morse-Code-Converter\morse converter.png")
canvas.create_image(250, 250, image= Logo)
canvas.grid(column= 1, row= 0, columnspan= 4)

Notice_label = Label(text= "When writing in Morse, separate characters with [space] and identify spaces with [/]", 
                     font= (FONT, 16, "bold"),
                     bg= GRAY,
                     highlightthickness= 0)
Notice_label.grid(column= 1, row= 1, columnspan= 4)


Input_label = Label(text= f"{Active_Language}: ", font= (FONT, 16, 'bold'), bg= GRAY, highlightthickness= 0)
Input_label.grid(column= 0, row= 2)

Input_box = Entry(width= 250)
Input_box.focus() # Makes it so the cursor starts here
Input_box.grid(column= 1, row= 2, columnspan= 4)

Output_label = Label(text= f"{Translate_Language}: ", font= (FONT, 16, 'bold'), bg= GRAY, highlightthickness= 0)
Output_label.grid(column= 0, row= 3)

Output_box = Entry(width= 250, state= "readonly")
Output_box.grid(column= 1, row= 3, columnspan= 4)

Switch_button = Button(text= "Switch", 
                       font= (FONT, 16, "bold"),
                       bg = CYAN,
                       command= switch,
)
Switch_button.grid(column=1, row=4)

Convert_button = Button(text= "Convert", 
                       font= (FONT, 16, "bold"),
                       bg = CYAN,
                       command= convert,
)
Convert_button.grid(column=2, row=4)

Clear_button = Button(text= "Clear", 
                       font= (FONT, 16, "bold"),
                       bg = CYAN,
                       command= clear,
)
Clear_button.grid(column=3, row=4)

Table_button = Button(text= "Table", 
                       font= (FONT, 16, "bold"),
                       bg = CYAN,
                       command= table,
)
Table_button.grid(column=4, row=4)

window.mainloop()