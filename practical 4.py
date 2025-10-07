import numpy as np

class NeuralNetwork:
    def __init__(self):
        # Seed for reproducibility
        np.random.seed(1)
        # 3 input nodes → 1 output node (random weights between -1 and 1)
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        """Activation function: Sigmoid"""
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        """Derivative of sigmoid"""
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        for iteration in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustment = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    def think(self, inputs):
        """Pass inputs through the neural net"""
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


# Initialize neural network
neural_network = NeuralNetwork()

print("Beginning Randomly Generated Weights: ")
print(neural_network.synaptic_weights)

# Training data (4 samples, 3 features each)
training_inputs = np.array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
])

# Expected outputs (4x1 matrix)
training_outputs = np.array([[0, 1, 1, 0]]).T

# Train the neural network
neural_network.train(training_inputs, training_outputs, 15000)

print("\nEnding Weights After Training: ")
print(neural_network.synaptic_weights)

# Test with user input
user_input_one = float(input("User Input One: "))
user_input_two = float(input("User Input Two: "))
user_input_three = float(input("User Input Three: "))

print("\nConsidering New Situation: ", user_input_one, user_input_two, user_input_three)
print("New Output Data: ")
print(neural_network.think(np.array([[user_input_one, user_input_two, user_input_three]])))
