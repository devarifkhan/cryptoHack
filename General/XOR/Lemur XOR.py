import numpy as np
from PIL import Image

img1=Image.open('../flag.png');
img2=Image.open('../lemur.png')

n1=np.array(img1)*255
n2=np.array(img2)*255

n_image=np.bitwise_xor(n1,n2)

Image.fromarray(n_image).save('n.png')