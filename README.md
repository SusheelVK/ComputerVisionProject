# Computer Vision
This repository contains the report and implementations of my course project for DSE312 Computer Vision at IISER Bhopal in Fall 2023. 
The course project was Handwritten Signature Verification and involved investigating the results of 2 existing models on 3 publicly available datasets(CEDAR, BHSig260-Hindi and Bengali).
The two existing models and the steps needed to replicate the results are in the respective folder. Preliminary results on the IISER dataset are also given, but the dataset is withheld for privacy reasons.
The repository also contains the code and report for the 3 course assignments.
The first assignment included the application of various simple filters namely translation and gradient detection as well as the Gaussian filter. All the filters were applied without the use of functions from libraries like OpenCV such as filter2d.
The second assignment involved the calculation of gradient magnitude and orientation as well as the formation of LoG, DoG and Gaussian pyramids of an image without inbuilt functions. Lastly, two images are merged using the Laplacian Pyramid.
The third assignment was to perform 10 class classification using the CIFAR-10 dataset by extracting the SIFT and HOG features of both the original RGB and the LBP variant of the original images, with classification done using SVM. The assignment also included the computation of optical flow of a video visualized by mapping the result back to the original video.
