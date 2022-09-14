import os
import re
import sdf
import numpy as np
from . import m_e, c

_field_names = {
        'Ex': 'Electric Field/Ex', 'Ey' : 'Electric Field/Ey' , 'Ez' : 'Electric Field/Ez' ,
        'Bx' : 'Magnetic Field/Bx', 'By' : 'Magnetic Field/By' , 'Bz' : 'Magnetic Field/Bz' ,
}


def get_sdffiles(path, prefix=''):
    sdffiles = []
    for file in os.listdir(path):
        if re.match(rf'{prefix}\d*\.sdf', file):
            sdffiles.append(f'{path}/{file}')

    sdffiles.sort()
    return sdffiles


def get_extent(result_path, ts, prefix=''):
    '''
    get 2D extent
    '''
    if isinstance(ts, int):
        ts = f'{ts:04d}'
    sdffile_name = f'{result_path}/{prefix}{ts}.sdf'
    f = sdf.read(sdffile_name, dict=True)
    
    extent = [
        f['Grid/Grid'].data[0][0],
        f['Grid/Grid'].data[0][-1],
        f['Grid/Grid'].data[1][0],
        f['Grid/Grid'].data[1][-1],
    ]
    
    return np.array(extent)


def get_field(result_path, ts, component, prefix='', slice=()) -> np.ndarray:
    if isinstance(ts, int):
        ts = f'{ts:04d}'
    sdffile_name = f'{result_path}/{prefix}{ts}.sdf'
    f = sdf.read(sdffile_name, dict=True)
    
    if component in _field_names.keys():
        dset = f.pop(_field_names[component]).data
    else:
        dset = f.pop(f'Derived/Number_Density/{component}').data
        
    if len(dset.shape) == 2:
        return dset[slice].T
    else:
        return dset[slice]


def get_particles(result_path, ts, name, component : str, prefix='') -> np.ndarray:
    if isinstance(ts, int):
        ts = f'{ts:04d}'
    sdffile_name = f'{result_path}/{prefix}{ts}.sdf'
    f = sdf.read(sdffile_name, dict=True)
    
    if component in ['px', 'py', 'pz']:
        dset = f.pop(f'Particles/{component.capitalize()}/{name}').data
        return dset[()] / m_e / c
    
    if component in ['x', 'y', 'z']:
        dset = f.pop(f'Grid/Particles/{name}').data
        return dset[{'x' : 0, 'y' : 1, 'z' : 2}[component]]

    if component == 'id':
        dset = f.pop(f'Particles/ID/{name}').data
        return dset[()]