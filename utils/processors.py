import torch
import numpy as np
import pandas as pd
from torch.utils import DataLoader
from torch.utils.Dataset import Dataset

class Trainer():

    def __init__(self,num_epochs:int,
                 training_batch_size:int,
                 eval_batch_size:int,
                 requires_grad:bool=True):
        
        super(Trainer,self).__init__()

        self.num_epochs = num_epochs
        self.training_batch_size = training_batch_size
        self.eval_batch_size = eval_batch_size
        self.requires_grad = requires_grad


    def train(self)->pd.DataFrame:
        """
            train the ANN
        """
        pass

    def eval(self):
        """
            Evaluation method for the ANN
        """
        self.requires_grad = False
        pass