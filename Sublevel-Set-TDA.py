# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:44:06 2020

@author: afran
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import os
import sys
from ripser import ripser
from scipy import sparse
from persim import plot_diagrams
from persim import PersImage
from sklearn.svm import LinearSVC
from utils import *


###########################################################################

# Computing Mean of Each Signal & Normalizing Signal
print("Computing Mean of Each Signal & Normalizing Signal")
mean_normalize("./Dummy_Dataset/")

# Computing Maximum Magnitude Point Across All Samples
print("Computing Maximum Magnitude Point Across All Samples")
max_magnitude = find_max_magnitude("./Mean_Normalized_Signals/")

# Range Enforcing All Signals
print("Range Enforcing All Signals")
range_enforce("./Mean_Normalized_Signals/", max_magnitude)

# Persistence Diagram Generation
print("Generating Persistence Diagrams")
generate_persistence_diagrams("./Range_Enforced_Signals/")

# Persistence Image Generation - Persistence Image Parameters Subject to User Tuning
print("Generating Persistence Images")

reduction = 0.08
pixel = 100
spreadval = 0.015
rangemin = -0.7
rangemax = 0.7

generate_persistence_images("./Persistence_Diagrams/", reduction, pixel, spreadval, rangemin, rangemax)


# SVM Classification - Parameters for SVM Classification Subject to User Tuning
###############################
print("....................................")
print("....................................")
print("....................................")
print("Beginning SVM Classification")    


SVM_random_state=None
SVM_dual=True
SVM_penalty='l2'
SVM_max_iter=1000
SVM_C=1.0

accuracy = SVM_leave_one_classify("./Persistence_Images/", SVM_random_state, SVM_dual, SVM_penalty, SVM_max_iter, SVM_C)


print("....................................")
print("....................................")
print("....................................")
print ("The SVM is " + str(accuracy*100) + " percent accurate")