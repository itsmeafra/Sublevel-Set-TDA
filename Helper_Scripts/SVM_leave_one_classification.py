# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:23:23 2020

@author: afran
"""
import numpy as np
import scipy.io as sio
import os
import sys
from sklearn.svm import LinearSVC

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