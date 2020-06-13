# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:16:02 2020

@author: afran
"""

import numpy as np
import scipy.io as sio
import os
from persim import PersImage


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