
from matplotlib import pyplot as plt
import numpy as np
import json
with open('train.json') as json_data:
    d = json.load(json_data)

def print_im(data, n, b):
    band = data[n]['band_' + str(b)]
    img = np.zeros(shape=(75,75))
    r = range(75)
    r = [x * 75 for x in r]
    for i in r:
        img[i//75,0:75] = band[i:i+75]

    plt.imshow(img)
    plt.show()

def fasit(data,n):
    print('Is iceberg: ' + str(data[n]['is_iceberg']))
    print('Inc angle: ' + str(data[n]['inc_angle']))


n = 3
while True:
    n+=1
    print_im(d,n,1)
    fasit(d,n)
    i = input('Fortsett? (j/n): ')
    if i.lower() == 'n':
        break
