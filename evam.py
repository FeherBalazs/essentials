import numpy as np

input = np.array([1])
weight = np.array([0.6])

def binary_threshold(input, weight, threshold):
	if sum(input * weight) > threshold:
		return 1
	else:
		return 0

# input = np.array([1,2,3])
# weight = np.array([1,2,3])
# print (input*weight)

# print ('Binary threshold: {}'.format(binary_threshold(input, weight, 0.4)))

def relu(input, weight):
	return max(0, (input * weight))

# input = -1
# weight = 0.5

# print ('Relu: {}'.format(relu(input, weight)))

# def diu(input, weight):
# 	'''Non-vectorized digital unit implementation.'''
# 	if sum(input * weight) > 0.5:
# 		return 1
# 	else:
# 		return 0
	
# def diu(input, weight):
# 	'''Vectorized digital unit implementation.'''
# 	a = np.array(sum(input * weight))
# 	a[a<0.5] = 0
# 	a[a>=0.5] = 1
# 	return a

# print ('Diu: {}'.format(diu(input, weight)))

def weight_init(shape):
	return (np.array(np.random.random(shape))/shape[0])

# print weight_init((3,2))

# print np.array([1,2,3]) * np.array([1,2,3])
# print np.array(np.random.random((1,3))) * np.array([1,2,3])
# print sum(np.array(np.random.random((1,3))) * np.array([1,2,3]))
# print sum(weight_init((1,3)) * np.array([1,2,3]))

# def diu(input, weight):
# 	'''Vectorized digital unit implementation.'''
# 	a = np.array(sum((input * weight).T))
# 	print ('Pruduct of input * weight: {}'.format(input * weight))
# 	print ('Sum of activations: {}'.format(sum((input * weight).T)))
# 	a[a<0.5] = 0
# 	a[a>=0.5] = 1
# 	print ('Result of diu activation: {}'.format(a))
# 	return a

# input = np.array([1,0.5,0.2])
# # weight = weight_init((3,3))
# weight = np.array([(0.1,1,10), (0.1,1,10), (0.1,1,10)]).T
# # weight = np.array([(0.1,0.1,0.1), (1,1,1), (10,10,10)])
# print ('Weight: {}'.format(weight))
# print ('Input: {}'.format(input))
# # print ('Diu: {}'.format(diu(input, weight)))
# diu(input, weight)

# input = np.array([1])
# weight = weight_init((1,1))
# # print ('Diu: {}'.format(diu(input, weight)))


# def diu(input, weight):
# 	'''Vectorized digital unit implementation.'''
# 	a = np.array(sum((input * weight)))
# 	print ('Pruduct of input * weight: {}'.format(input * weight))
# 	print ('Sum of activations: {}'.format(sum((weight * input).T)))
# 	print ('Sum of activations (dot product): {}'.format(np.dot(weight, input)))
# 	a[a<0.5] = 0
# 	a[a>=0.5] = 1
# 	print ('Result of diu activation: {}'.format(a))
# 	return a

def diu(input, weight):
	'''Vectorized digital unit implementation.'''
	a = np.dot(weight, input)
	print ('Weight: {}'.format(weight))
	print ('Input: {}'.format(input))
	print ('Pruduct of input * weight: {}'.format(input * weight))
	print ('Sum of activations (dot product): {}'.format(np.dot(weight, input)))
	a[a<0.5] = 0
	a[a>=0.5] = 1
	print ('Result of diu activation: {}'.format(a))
	return a

# input = np.array([1,0.5,0.2])
# W1 = np.array([(0.1,0.1,0.1), (1,1,1), (10,10,10)])
# a1 = diu(input, W1)
# W2 = np.array([(0.1,0.1,0.1), (1,1,1), (10,10,10)])
# a2 = diu(a1, W2)

input = np.array([1,0.5,0.2])
W1 = weight_init((3,3))
a1 = diu(input, W1)
W2 = weight_init((3,3))
a2 = diu(a1, W2)
W3 = weight_init((3,3))
a3 = diu(a2, W3)
W4 = weight_init((3,3))
a4 = diu(a3, W4)