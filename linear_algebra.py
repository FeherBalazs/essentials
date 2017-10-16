import numpy as np

# What maths you need to know to implement neural networks?
# First you need to know some linear algebra.
# Why is it important for neural networks? 
# Let's take the following problem.

# Multiply the following two arrays:
x = [1,2,3]
y = [2,3,4]

# Solution 1: For-loop version
product = []
for i in range(len(x)):
    product.append(x[i]*y[i])
print(product)

# Solution 2: Linear algebra version
x = np.array([1,2,3])
y = np.array([2,3,4])
print(x * y)

# Solution 2 is 3 times faster. It is also more elegant.

# In neural networks knowledge is stored in connections between neurons, i.e. in synapses. Each synapse is represented by a number. 
# The larger the number the stronger the connection between the neurons. The stronger the connection the more one neuron can excite the other.

# Vectors

# In the following example let's assume x represents output values of 3 neurons, and w repesents synaptic weights through which those signals reach a certain neuron represented by n.
# How do we calculate the strength of the signal reaching neuron n?

x = np.array([1,2,3])
w = np.array([2,3,4])
n = np.dot(x,w)
print(n)

# Matrices

a = np.array([
 [1,2,3], 
 [4,5,6]
])
print(a.shape)

b = np.array([
 [1,2], 
 [3,4],
 [5,6]
])
print(b.shape)

# First term of shape function is rows second is columns.

# In the following example let's assume x represents output values of 3 neurons, and w repesents synaptic weights through which those signals reach two neurons represented by n1 and n2.
# How do we calculate the strength of the signals reaching neurons n1 and n2?

x = np.array([1,2,3])
w = np.array([
 [1,2], 
 [3,4],
 [5,6]
])
print(x.shape, w.shape)
n1_n2 = np.dot(x, w)
print(n1_n2)

# Before training neural nets we set up weight matrices randomly. Let's wtite a function to initialize a weight matrix for the above example: 

def weight_init(input, output):
	return np.random.random((input, output))

print weight_init(3,2)

# We want our neurons to compute some functions on the input. As universality can only be reached with digital systems, and because the the brain is a digital computer we will implement a digital unit, that outputs either 1 or 0.

def diu(input, weight):
	'''Vectorized digital unit implementation.'''
	a = np.dot(input, weight)
	a[a<0.5] = 0
	a[a>=0.5] = 1
	return a

print ('Diu: {}'.format(diu(x, w)))

# print('''\n-------------------\nSection 2\n-------------------\n''')