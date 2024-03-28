import os
import numpy as np
import pandas as pd
from micrograd.engine import Value
from sklearn.neural_network import MLPClassifier



class CustomNet():
    
    def __init__(self,
                 input_shape:int,
                 num_layers:int,
                 num_nodes:list):
        """
            A custom ANN implementation 
            using nnumpy, pandas and micrograd
            by Kapapathy.

            https://github.com/karpathy/micrograd.git
        """
        super(CustomNet,self).__init__()
        
        # initiallize the architecture and weights
        self.input_shape = input_shape
        self.n_layers = num_layers
        self.n_nodes = num_nodes
        self.W = np.block(np.random.random(
            input_shape,self.n_nodes[0]
        ),
)
    def create_network(self):
        """
            Create the ANN by pre-defined
            num layers and nodes per layer.
            initialize the weights and bias 
            randomly to back-prpogate and optimize
            during training. 
        """
        print("Creating a network with {} hidden layers".format(self.n_layers))
