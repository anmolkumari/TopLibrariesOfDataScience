import numpy as np 

#creating an array
x=np.array([1,2,3,4,5,6])
print(x)

#traversal
print(x[0])

#generating random value from gaussian distribution in a shape given
y=np.random.randn(2,3)
print(y)

#slicing 

k=x[:5:2]
print(k)

k=x[:5]
print(k)

#printing axes
print(x.ndim)

#printing type
print(type(x))

#saving 
np.save('val',x)

#shape
print(x.shape)
 #size
print(x.size)
#data type of values inside array
print(x.dtype)

#arange: returns evenly spaced values within a given interval. step size is specified.
print(np.arange(0,50,5))

# Creating array from list with type String
sarr = np.array([['a', 'b', 'c'], ['d', 'e', 'f']], dtype = 'object') 
print ("Array created using passed list:\n", sarr)

# Creating a 3X4 array with all zeros 
c = np.zeros((3, 4)) 
print ("\nAn array initialized with all zeros:\n", c) 

dt = np.dtype(np.int8)
print(dt)