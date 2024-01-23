import os
import shutil

# Function to draw a split line
def draw_split_line():
    # Get the size of the terminal window
    columns, _ = shutil.get_terminal_size()
    # Print a line of dashes equal to the width of the terminal
    print('=' * columns)

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux (os.name: 'posix')
    else:
        os.system('clear')
