# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:57:13 2020

@author: afran
"""

import numpy as np
import scipy.io as sio
import os
from ripser import ripser
from scipy import sparse
from persim import PersImage
import sys
from sklearn.svm import LinearSVC


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


#Mean Normalization
def mean_normalize(directory):
    for folder in os.listdir(directory):
        for file in os.listdir(directory + folder):
            x = np.squeeze(np.transpose(sio.loadmat(directory + folder + "/" + file)['x']))
            x_mean = np.mean(x)
            
            x_mean_normalized = x - x_mean
            
            filename = "./Mean_Normalized_Signals/" + file
            sio.savemat(filename, dict([('x', x_mean_normalized)]))
            





# Persistence Diagram Generation
def generate_persistence_diagrams(directory):
    for file in os.listdir(directory):
        x = np.squeeze(np.transpose(sio.loadmat(directory + file)['x']))
        
        # Extracting Needed Info
        N = len(x)
        t = np.arange(N)
        
        #Sublevelset Filtration
        # Add edges between adjacent points in the time series, with the "distance"
        # along the edge equal to the max value of the points it connects
        I = np.arange(N-1)
        J = np.arange(1, N)
        V = np.maximum(x[0:-1], x[1::])
        
        # Add vertex birth times along the diagonal of the distance matrix
        I = np.concatenate((I, np.arange(N)))
        J = np.concatenate((J, np.arange(N)))
        V = np.concatenate((V, x))
        
        #Create the sparse distance matrix
        D = sparse.coo_matrix((V, (I, J)), shape=(N, N)).tocsr()
        dgm0 = ripser(D, maxdim=0, distance_matrix=True)['dgms'][0]
        dgm0 = dgm0[dgm0[:, 1]-dgm0[:, 0] > 1e-3, :]
        allgrid = np.unique(dgm0.flatten())
        allgrid = allgrid[allgrid < np.inf]
        xs = np.unique(dgm0[:, 0])
        ys = np.unique(dgm0[:, 1])
        ys = ys[ys < np.inf]
        
        # Removing Infinity Points
        where_are_inf = np.isinf(dgm0)
        dgm0 = dgm0[~where_are_inf[:,1]]
        
        filename = "./Persistence_Diagrams/" + file
        sio.savemat(filename, dict([('PD', dgm0)]))
        


def generate_persistence_diagram(x):
        
    # Extracting Needed Info
    N = len(x)
    t = np.arange(N)
    
    #Sublevelset Filtration
    # Add edges between adjacent points in the time series, with the "distance"
    # along the edge equal to the max value of the points it connects
    I = np.arange(N-1)
    J = np.arange(1, N)
    V = np.maximum(x[0:-1], x[1::])
    
    # Add vertex birth times along the diagonal of the distance matrix
    I = np.concatenate((I, np.arange(N)))
    J = np.concatenate((J, np.arange(N)))
    V = np.concatenate((V, x))
    
    #Create the sparse distance matrix
    D = sparse.coo_matrix((V, (I, J)), shape=(N, N)).tocsr()
    dgm0 = ripser(D, maxdim=0, distance_matrix=True)['dgms'][0]
    dgm0 = dgm0[dgm0[:, 1]-dgm0[:, 0] > 1e-3, :]
    allgrid = np.unique(dgm0.flatten())
    allgrid = allgrid[allgrid < np.inf]
    xs = np.unique(dgm0[:, 0])
    ys = np.unique(dgm0[:, 1])
    ys = ys[ys < np.inf]
    
    # Removing Infinity Points
    where_are_inf = np.isinf(dgm0)
    dgm0 = dgm0[~where_are_inf[:,1]]
    
    return dgm0


# Persistence Image Generation
def generate_persistence_images(directory, threshold, pixel, spreadval, rangemin, rangemax):
    for file in os.listdir(directory):
        dgm0 = np.squeeze(sio.loadmat(directory + file)['PD'])
        # Computing Lifetimes for Thresholding of Persistence Diagrams
        lifetime = np.ones(len(dgm0))
        
        for h in range(len(dgm0)):
            lifetime[h] = dgm0[h][1] - dgm0[h][0]
        
        #Keeps only points greater than reduction value
        isvalid = np.greater(lifetime, threshold) 
        reduced_pd = dgm0[isvalid]
        
        print("Beginning Persistence Image Generation for " + file)
        print("Length of PD: " + str(len(dgm0)) + " points")
        print("Length Reduced PD: " + str(len(reduced_pd)) + " points")
        
        pim = PersImage(pixels=[pixel,pixel], spread=spreadval, specs={"minBD": rangemin, "maxBD": rangemax})
        imgs = pim.transform(reduced_pd)
        imgs = imgs/np.max(imgs)
        imgs = imgs.reshape((-1))
        
        filename = "./Persistence_Images/" + file
        sio.savemat(filename, dict([('PersImg', imgs)]))
        
    
def reduce_persistence_diagram(dgm0, threshold):
    # Computing Lifetimes for Thresholding of Persistence Diagrams
    lifetime = np.ones(len(dgm0))
    
    for h in range(len(dgm0)):
        lifetime[h] = dgm0[h][1] - dgm0[h][0]
    
    #Keeps only points greater than reduction value
    isvalid = np.greater(lifetime, threshold) 
    reduced_pd = dgm0[isvalid]
    
    print("Length of PD: " + str(len(dgm0)) + " points")
    print("Length Reduced PD: " + str(len(reduced_pd)) + " points")
    
    return reduced_pd

    
def generate_persistence_image(dgm0, threshold, pixel, spreadval, rangemin, rangemax):
    
    # Computing Lifetimes for Thresholding of Persistence Diagrams
    lifetime = np.ones(len(dgm0))
    
    for h in range(len(dgm0)):
        lifetime[h] = dgm0[h][1] - dgm0[h][0]
    
    #Keeps only points greater than reduction value
    isvalid = np.greater(lifetime, threshold) 
    reduced_pd = dgm0[isvalid]
    
    print("Length of PD: " + str(len(dgm0)) + " points")
    print("Length Reduced PD: " + str(len(reduced_pd)) + " points")
  
    
    pim = PersImage(pixels=[pixel,pixel], spread=spreadval, specs={"minBD": rangemin, "maxBD": rangemax})
    imgs = pim.transform(reduced_pd)
    imgs = imgs/np.max(imgs)
    #imgs = imgs.reshape((-1))
    
    return imgs
    
    
        

# Range Enforcing All Signals
def range_enforce(directory, divisor):
    for file in os.listdir(directory):
        x = np.squeeze(np.transpose(sio.loadmat(directory + file)['x']))
        
        x_range_enforced = x / divisor
        
        filename = "./Range_Enforced_Signals/" + file
        sio.savemat(filename, dict([('x', x_range_enforced)]))
        


# SVM Classification
def SVM_leave_one_classify(directory, SVM_random_state=None, SVM_dual=True, SVM_penalty='l2', SVM_max_iter=1000, SVM_C=1.0):
    #Creating ground truth array
    truth = []
    prediction = []
    for file in os.listdir(directory):
        if "normal" in file:
            truth.append(0)
        elif "increased" in file:
            truth.append(1)
        else:
            print("[Error] Invalid Filename")
            sys.exit()
    
    #Leave one subject out validation using SVM
    for file in os.listdir(directory):
        
        print("predicting file " + file)
        
        X_train = []
        y_train = []
        
        #Every file except for left out trial
        for train_file in os.listdir(directory):
            if train_file != file:
                X_data = np.squeeze(np.transpose(sio.loadmat(directory + train_file)['PersImg']))
                
                X_train.append(X_data)
                
                if "normal" in train_file:
                    y_train.append(0)
                elif "increased" in train_file:
                    y_train.append(1)
                else:
                    print("[Error] Invalid Filename")
                    sys.exit()
        
        #Using parameters entered earlier
        clf = LinearSVC(random_state=SVM_random_state, dual=SVM_dual, penalty=SVM_penalty, max_iter=SVM_max_iter, C=SVM_C)
        
        clf.fit(X_train, y_train)
        
        X_pred_data = np.squeeze(np.transpose(sio.loadmat(directory + file)['PersImg']))
        X_pred_data = [X_pred_data]
        
        prediction.append(clf.predict(X_pred_data))
    
    #Checking against ground truth array
    print("Checking against ground truth array....")
    accuracy_array = []
    for i in range(len(truth)):
        accuracy_array.append(1 if truth[i] == prediction[i] else 0)
    
    accuracy = sum(accuracy_array)/len(accuracy_array)
    
    return accuracy