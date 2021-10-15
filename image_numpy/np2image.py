import numpy as np
from PIL import Image
import os

path = '/home/hallasan/junghun/SR_Training/dataset/mit34_70/LR/x3'
file_list = os.listdir(path)
i = 0

for file in file_list:
    n = np.load(path+'/'+file)
    image = Image.fromarray(n)
    image.save("/home/hallasan/junghun/SR_Training/dataset/mit34_70_img/LRimage/x3/%s.png" % file[:-4])