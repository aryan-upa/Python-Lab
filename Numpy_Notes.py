
import numpy as np # here np is an alias, 'false name'.
# import numpy
# from numpy import * # gets all the function by the name, we don't use to call 'em as attributes, takes up lot of space
# from numpy import functions_names # gets only functions, whose names are given.

"""
Numpy is not a standard module, but actually a scientific module for fast array operation.
Numpy -> Numerical Python.
It is used for Multi Dimensional Array.

Q: What is a Package?
A: Package is a folder having modules in it which have functions in it.
    going from package to module we use '.'
    Ex:
        import package.module.function 
"""


lst = [1,2,3,4]
print(lst)  # [1, 2, 3, 4]
arr = np.array(lst)
print(arr)  # [1 2 3 4] # There are no commas in array.
"Array supports the item assignment and can act both as mutable and immutable."
print(type(arr[0]))  # <class 'numpy.int32'> in this we can fix the size of elements.

"""
    1. array(): method in numpy module. Convert the sequence into ndarray.
        Elements in the array must be homogenous.
        
        Arrays are faster than the lists, that's why they are used to store large data and faster operation.
        
        If we have multiple type of elements in an array even in numbers if we have a lower data type with higher one, 
        then it'll convert all the data types into higher data type.
        
            [dtype1, dtype2] -> Resulting data type of array.
            int, float -> float
            int, float, string -> string
            int, string -> string
            
            reshape is a function, while shape is an attribute.
            
    Attributes:
        1. ndim : returns the dimension of the array, 2D, 3D etc.
        2. size : Returns the total number of elements in the array.
        3. shape : Returns the dimension of the array no. of rows and column as per dimension.
        4. dtype : returns the data type of elements in the array.
        5. copy : To create a new copy of that array. Different memory location yet same value.
        6. view : To create a reference of the same data. Same memory location, just a new name to an old object.

    Method:
        1. reshape() : To reshape the array.
        2. arange() : create an array with given range and also works with step as float.
"""

arr = np.array([1, 2, 3, 5.2])
print(arr) # [1.  2.  3.  5.2] all elements are converted into float..

arr = np.array([1,2,'hello',3])
print(arr) # ['1' '2' 'hello' '3'] all elements are converted into strings.


# Using a scalar value generates a 0 Dimensional array.
arr = np.array(23) # Generates an array of 0 Dimension.
print(arr, type(arr), arr.ndim) # 23 <class 'numpy.ndarray'> 0

# > A 1-D Array
" 1D array is known as 1st order tensor. "
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr, type(arr), arr.ndim)  # [1 2 3 4 5 6 7 8 9] <class 'numpy.ndarray'> 1

arr = np.array([1,2,3,4],dtype=np.float64)
print(arr, type(arr), arr.ndim) # [1. 2. 3. 4.] <class 'numpy.ndarray'> 1
"The numpy adds a '.' after integer part but not a zero after unless any other value exist."


print(type(arr)) # <class 'numpy.ndarray'> : Returns data type of array.
print(arr.dtype) # float64 : Returns data type of elements of the given array.
print(arr.shape) # (4,) : For tuple formation a comma is included.
print(arr.size) # 4 : No. of elements in the array.
print(arr.ndim) # 1 : Dimension of array.


"Now by default data of array is of 32bit."
"To change this we do..."
arr = np.array([1,2,3,4,5,6,7,8,9], dtype=np.int8)
print(arr, type(arr), arr.ndim, type(arr[0])) # [1 2 3 4 5 6 7 8 9] <class 'numpy.ndarray'> 1 <class 'numpy.int8'>

arr = np.array([256,257,120,0,128], dtype=np.int8)
print(arr)  # [   0    1  120    0 -128]

"Array also works with reverse indexing."
arr = np.array([1,2,3.3,'hello'])
# By default any data type in this will hold the class of numpy_int, numpy_str_ etc.

arr = np.array([1,2,3.3,'hello'],dtype='object')
# this will make the numpy array act as a list, this will take up a lot of space.
# data type of every variable will be of normal python.


# 2-D Array
" 2D array is known as 2nd order tensors. "

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
# It by default stores the value in this format.
# [[1 2 3]
#  [4 5 6]]

print(arr.shape)
# returns a tuple holding the value Rows and Columns
# (2, 3)

" While changing the dimension it is to keep in mind that the number of elements in the array must be same. "
arr.shape = 3,2  # Changes the current shape of the array.
print(arr)
# [[1 2]
#  [3 4]
#  [5 6]]

print(arr.ndim) # 2 Two Dimensional array
print(arr.size) # 6 : Total number of elements.
print(arr.shape) # (2,3) : This returns the no. Rows vs. Columns

" Reshape Method "
import numpy as np
arr1 = np.array([[2,4],[3,4],[5,6]])
arr2 = arr1.reshape(2,3)
print(arr1)
print(arr2)

"Arr1 : "
# [[2 4]
#  [3 4]
#  [5 6]]

"Arr2 : "
# [[2 4 3]
#  [4 5 6]]

" arange Method "
arr1 = np.arange(1,5,0.2) # This will give a 1D array, further we can use reshape method.
print(arr1)
# [1.  1.2 1.4 1.6 1.8 2.  2.2 2.4 2.6 2.8 3.  3.2 3.4 3.6 3.8 4.  4.2 4.4 4.6 4.8]


" Accessing the Elements in an Array "

arr = np.array([[9,5,4,0],[6,6,2,2],[5,8,1,2],[6,5,4,2]])
print(arr)
# [[9 5 4 0]
#  [6 6 2 2]
#  [5 8 1 2]
#  [6 5 4 2]]

" Whenever we are calling an element in an array we only use 1 square bracket. "
" The method will be row,column "

print(arr[2,2]) # as indexing starts from zero, therefore, 3rd Row, 3rd Column which is 1.
# Prints 1.

" How to do slicing in array. "
# For all elements means all rows all columns
arr[:,:]
# Output is in this format.
# array([[9, 5, 4, 0],
#        [6, 6, 2, 2],
#        [5, 8, 1, 2],
#        [6, 5, 4, 2]])

arr[:1,1:3]  # In this we are slicing b/w in 0th Row and 1th and 2th Column therefore the elements are 5,4.
# array([[5, 4]]) : As we are searching in a 2D array then the result will also be a 2D matrix.

# Array also works in negative index.

"""
    Unknown Dimension
    We are allowed to have one unknown dimension in the array, provided that number of elements must be the same.
    To do this we pass '-1' to the dimension function as a parameter.
    We can not pass -1 to more than one parameter.
"""

"""
Flattening of the arrays.
    Converting the multi Dimensional array into a 1D array.
    
    1. Using shape
"""

L = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr = np.array(L)
arr.shape = (8,) # We give tuple to shape, As single data in tuple goes with a comma.
print(arr) # 1D Array -> [1 2 3 4 5 6 7 8]

# When we write (8,) it is not an array with 1 row and 8 column, it is a 1D array so it
# not have the concept of rows and column, it's just data in a single line.
# But when we write, (1,8) then it'll create a 2D array with 1 row and 8 columns.

"""
    2. Using reshape
"""

L = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr = np.array(L)
b = arr.reshape(-1) # In reshape we pass parameters, Unknown Dimension will do it itself .
print(b) # arr remains unaffected, [1, 2, 3, 4, 5, 6, 7, 8]

"""
    3. Using flatten function : No need to pass parameter, It does its job by default.
"""

L = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr = np.array(L)
b = arr.flatten()
print(b) # arr remains unaffected, [1, 2, 3, 4, 5, 6, 7, 8]

"""
    4. Using ravel function 
"""

L = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr = np.array(L)
b = arr.ravel() # Returns a flattened array.
print(b) # arr remains unaffected, [1, 2, 3, 4, 5, 6, 7, 8]

"""
Transposing an array
    Changing Rows into Columns.
    
    Ways:
    1. Using T : attribute.
"""

L = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr = np.array(L)
arr = arr.T
print(arr) # Returns a matrix with rows and columns interchanged.

"""
    2. Using transpose : method
"""

L = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr = np.array(L)
arr = arr.T
print(arr) # Returns a matrix with rows and columns interchanged.

"""
    3. Using transpose : function
"""

L = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr = np.array(L)
arr = np.transpose(arr)
print(arr) # Returns a matrix with rows and columns interchanged.

# Return in each case :
# [[1 5]
#  [2 6]
#  [3 7]
#  [4 8]]

"""
To add two arrays : 
"""

L1 = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr1 = np.array(L1)
L2 = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr2 = np.array(L2)

arr3 = arr1+arr2
print(arr3)

# [[ 2  4  6  8]
#  [10 12 14 16]]

"""
To subtract two arrays : 
"""

L1 = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr1 = np.array(L1)
L2 = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr2 = np.array(L2)

arr3 = arr1-arr2
print(arr3)

# [[0 0 0 0]
#  [0 0 0 0]]

"""
To multiply two arrays : 
"""

L1 = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr1 = np.array(L1)
L2 = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr2 = np.array(L2)

arr3 = arr1*arr2
print(arr3)

# [[ 1  4  9 16]
#  [25 36 49 64]]

"""
To divide two arrays : 
"""

L1 = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr1 = np.array(L1)
L2 = [[1,2,3,4],[5,6,7,8]] # 2D Array
arr2 = np.array(L2)

arr3 = arr1/arr2
print(arr3)

# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]


" Matrix Operation in Array : "

# Matrix Multiplication
# We have dot function in Numpy which multiply matrices.

mat1 = np.array([[1,2,3],[4,5,6]])
mat2 = np.array([[1,2],[3,5],[4,5]])

if mat1.shape[1] == mat2.shape[0]:
    print(np.dot(mat1,mat2))
    # The result :
    # [[19 27]
    #  [43 63]]
else:
    print("Invalid Operation.")

# The multiply function works on element to element

mat1 = np.array([[1,2,3],[4,5,6]])
mat2 = np.array([[1,2,3],[4,5,6]])

print(np.multiply(mat1,mat2))
# The Result :
# [[ 1  4  9]
#  [16 25 36]]

" For sum, subtraction, division etc we have different functions "
" Like np.sum, etc. "


# Sin and Cosine in numpy
import numpy as np
import matplotlib.pyplot as plt
# Matplotlib is a package and pyplot is a module which helps in plotting the graphs.
x_axis = np.arange(0,11,.05)
y_data1 = np.sin(x_axis)
y_data2 = np.cos(x_axis)

# plt.plot function plots the graph while, plt.show shows the plotted graphs.
plt.plot(x_axis, y_data1, color='Crimson', linewidth=4)
plt.plot(x_axis, y_data2, color='Purple', linewidth=2)
plt.show()

# around function in numpy
# For rounding off the data in an array.
a = np.array([1.01,1.564,1.456,5.6454,9.4,2.546,56.1654])
print('Original Array : ',a)
print('After Rounding off : ',end='')
print(np.around(a)) # [ 1.  2.  1.  6.  9.  3. 56.]
print("When Decimal is 1 : ",end='')
print(np.around(a, decimals=1)) # [ 1.   1.6  1.5  5.6  9.4  2.5 56.2]

# Similarly we have ceil and floor with the same function.

"Array as Image"
import numpy as np
mat = np.ones([3,3,2]) # Row, Column, Depth
# Returns a matrix of given size but all elements are one.
print(mat)

# [[[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]]

"For just the same function but with zeroes we have a function np.zeroes. "
"to show this data in the form of image we use matplotlib.pyplot and function imshow."

import numpy as np
import matplotlib.pyplot as plt
import random as rd
mat = np.zeros([100,100])
plt.imshow(mat) # shows a completely dark image as all values are zero
for i in range(0,100,5):
    mat[:,i] = rd.random() # Makes all rows of ith column as value given by random.
for i in range(0,100,5):
    mat[i,:] = rd.random() # Makes all column of ith row as value given by random.
mat[:,99] = 1
mat[99,:] = 1
plt.imshow(mat)

# Gives a graph, try and run it.

# Array Sum
" Axis 1 is from left to right. "
" Axis 0 is from top to bottom. "
lst = [1,2,3,4,5,6,7,8,9,10]
arr = np.array(lst)
s = np.sum(arr) # By default the axis is 0, so doing this will print the sum of data
# in the axis 0, means complete row. In 1D there is no other axis.
print(s)

# For a 2D Array
lst = [[1,2,3,4,5],[6,7,8,9,10]]
arr = np.array(lst)
print(arr)
s = np.sum(arr,axis=0)
print(s)

# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
# as axis is 0, Column Wise Sum is clearly visible.
# [ 7  9 11 13 15]

s = np.max(arr,axis=1) # this would return an array of elements, having the maximum value in axis 1,
# which is row-wise. No. of elements in return will be equal to no. of rows.
print(s)
# [ 5 10] # Prints max value of row1 and row2.

"linspace"
"returns the data in given start and end and having no. of elements."
"it calculates itself and gives that no. of elements including start and stop. "

arr = np.linspace(1,10,100) # Start Stop and no. of elements
print(arr) # prints a 1D Data in the array.
# we can also change the shape using attribute, method or function.
print(arr.reshape(10,10)) # Returns a 2D array having 10 rows and 10 columns.

" To calculate the size of an array "
k = [1,2,3,4,5,6,7,8,9,1232,64546,654,65,64,654,846,1354]
import sys
print(sys.getsizeof(k[0])*len(k),' bytes is the size of list.') # 238 Bytes
arr = np.array(k)
print(arr.size*arr.itemsize,' bytes is the size of array.') # 68 Bytes


"eye function to get Identity matrix."

import numpy as np
mat = np.eye(5) # Gives a 5*5 Identity Matrix.
print(mat)

# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

