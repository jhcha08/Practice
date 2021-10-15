import numpy as np
import os 
from PIL import Image

path = '/home/hallasan/junghun/SR_Training/dataset/MitHuman_add_x4_500/HR'
file_list = os.listdir(path)
i = 0
for file in file_list:
    im = Image.open(path+'/'+file)
    print(im.size)
    n = np.load(path+'/'+file)
    i += 1
    print(file, np.shape(n))
print('number of files: ', i)