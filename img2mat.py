# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 21:05:06 2019

@author: CivilKen
"""

import os
import numpy as np
from skimage.transform import resize
from skimage import io

imgfiles = os.listdir('Aberdeen')
X = np.zeros((7500,415))

for i in range(len(imgfiles)):
    img = 'Aberdeen/'+imgfiles[i]
    result = np.array(io.imread(img))
    result = resize(result,(50,50,3))
    flatimg = result.flatten()
    X[:,i] = flatimg

np.save('X.npy', X)
