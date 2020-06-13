# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:47:15 2020

@author: afran
"""

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import metrics
import sklearn
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

from ripser import Rips
from persim import PersImage

import pandas as pd
import os
from ripser import ripser
import matplotlib.pyplot as plt
from scipy import sparse
import time
import scipy.io as sio
import math
import matplotlib as mpl
import random
    
    
#print(x)
"""
plt.xlabel('Time', fontsize = 22)
plt.ylabel('Amplitude', fontsize = 22)
plt.title('Sinusoid', fontsize = 24)
plt.tick_params(axis = 'both', labelsize = 16)
#plt.figure(num = 1, figsize = [10, 10])
plt.plot(t, x, linewidth=5)
"""
'''
noise = np.random.normal(0,1,len(t))/5

x = []
for time in range(len(t)):
    x.append(math.sin(t[time]) + noise[time])
    
    
#print(x)
plt.xlabel('Time', fontsize = 22)
plt.ylabel('Amplitude', fontsize = 22)
plt.title('Sinusoid', fontsize = 24)
plt.tick_params(axis = 'both', labelsize = 16)
#plt.figure(num = 1, figsize = [10, 10])
plt.plot(t, x, linewidth=5)


'''
for i in range(50):
    length = 2*random.random() + 9
    
    shift = 10*random.random() - 5
    
    t = np.linspace(0,length/2*math.pi,1000)
    t_cos = np.linspace(0, length*math.pi,1000)
    cos_amp = 4*random.random() - 2
    sin_amp = 4*random.random() - 2
    
    x = []
    for time in range(len(t)):
        x.append(cos_amp*math.cos(t_cos[time]) + sin_amp*math.sin(t[time]) + shift)
    
    noise = np.random.normal(0,1,len(x))/10
    #print(noise)
    x_normal = x + noise
    
    plt.figure(1)
    plt.xlabel('Time', fontsize = 22)
    plt.ylabel('Amplitude', fontsize = 22)
    plt.title('Sinusoid', fontsize = 24)
    plt.tick_params(axis = 'both', labelsize = 16)
    #plt.figure(num = 1, figsize = [10, 10])
    plt.plot(t, x_normal-np.mean(x_normal))
    
    filename = "./Dummy_Dataset/Normal_Distortion/normal_sample_" + str(i) + ".mat"
    
    sio.savemat(filename, dict([('x', x_normal)]))

for i in range(20):
    length = 2*random.random() + 9
    
    shift = 10*random.random() - 5
    
    t = np.linspace(0,length*math.pi,1000)
    t_cos = np.linspace(0, length/2*math.pi,1000)
    cos_amp = 4*random.random() - 2
    sin_amp = 4*random.random() - 2
    
    x = []
    for time in range(len(t)):
        x.append(cos_amp*math.cos(t_cos[time]) + sin_amp*math.sin(t[time]) + shift)
    
    more_noise = np.random.normal(0,1,len(x))/3
    #print(more_noise)
    x_more_noise = x + more_noise
    
    plt.figure(2)
    plt.xlabel('Time', fontsize = 22)
    plt.ylabel('Amplitude', fontsize = 22)
    plt.title('Sinusoid', fontsize = 24)
    plt.tick_params(axis = 'both', labelsize = 16)
    #plt.figure(num = 1, figsize = [10, 10])
    plt.plot(t, x_more_noise-np.mean(x_more_noise))
    
    filename = "./Dummy_Dataset/Increased_Distortion/increased_sample_" + str(i) + ".mat"
        
    sio.savemat(filename, dict([('x', x_more_noise)]))

