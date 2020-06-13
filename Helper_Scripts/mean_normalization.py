# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:19:29 2020

@author: afran
"""

import numpy as np
import scipy.io as sio
import os


#Mean Normalization
def mean_normalize(directory):
    for folder in os.listdir(directory):
        for file in os.listdir(directory + folder):
            x = np.squeeze(np.transpose(sio.loadmat(directory + folder + "/" + file)['x']))
            x_mean = np.mean(x)
            
            x_mean_normalized = x - x_mean
            
            filename = "./Mean_Normalized_Signals/" + file
            sio.savemat(filename, dict([('x', x_mean_normalized)]))