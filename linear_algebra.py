import numpy

# What mathematical ideas you need to know to program neural networks?
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
x = numpy.array([1,2,3])
y = numpy.array([2,3,4])
print(x * y)

# Solution 2 is 3 times faster. It is also more elegant.

# In neural networks knowledge is stored in connections between neurons, i.e. in synapses. Each synapse is represented by a number. 
# The larger the number the stronger the connection between the neurons. The stronger the connection the more one neuron can excite the other.

# print('''\n-------------------\nSection 2\n-------------------\n''')