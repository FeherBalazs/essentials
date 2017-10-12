import numpy as np

def weight_init(shape):
	'''Regularized weight initialization method.'''
	return np.random.random(shape)/shape[0]

def diu(input, weight):
	'''Vectorized digital unit implementation.'''
	a = np.dot(weight, input)
	a[a<0.5] = 0
	a[a>=0.5] = 1
	return a

input = np.array([1,0.5,0.2])
W1 = np.array([(0.1,0.1,0.1), (1,1,1), (10,10,10)])
a1 = diu(input, W1)
W2 = weight_init((1,3))
output = diu(a1, W2)

print output

# input = np.array([1,0.5,0.2])
# W1 = weight_init((3,3))
# a1 = diu(input, W1)
# W2 = weight_init((3,3))
# a2 = diu(a1, W2)
# W3 = weight_init((3,3))
# a3 = diu(a2, W3)
# W4 = weight_init((3,3))
# a4 = diu(a3, W4)

# print a4

def diu_derivative(output):
	'''Calculates derivatives for diu.'''
	output[output<0.5] = 0
	output[output>=0.5] = 1
	return output

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def sigmoid_activation(weight, input):
	return sigmoid(np.dot(weight, input))

def sigmoid_derivative(x):
	return 1 * (1 - x)

def backprop(expected, output):
	error = (expected - output) * diu_derivative(output)

def get_error(guess, feedback):
	return (feedback - guess)

def init():
	input = np.array([0.05, 0.1])
	w1 = np.array([(0.15, 0.25), (0.20, 0.30)])
	w2 = np.array([(0.40, 0.50), (0.45, 0.55)])
	b1 = 0.35
	b2 = 0.60
	feedback = np.array([0.01, 0.99])
	return input, feedback, w1, w2, b1, b2

input, feedback, w1, w2, b1, b2 = init()

def conjecture(input, w1, w2):
	a1 = sigmoid(input, w1)
	guess = sigmoid(a1, w2)
	return guess

def criticism(guess, feedback):
	error = get_error(guess, feedback)
	da1

# conjecture(input, w1, w2)


