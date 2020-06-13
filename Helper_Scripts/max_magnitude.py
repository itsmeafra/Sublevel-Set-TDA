# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:49:39 2020

@author: afran
"""

import numpy as np
import scipy.io as sio
import os


# Computing Maximum Magnitude Point Across All Samples
def find_max_magnitude(directory):
    max_magnitude = -1
    
    for file in os.listdir(directory):
        x = np.squeeze(np.transpose(sio.loadmat(directory + file)['x']))
        
        data_max = max(x)
        data_min = min(x)
        
        data_max_magnitude = abs(data_max) if abs(data_max) > abs(data_min) else abs(data_min)
        
        if data_max_magnitude > max_magnitude:
            max_magnitude = data_max_magnitude
            
    return max_magnitude