from PIL import Image
import numpy as np


def threshold(filename, step=20):
    img = Image.open(filename).convert("L")
    pixels = list(img.getdata())
    arr = np.array(pixels)
    arr2d = np.reshape(arr, img.size)

    blocks = np.reshape(arr2d, (-1, step, step))
    for block in blocks:
        factor = 1.2              # CHANGE DEPENDING ON RESULT -> Need algorithm
        mean = np.mean(block)
        thresh = mean/factor

        block[block <= thresh] = 0
        block[block > thresh] = 1

    arr2d = np.reshape(blocks, (1, -1))

    img2 = Image.new("1", img.size)
    img2.putdata(arr2d[0].tolist())
    img2.save("test.jpg")
    return img2

threshold("im6.jpg", 5)
