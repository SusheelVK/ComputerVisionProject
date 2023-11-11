import os, shutil
from PIL import Image
import numpy as np
srcPath = './BHSig260-Hindi/Forgery/' 
destpath = './BHSig260-Hindi/Genuine/'

max_size = (1, 1)
files = os.listdir(destpath)
for file in files:
    im = Image.open(file)
    imarray = np.array(im)
    
    if imarray.size > max_size:
        max_size = imarray.size
