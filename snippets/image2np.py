import cv2
from PIL import Image
import numpy as np
import os

path = 'your path'
file_list = os.listdir(path)
i = 0

for file in file_list:
    img = cv2.imread(path+'/'+file)
    result_shrink = np.asarray(Image.open(path+'/'+file))
    np.save('your path/'+'%s.npy' % file[:-4], result_shrink)
