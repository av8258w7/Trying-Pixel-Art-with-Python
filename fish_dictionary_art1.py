#FishArtMap1
import numpy as np
import matplotlib.pyplot as plt

canvas_size = 16
pixel_art_canvas_text = np.ones((canvas_size, canvas_size, 3)) #blank canvas with RGB

# Mapping colors to letters in dictionary 
text_colors = {
    'W': [1.0, 1.0, 1.0],  #White
    'X': [0.0, 0.0, 0.0],  #Black
    'R': [1.0, 0.0, 0.0],  #Red
    'G': [0.0, 1.0, 0.0],  #Green
    'B': [0.0, 0.0, 1.0],  #Blue
    'Y': [1.0, 1.0, 0.0],  #Yellow
    'P': [0.5, 0.0, 0.5],  #Purple
    'O': [1.0, 0.5, 0.0],  #Orange
    'L': [0.7, 0.9, 1.0], #Light blue
}

#Art mapping
pixel_art_text = """
BBBBBBBBBBBBBBBB
BBLWBBBBBBBBBBBB
BBLLBBBOBBBBBBBB
BBBBBOOOBBBBBBBB
BBBYYYYYYBBBOBBB
BBBYXYYYYYBOOBBB
BBYYYYOOYYOOOBBB
BBYYYYYOYYOOOBBB
BBBYYYYYYYBOOBBB
BBBYYYYYYBBBOBBB
BBBBBOOOBBBBBBBB
BBLLBBBOBBBBBBBB
BBLWBBBBBBBBBBBB
BBBBBBBBBBBBBBBB
BBBBBLBBBBBBBBBB
BBBBBBBBBBBBBBBB
"""


lines = [line for line in pixel_art_text.strip().split('\n') if line.strip()]
#line is appended to the list for every element in pixel_art_text
#Clears leading and trailing blank spaces, and splits the whole string into multiple smaller string
#if any newline command is included. Otherwise the whole row is a single list and output as such.
#appending continues until /if condition of line.strip becomes False. For any non empty character the boolean is True.
#list = [expression /for item /in iterable /if condition]
#list = [expression_if_true /if condition /else expression_if_false /for item /in iterable]
 

# Ensure the input text matches the canvas size
if len(lines) != canvas_size or any(len(line) != canvas_size for line in lines):
    print(f"Warning: Text art dimensions ({len(lines)}x{len(lines[0])}) do not match canvas size ({canvas_size}x{canvas_size}).") #rows×columns
    #len(lines) gives the number of 'lines' elements in the list lines, and len(lines[0]) gives the number of elements in the string lines (1st row)
else: #when written art matches canas size
    for r, line in enumerate(lines): #go row-wise from 0 to last index-wise
        for c, char in enumerate(line): #go column-wise in one row at a time and read the assigned char
            if char in text_colors: #if char is defined, map and output the assigned value into the list where the char was
                pixel_art_canvas_text[r, c] = text_colors[char]
            else:
                print(f"Warning: Character '{char}' not found in color mapping. Using white.")
                pixel_art_canvas_text[r, c] = text_colors[' ']


plt.figure(figsize=(6, 6))
plt.imshow(pixel_art_canvas_text)
plt.title(f'Mapped art')
plt.xticks(np.arange(-0.5, canvas_size, 1), labels=[])
plt.yticks(np.arange(-0.5, canvas_size, 1), labels=[])
plt.grid(True, which='both', color='black', linewidth=0)
plt.tick_params(axis='both', which='both', length=0)
plt.show()