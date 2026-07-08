#PixelArt
#Fundamentally doing this through plotting
import numpy as np
import matplotlib.pyplot as plt

#Pixel Art Canvas Setup
#Grayscale: 1=white, 0=black; RGB tuple: colour

#16×16 art
canvas_size = 16
#Empty canvas
pixel_art_canvas = np.ones((canvas_size, canvas_size))

#Display the empty canvas and enlarge the figure size
plt.figure(figsize=(6, 6)) #magnification in width, height
plt.imshow(pixel_art_canvas, cmap='gray', vmin=0, vmax=1)
plt.title(f'Empty {canvas_size}x{canvas_size} Pixel Art Canvas')
plt.xticks(np.arange(-0.5, canvas_size, 1), labels=[]) #no label displayed
plt.yticks(np.arange(-0.5, canvas_size, 1), labels=[])
plt.grid(True, which='both', color='black', linewidth=0.0) #Hides grids
plt.tick_params(axis='both', which='both', length=0) #Hides tick marks
plt.show()

#GRAY ART
pixel_art_canvas[3:5, 3:5] = 0 #left eye [3&4 color black vertically, 3&4 colored black horizontally]
pixel_art_canvas[1, 2:6] = 0 #left eyebrow [vertical position from 0 at top:range to color + 1, horizontal position from 0 at left end:range+1]
pixel_art_canvas[3:5, 11:13] = 0 #right eye
pixel_art_canvas[1, 10:14] = 0 #right eyebrow
pixel_art_canvas[5:8, 8] = 0 #nose bridge
pixel_art_canvas[7, 7] = 0 #nose
pixel_art_canvas[10, 3:13] = 0 #upper lip
pixel_art_canvas[13, 5:11] = 0 #lower lip
pixel_art_canvas[11, 3] = 0
pixel_art_canvas[12, 4] = 0
pixel_art_canvas[11, 12] = 0
pixel_art_canvas[12, 11] = 0

plt.figure(figsize=(6, 6))
plt.imshow(pixel_art_canvas, cmap='gray', vmin=0, vmax=1)
plt.title(f'Sketch on the {canvas_size}x{canvas_size} Pixel Art Canvas')
plt.xticks(np.arange(-0.5, canvas_size, 1), labels=[])
plt.yticks(np.arange(-0.5, canvas_size, 1), labels=[])
plt.grid(True, which='both', color='black', linewidth=0)
plt.tick_params(axis='both', which='both', length=0)
plt.show()

#COLOURS
#Assign 3 values for each pixel (RGB)
canvas_size = 16
pixel_art_canvas_rgb = np.ones((canvas_size, canvas_size, 3)) # White background

#Pre-define colours
BLACK = [0.0, 0.0, 0.0]
DARKSKIN = [0.8, 0.5, 0.5]
RED = [1.0, 0.2, 0.3]
DARKRED = [0.7, 0.0, 0.0]
SKIN = [1, 0.8, 0.8]

pixel_art_canvas_rgb[3:5, 3:5] = BLACK # left eye
pixel_art_canvas_rgb[1, 2:6] = BLACK # left eyebrow
pixel_art_canvas_rgb[3:5, 11:13] = BLACK # right eye
pixel_art_canvas_rgb[1, 10:14] = BLACK # right eyebrow

pixel_art_canvas_rgb[5:8, 8] = DARKSKIN # nose bridge
pixel_art_canvas_rgb[7, 7] = DARKSKIN # nose

pixel_art_canvas_rgb[10, 3:13] = RED # upper lip
pixel_art_canvas_rgb[13, 5:11] = RED # lower lip
pixel_art_canvas_rgb[11, 3] = RED
pixel_art_canvas_rgb[12, 4] = RED
pixel_art_canvas_rgb[11, 12] = RED
pixel_art_canvas_rgb[12, 11] = RED

#rest of the skin
pixel_art_canvas_rgb[0, 0:16] = SKIN #forehead
pixel_art_canvas_rgb[1, 0:2] = SKIN 
pixel_art_canvas_rgb[1, 6:10] = SKIN
pixel_art_canvas_rgb[1, 14:16] = SKIN
pixel_art_canvas_rgb[2, 0:16] = SKIN #eyespace
pixel_art_canvas_rgb[3:5, 5:11] = SKIN
pixel_art_canvas_rgb[3:16, 0:3] = SKIN #left cheek
pixel_art_canvas_rgb[5:10, 3:7] = SKIN
pixel_art_canvas_rgb[5:7, 7] = SKIN
pixel_art_canvas_rgb[3:16, 13:16] = SKIN #right cheek
pixel_art_canvas_rgb[5:10, 9:13] = SKIN
pixel_art_canvas_rgb[8:10, 7:10] = SKIN
pixel_art_canvas_rgb[14:16, 3:13] = SKIN #chin
pixel_art_canvas_rgb[12, 3] = SKIN
pixel_art_canvas_rgb[13, 3:5] = SKIN
pixel_art_canvas_rgb[12, 12] = SKIN
pixel_art_canvas_rgb[13, 11:13] = SKIN
pixel_art_canvas_rgb[12, 5:11] = DARKRED

plt.figure(figsize=(6, 6))
plt.imshow(pixel_art_canvas_rgb) # No cmap needed for RGB data
plt.title(f'Coloured Pixel Attempt')
plt.xticks(np.arange(-0.5, canvas_size, 1), labels=[])
plt.yticks(np.arange(-0.5, canvas_size, 1), labels=[])
plt.grid(True, which='both', color='black', linewidth=0.5) # Re-adding grid for clarity
plt.tick_params(axis='both', which='both', length=0)
plt.show()