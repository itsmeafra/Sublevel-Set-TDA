### This page is under construction and will soon contain sample code for the following paper: 

>Nawar, A., Rahman, F., Krishnamurthy, N., Som, A. and Turaga, P.,
*Topological Descriptors for Parkinson's Disease Classification and Regression Analysis.*
[arXiv preprint arXiv:2004.07384](https://arxiv.org/abs/2004.07384)., 2020. 

>Bibtex:
```
@article{nawar2020topological,
  title={Topological Descriptors for Parkinson's Disease Classification and Regression Analysis},
  author={Nawar, Afra and Rahman, Farhan and Krishnamurthi, Narayanan and Som, Anirudh and Turaga, Pavan},
  journal={arXiv preprint arXiv:2004.07384},
  year={2020}
}
```

# Topological Descriptors for Parkinson’s Disease Classification and Regression Analysis

 This repository contains sample code for understanding the process of persistence image extraction referenced in the paper. 

 This file contains information on the function of each of the files and folders in the repository. At the end of the document, you can find some troubleshooting information. 

## Primary Files:

 The most important files to use to understand the proposed method are [sublevel\_set\_TDA.ipynb](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/sublevel_set_TDA.ipynb) and [Sublevel-Set-TDA.py](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/Sublevel-Set-TDA.py). In these files, we utilize sample signals meant to mimic different classes of subjects to run through the proposed method. We process the data in the same way we would real-world data. The *sublevel\_set_TDA.ipynb* is meant to be a visual aid using only a couple sample signals, while the *Sublevel-Set-TDA.py* script is meant to analyze a full dataset.
Refer to the “Files” section for more detailed information about the contents of the repository, including these primary files.

## Files:

[sublevel\_set\_TDA.ipynb](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/sublevel_set_TDA.ipynb) : Jupyter Notebook script designed to familiarize the user with the method of persistence diagram and persistence image extraction. A couple of sample signals are used, and visuals are provided to aid in this learning process. A more complex example of persistence diagram extraction, using _sample\_signal.mat_, is provided at the end of the script. 
 
 [Sublevel-Set-TDA.py](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/Sublevel-Set-TDA.py): Python script that takes information from the _Dummy\_Dataset_ to exemplify the proposed method. Preprocesses all of the data in the _Dummy\_Dataset_, creates persistence diagrams from the processed signals, and then creates persistence images from the persistence diagrams. The images are then run through an SVM for classification. The persistence images could also be used in regression tasks. With the current settings, SVM classification is 100% because this is merely meant to be an exercise in how to implement the proposed method rather than an indication of real-world accuracy values. 
 
[utils.py](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/utils.py): Python script that contains helper functions that are used in the _Sublevel-Set-TDA.py_ and _sublevel\_set\_TDA.ipynb_ files. 
 
 [Create\_Dummy\_Dataset.py](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/Create_Dummy_Dataset.py): Python script to enable the user to create a collection of their own sample signals from which to test on. This script was used to create the signals in the _Dummy\_Dataset_ folder. 
 
[Dummy\_Dataset](https://github.com/itsmeafra/Sublevel-Set-TDA/tree/master/Dummy_Dataset): Folder containing sample signals to highlight the method explained in the paper. Contains 50 signals with an average amount of distortion in the _Normal\_Distortion_ folder, and 30 signals with heightened distortion in the _Increased\_Distortion_ folder.  
 
 [Mean\_Normalized\_Signals](https://github.com/itsmeafra/Sublevel-Set-TDA/tree/master/Mean_Normalized_Signals): Folder containing the same signals in the _Dummy\_Dataset_, however, the signals have been processed to be mean normalized. 
 
 [Range\_Enforced\_Signals](https://github.com/itsmeafra/Sublevel-Set-TDA/tree/master/Range_Enforced_Signals): Folder containing the same signals as in the _Mean\_Normalized\_Signals_, however, the signals y-values have been enforced to lie between [-1, 1] 
 
 [Persistence\_Diagrams](https://github.com/itsmeafra/Sublevel-Set-TDA/tree/master/Persistence_Diagrams): Folder containing Persistence Diagrams extracted using the signals in the _Range\_Enforced\_Signals_ folder. 
 
 [Persistence\_Images](https://github.com/itsmeafra/Sublevel-Set-TDA/tree/master/Persistence_Images): Folder containing Persistence Images extracted from the _Persistence\_Diagrams_ folder, and using parameters specified by the _Sublevel-Set-TDA.py_ script 
 
 [Helper\_Scripts](https://github.com/itsmeafra/Sublevel-Set-TDA/tree/master/Helper_Scripts): Folder containing many of the same functions found in _utils.py_, however, they are separated into their own scripts  
 
 [sample\_signal.mat](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/sample_signal.mat): A complex sample signal displayed in the _sublevel\_set\_TDA.ipynb_ script. The purpose of this signal is to highlight many of the different kinds of pairings that are possible when Persistence Diagrams are extracted. 
 
 **jpg/png files**: Supplementary image files for _sample\_signal.mat_ 
 
 [Paper Conference Video.pptx](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/Paper%20Conference%20Video.pptx): EMBC Conference presentation PowerPoint slides 
 
 [Paper Conference Video.pdf](https://github.com/itsmeafra/Sublevel-Set-TDA/blob/master/Paper%20Conference%20Video.pdf): EMBC Conference presentation PDF (of slides) 

## Required Packages:
 The following is a list of required packages for the code to run. In parenthesis, the version used when creating this repository is included. 
 
numpy _(version 1.15.4)_
 
matplotlib _(version 3.2.1)_
 
scipy _(version 1.4.1)_
 
ripser _(version 0.3.0)_
 
persim _(version 0.1.2)_
 
sklearn _(version 0.0)_ 

os

sys 

## Trouble Shooting
 If any of your code fails to run, please check the version of your numpy and persim packages. A specific function that is used in persim (which is not developed by us) utilizes an old version of numpy that may not work if you have a newer version of numpy installed. The version used to develop the repository are listed in the “Packages” section. Also note that reinstalling persim will update your numpy to the most recent version of numpy. Therefore, if you have to move to a different version of numpy, do so after installing persim. 
 
You can use the command “pip list” to view your current package versions. 

## Link to Paper:
[Topological Descriptors for Parkinson's Disease Classification and Regression Analysis](https://arxiv.org/abs/2004.07384)

