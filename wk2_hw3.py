# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC

## Week 2 Lesson 3

# q1: Why is np.transpose(img, (1, 0, 2)) NOT the same as np.rot90(img)?

# ANS: transpose is a matrix operation that converts rows to columns.  Done visually, this results in something
# than rotating the image 90 degrees.

##HW

# q2: Use a *for* loop to create the figures in the following code.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread

file_nm = "classlogo.png"
img = imread(file_nm) ## Note we do not have to close this
img.shape #(500,300,4) Look an alpha channel
# Lets view it But rotated
A = np.transpose(img, (1, 0, 2)).copy()
B = np.rot90(img).copy()  ## We need to copy() here if we want a new object
plt.figure("A")
plt.imshow(A) #Make an image plot object
plt.figure("B")
plt.imshow(B) #Make an image plot object
plt.figure("classlogo")
plt.imshow(img)
plt.show()  # Display it to screen
plt.close()  # Make sure everything is closed

fig_list = [A, B, img]
fig_names = ["a", "b", "logo"]

for figs, names in zip(fig_list, fig_names):
    plt.figure("names")
    plt.imshow(figs)
    plt.show()

## HW

# When importing the following: numpy and pandas, what is the common alias used.

# ANS:   numpy as np, pandas as pd