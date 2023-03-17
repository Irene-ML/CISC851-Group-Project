"""_description_
"""
import numpy as np

class Agent:
    """
        Create Agent (player) object
    """
    
    def __init__(self, n_feature, n_hidden, n_out):
        """
        Initialization the Agent
        
        Args:
            n_feature (int): number of features that fed into neural network
            n_hidden (int): number of nodes at hidden layer
            n_out (int): number of nodes at output layer
        """
        self.n_feature = n_feature
        self.n_hidden = n_hidden
        self.n_out = n_out
        self.w_ih = np.random.rand(self.n_feature, self.n_hidden) * 0.1
        self.w_ho = np.random.rand(self.n_hidden, self.n_out) * 0.1
        self.fitness = []
        
        
    def prediction(self, input_features, activation = "sigmoid"):
        """
        Define prediction function that predicts the x, y components of acceleration
        Args:
            input_features (np.ndarray): feature values of the ball object
            activation (String): activation function that is used at hidden layer
        """
        if activation == "sigmoid":
            return self.relu(np.dot(self.sigmoid(np.dot(input_features, self.w_ih)), self.w_ho))
        
        elif activation == "relu":
            
            return self.relu(np.dot(self.relu(np.dot(input_features, self.w_ih)), self.w_ho))
            
        else:
            raise Exception("use 'sigmoid' or 'relu' for second arg")
    
    
    def sigmoid(self, x):
        """
        Define sigmoid function
        Args:
            x (numpy.ndarray): output scores at certain layer
        """
        return np.array(1. / (1. + np.exp(-x)))
    
    def relu(self, x):
        """
        Define relu funciton
        Args:
            x (numpy.ndarray): output scores at certain layer
        """
        return np.maximum(0, x);
