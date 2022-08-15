import os
import numpy as np

def read_scalar(path, keyword):
    scalars = os.path.join(path, 'scalars.txt')

    data = []
    with open(scalars, mode='r') as f:
        data_start = False
        data_loc = None
        for line in f.readlines():
            if line.find(keyword) > 0:
                if line.strip('#').split()[0].isnumeric():
                    continue
                data_start = True
                data_loc = line.strip('#').split().index(keyword)
                continue
            if data_start:
                data.append(float(line.split()[data_loc]))
    return np.asarray(data, dtype=float)