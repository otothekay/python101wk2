# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC

## Week 2 Lesson 2

## Problems
### 1

#Write a script that
#* generates an array of numbers from 16-100,000 with a stride of 4.
#* reshape it to a 2083 rows by 12 columns
#* print out the first 3 and last 3 rows

import numpy as np
from numpy import ndarray

my_array: ndarray = np.array(range(16,100000,4))
reshaped = my_array.reshape(2083,12)
print(reshaped[:3])
print(reshaped[:-3])



### 2
#Build an numpy array WITH named types

second_array = np.array(range(1,10)).astype(int)
print(second_array.dtype)
print(second_array)

### 3
#Build a numpy array of ones called "A"
#* take a slice out and call that slice by variable "B".
#* multiply B by 5 or a slice of B by 5
#* print(A)
#* repeat above WITHOUT or WITH changing the value of "A"

A = np.ones(10)
B = A[:5]
C = B*5
print(A)  #value of A doesn't change
A[:5] = C #value of A does change
print(A)


### 4
#Take the mode of the data in the last example
A[5] = 1
values, counts = np.unique(A,return_counts=True)
print(values, counts)



### 5
#Read in a csv file but use dtype 'U5' for the header

data = np.genfromtxt('Hawaii.csv', delimiter=',',dtype=None,encoding=None)
print(data)
data[1:-1,0:-1].astype(float)
#I don't know why the above isn't converting the table values
# to floats that are rows non in the header.
print(data)