# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:13:45 2020

@author: afran
"""

import numpy as np
import scipy.io as sio
import os
from ripser import ripser
from scipy import sparse


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