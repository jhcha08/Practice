import numpy as np
from PIL import Image
import os

path = 'your path'
file_list = os.listdir(path)
i = 0

for file in file_list:
    n = np.load(path+'/'+file)
    image = Image.fromarray(n)
    image.save("your path/%s.png" % file[:-4])
