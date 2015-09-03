from PIL import Image
import numpy as np
from PIL import ImageEnhance

def threshold(filename, step=20):
    img    = Image.open(filename).convert("L")
    img = ImageEnhance.Contrast(img).enhance(1.2)
    pixels = list(img.getdata())
    arr    = np.array(pixels)
    arr2d  = arr.reshape(img.size)

    blocks = np.reshape(arr2d, (-1, step, step))
    for block in blocks:
        factor = 1.2 # CHANGE DEPENDING ON RESULT -> Need algorithm
        mean   = np.mean(block)
        thresh = mean/factor

        block[block <= thresh] = 0
        block[block > thresh] = 1

    arr2d = np.reshape(blocks, (1, -1))

    img2  = Image.new("1", img.size)
    img2.putdata(arr2d[0].tolist())
    img2.save("test.jpg")
    img2.show()



    return img2

threshold("im5.jpg", 5)
