"""
Module for BT-Settl atmospheric model spectra.
"""

import os
import tarfile
import urllib.request

import spectres
import numpy as np
import pandas as pd

from species.util import data_util


def add_btsettl(input_path,
                database,
                wavel_range,
                teff_range,
                spec_res):
    """
    Function for adding the BT-Settl atmospheric models to the database.

    Parameters
    ----------
    input_path : str
        Folder where the data is located.
    database : h5py._hl.files.File
        Database.
    wavel_range : tuple(float, float)
        Wavelength range (micron).
    teff_range : tuple(float, float), None
        Effective temperature range (K).
    spec_res : float
        Spectral resolution.

    Returns
    -------
    NoneType
        None
    """

    if not os.path.exists(input_path):
        os.makedirs(input_path)

    data_folder = os.path.join(input_path, 'bt-settl/')

    input_file = 'BT-Settl_M-0.0_a+0.0.tar'

    url = 'https://phoenix.ens-lyon.fr/Grids/BT-Settl/CIFIST2011/SPECTRA/BT-Settl_M-0.0_a+0.0.tar'

    data_file = os.path.join(input_path, input_file)

    if not os.path.isfile(data_file):
        print('Downloading BT-Settl model spectra (5.8 GB)...', end='', flush=True)
        urllib.request.urlretrieve(url, data_file)
        print(' [DONE]')

    print('Unpacking BT-Settl model spectra (5.8 GB)...', end='', flush=True)
    tar = tarfile.open(data_file)
    tar.extractall(data_folder)
    tar.close()
    print(' [DONE]')

    teff = []
    logg = []
    flux = []

    wavelength = [wavel_range[0]]

    while wavelength[-1] <= wavel_range[1]:
        wavelength.append(wavelength[-1] + wavelength[-1]/spec_res)

    wavelength = np.asarray(wavelength[:-1])

    for _, _, file_list in os.walk(data_folder):
        for filename in sorted(file_list):

            if filename.startswith('lte') and filename.endswith('.7.bz2'):
                if len(filename) == 39:
                    teff_val = float(filename[3:6])*100.
                    logg_val = float(filename[7:10])
                    feh_val = float(filename[11:14])

                elif len(filename) == 41:
                    teff_val = float(filename[3:8])*100.
                    logg_val = float(filename[9:12])
                    feh_val = float(filename[13:16])

                else:
                    raise ValueError('The length of the filename is not compatible for reading '
                                     'the parameter values.')

                if teff_range is not None:
                    if teff_val < teff_range[0] or teff_val > teff_range[1]:
                        continue

                if feh_val != 0.:
                    continue

                print_message = f'Adding BT-Settl model spectra... {filename}'
                print(f'\r{print_message:<80}', end='')

                dataf = pd.pandas.read_csv(data_folder+filename,
                                           usecols=[0, 1],
                                           names=['wavelength', 'flux'],
                                           header=None,
                                           dtype={'wavelength': str, 'flux': str},
                                           delim_whitespace=True,
                                           compression='bz2')

                dataf['wavelength'] = dataf['wavelength'].str.replace('D', 'E')
                dataf['flux'] = dataf['flux'].str.replace('D', 'E')

                dataf = dataf.apply(pd.to_numeric)
                data = dataf.values

                # [Angstrom] -> [micron]
                data_wavel = data[:, 0]*1e-4

                # See https://phoenix.ens-lyon.fr/Grids/FORMAT
                data_flux = 10.**(data[:, 1]-8.)  # [erg s-1 cm-2 Angstrom-1]

                # [erg s-1 cm-2 Angstrom-1] -> [W m-2 micron-1]
                data_flux = data_flux*1e-7*1e4*1e4

                data = np.stack((data_wavel, data_flux), axis=1)

                index_sort = np.argsort(data[:, 0])
                data = data[index_sort, :]

                if np.all(np.diff(data[:, 0]) < 0):
                    raise ValueError('The wavelengths are not all sorted by increasing value.')

                teff.append(teff_val)
                logg.append(logg_val)

                try:
                    flux.append(spectres.spectres(wavelength, data[:, 0], data[:, 1]))
                except ValueError:
                    flux.append(np.zeros(wavelength.shape[0]))

    data_sorted = data_util.sort_data(np.asarray(teff),
                                      np.asarray(logg),
                                      None,
                                      None,
                                      None,
                                      wavelength,
                                      np.asarray(flux))

    data_util.write_data('bt-settl', ['teff', 'logg'], database, data_sorted)

    print_message = 'Adding BT-Settl model spectra... [DONE]'
    print(f'\r{print_message:<80}')
