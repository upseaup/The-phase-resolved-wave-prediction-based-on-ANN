# The-phase-resolved-wave-prediction-based-on-ANN

The program is developed in the following environment  
    python = 3.9.13   
    TensorFlow = 2.10   
    numpy = 1.21.5  
    matpoltlib = 3.5.2  
    
This program was developed under Windows 10 and has not been tested on Linux.
Therefore, there may be some issues under Linux.

Code for paper "Enhancing deterministic prediction in unidirectional ocean waves using an Artificial Neural Network with exponential linear unit", see https://www.sciencedirect.com/science/article/pii/S002980182400876X.

Citation  

    @article{FENG2024117539,  
    title = {Enhancing deterministic prediction in unidirectional ocean waves using an Artificial Neural Network with exponential linear unit},  
    journal = {Ocean Engineering},  
    volume = {301},  
    pages = {117539},  
    year = {2024},  
    issn = {0029-8018},  
    doi = {https://doi.org/10.1016/j.oceaneng.2024.117539},  
    url = {https://www.sciencedirect.com/science/article/pii/S002980182400876X},  
    author = {Zhongying Feng and Zhan Wang and Kun Zheng and Ruipeng Li and Yuxin Zhao and Ye Wang},  
    keywords = {Artificial Neural Network, Exponential linear unit, Deterministic ocean wave prediction, High-order Spectral method},
    abstract = {The phase-resolved wave prediction based on physical methods is difficult to ensure both accuracy and efficiency simultaneously. In recent years, Artificial Neural Network (ANN) has been successfully utilized for deterministic ocean wave prediction with efficiency and high precision. In this work, an ANN with the exponential linear unit (ELU) activation function is developed for deterministic wave prediction in unidirectional sea states. High-order Spectral method is used to generate the data on wave elevation. Instead of the traditional rectified linear unit (ReLU), we propose to use ELU as the activation function in the present ANN. Numerical results show that the ANN with the ELU activation function provides a more accurate prediction than the ANN with the ReLU activation function. Based on wave elevation measured at a fixed position, wave elevation prediction at another fixed position and wave elevation prediction in a fixed zone, are both studied by making use of the ANN with the ELU. Moreover, the factors including sea state and time length of wave elevation measured at a fixed position are considered to demonstrate the efficiency of the prediction results.}  
    }  
