# Licensed under a 3-clause BSD style license - see LICENSE.rst
import glob
import os
from xml.dom import minidom

import astropy.units as u
from astropy.io import ascii
from astropy.table import Table, QTable

try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"
__all__ = []

_package_directory = os.path.dirname(os.path.abspath(__file__))
_data_directory = os.path.abspath(os.path.join(_package_directory, 'data'))

_metadata_files = glob.glob(os.path.join(_data_directory, '*.xml'))

# hard code the expected meta data in each meta file
_column_data = {"datafilename": [], "description": [], "keywords": [], "event_id": [],
                "instruments": [], "reference_doi": [], "acknowledgment": [], "notes": [],
                "col_units": []}


for this_metadata_file in _metadata_files:
    mydoc = minidom.parse(this_metadata_file)
    metas = mydoc.getElementsByTagName('meta')

    for elem in metas:
        _column_data[elem.attributes['name'].value].append(elem.firstChild.data)

dataset_index = Table(_column_data)
dataset_index.add_index('datafilename')


def load_dataset(filename):
    """Load a dataset.

    Returns
    -------
    result: QTable
    """
    datafile_path = os.path.join(_data_directory, filename)
    result = QTable(ascii.read(datafile_path, format='csv', fast_reader=False))

    # add the meta data
    this_row = dataset_index.loc['dem_quiet_sun.csv']
    meta_dict = dict(zip(this_row.colnames, this_row))
    result.meta = meta_dict

    if dataset_index.loc[filename]['col_units'] != "None":
        units_list = dataset_index.loc[filename]['col_units'].split(',')
        for this_unit, this_col in zip(units_list, result.columns):
            result[this_col].unit = u.Unit(this_unit)
    return result


