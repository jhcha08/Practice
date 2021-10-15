import cv2
from PIL import Image
import numpy as np
import os

path = '/home/hallasan/junghun/EDSR-PyTorch/dataset/DIV2K/DIV2K_train_LR_bicubic/X4'
file_list = os.listdir(path)
i = 0

for file in file_list:
    img = cv2.imread(path+'/'+file)
    result_shrink = np.asarray(Image.open(path+'/'+file))
    np.save('/home/hallasan/junghun/SR_Training/dataset_div2k/LR/x4/'+'%s.npy' % file[:-4], result_shrink)