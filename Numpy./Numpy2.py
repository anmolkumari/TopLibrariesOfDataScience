

import numpy as np 
#array1
l1 = [[1,2,3],[4,5,6]]
a1 = np.array(l1)
print(a1)

#array2
l2 = [[1,2,3],['a','b','c']]
a2 = np.array(l2)
print(a2)

#array3
l3 = [[1,2], [3,4]]
a3 = np.array(l3, dtype=float)
print(a3)
#array4
a4 = np.array(l3, dtype=complex)
print(a4)

''' data types defined in numpy
bool_
int_
intc
intp
int8
int16
int32
int64
uint8
uint16
uint32
uint64
float_
float16
float32
float64
complex_
complex64
complex128
'''

#dtype object (data type objects)

dt1 = np.dtype(np.int32)
print(dt1)

dt2 = np.dtype('i1')
print(dt2)

dt3 = np.dtype('i2')
print(dt3)

dt4 = np.dtype('i4')
print(dt4)

dt4 = np.dtype('i8')
print(dt4)

# creating structured data type
dt5 = np.dtype([('age',np.int8)])
print(dt5)

a5 = np.array([15,20,25,30],dtype= dt5)
print(a5)
print(a5['age'])

# b is byte 
# creating our own ndarray
edt = np.dtype([('name','S30'), ('age','i1'), ('salary','f4') ])
employee = np.array([('anshu',20,25000.0), ('muskaan',21,26000.0), ('tanvi',21,27000.0)], dtype=edt)
print(employee)
print(employee['name'])
print(employee['age'])



#attributes 
# 1. shape (returns tuple)
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr.shape)

# 2. resize the array
arr.shape = (2,6)
print(arr)

#reshape()
arr = arr.reshape(4,3)
print(arr)

# 3. ndim
print(arr.ndim)

temp = np.array([[[1,2],[3,4]]])
print(temp)
print(temp.shape)
print(temp.ndim)


# arange() returns the array of evenly spaced numbers
# np.arange(start, stop, step, dtype), stop excluded
a6 = np.arange(24)
print(a6)
# ndim returns the dimensions of array
print(a6.ndim)

a7 = a6.reshape(2,4,3)
print(a6)
print(a7)
print(a6.ndim)
print(a7.ndim)

# itemsize returns the size of element of array

d1 = np.array([1,2,3], dtype=np.int8)
print(d1.itemsize) #int8 = 1 byte
d2 = np.array([1,2,3], dtype=np.float64)
print(d2.itemsize) #float64 = 8 bytes

# flags
print(d2.flags)

#empty creates unintialised array of specified shape and dtype
#np.empty(shape, dtype)
emptyArr = np.empty([4,2], dtype=np.int8)
print(emptyArr)

#zeros creates an array filled with zeros
#np.zeros(shape,dtype)
#default dtype is float
zerosArr = np.zeros([4,2], dtype=np.int8)
print(zerosArr)

#structured type
z1 = np.zeros([4,2], dtype=[('x','i1'),('y','i1')])
print(z1)
print(z1['x'])

#ones creates an array filled with ones
onesArr = np.ones([4,2], dtype=np.int8)
print(onesArr)


#creating an array from existing data
# asarray is used
#list to aaray
list1 = [1,2,3,4,5]
listToArray = np.asarray(list1)
print(listToArray)

#when dtype is defined
listToArray1 = np.asarray(list1, dtype=np.float64)
print(listToArray1)

#tuple to array
tuple1 = (1,2,3,4,5)
tupleToArray = np.asarray(tuple1)
print(tupleToArray)

#list of tuples to array
listOfTuples = [(1,2,3),(4,5,6)]
listOfTuplesArr = np.asarray(listOfTuples)
print(listOfTuplesArr)

# np.frombuffer is used to create an array from any object that exposes from buffer
s1 = b'from buffer'
ar = np.frombuffer(s1, dtype='S1')
print(ar)

#np.fromiter is used to create an array from any iterable object
list2 = range(10)
fromIterArr = np.fromiter(list2, dtype=np.float32)
print(fromIterArr)

#np.linspace() 
#np.logspace()

#python slice object is constructed by slice() with parameters start, stop, step
ar1 = np.arange(10)
slice1 = slice(2,8,2)
print(ar1[slice1])

# method 2 - slicing
print(ar1[2:8:2])

#broadcasting
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print(c)

a = np.array([1,2,3]) 
b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
c = a + b
print(c)

# np.nditer - multidimensional iterator object to iterate over an array 
iterArr = np.arange(12)
iterArr = iterArr.reshape(3,4)
for x in np.nditer(iterArr):
	print(x)

#The order of iteration is chosen to match the memory layout of an array, without considering a
# particular ordering. This can be seen by iterating over the transpose of the above array.
x1 = iterArr.T
for x in np.nditer(x1):
	print(x)


a = x1.copy(order='C')
print('C-style order: ')
for x in np.nditer(a):
	print(x)

b = x1.copy(order='F')
print('F-style order: ')
for x in np.nditer(b):
	print(x)

#forcing nditer to print in a specified manner
x1 = iterArr.T
for x in np.nditer(x1, order='C'):
	print(x)


# printing two different array simultaneously
a = np.arange(0,60,5) 
a = a.reshape(3,4)
b = np.array([1, 2, 3, 4], dtype = np.int8)
for x,y in np.nditer([a,b]): 
   print("%d:%d"%(x,y))