import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def train_nn():
    np.random.seed(1)
    
    # Input dataset (4 samples, 2 features each)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    
    # Expected output (XOR problem)
    y = np.array([[0], [1], [1], [0]])
    
    # Initialize weights
    input_size = 2
    hidden_size = 3
    output_size = 1

    W1 = np.random.uniform(-1, 1, (input_size, hidden_size))
    W2 = np.random.uniform(-1, 1, (hidden_size, output_size))

    b1 = np.zeros((1, hidden_size))
    b2 = np.zeros((1, output_size))

    learning_rate = 0.5
    epochs = 10000

    # Training loop
    for epoch in range(epochs):
        hidden_layer_input = np.dot(X, W1) + b1
        hidden_layer_output = sigmoid(hidden_layer_input)
        final_layer_input = np.dot(hidden_layer_output, W2) + b2
        output = sigmoid(final_layer_input)

        error = y - output

        d_output = error * sigmoid_derivative(output)
        d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden_layer_output)

        W2 += hidden_layer_output.T.dot(d_output) * learning_rate
        b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
        W1 += X.T.dot(d_hidden) * learning_rate
        b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Error: {np.mean(np.abs(error))}")

    print("\nTrained Output:")
    print(output)

if __name__ == "__main__":
    train_nn()
