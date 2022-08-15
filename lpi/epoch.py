import os
import re

def get_sdffiles(path, prefix=''):
    sdffiles = []
    for file in os.listdir(path):
        if re.match(rf'{prefix}\d*\.sdf', file):
            sdffiles.append(f'{path}/{file}')

    sdffiles.sort()
    return sdffiles