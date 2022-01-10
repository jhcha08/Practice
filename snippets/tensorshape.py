import numpy as np
import os 
from PIL import Image

path = 'your path'
file_list = os.listdir(path)
i = 0
for file in file_list:
    im = Image.open(path+'/'+file)
    print(im.size)
    n = np.load(path+'/'+file)
    i += 1
    print(file, np.shape(n))
print('number of files: ', i)
