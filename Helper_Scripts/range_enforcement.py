# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:03:54 2020

@author: afran
"""
import numpy as np
import scipy.io as sio
import os


# Range Enforcing All Signals
def range_enforce(directory, divisor):
    for file in os.listdir(directory):
        x = np.squeeze(np.transpose(sio.loadmat(directory + file)['x']))
        
        x_range_enforced = x / divisor
        
        filename = "./Range_Enforced_Signals/" + file
        sio.savemat(filename, dict([('x', x_range_enforced)]))