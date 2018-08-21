# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:06:20 2018

@author: baman
"""

import pandas as pd
import io
import zipfile

import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen

def get_data_dob_json(url, in_file):
    """
    Extract the data from a zipped-archive on the web
    """
    archive_data = urlopen(url).read()
    
    zip_data = io.BytesIO()
    zip_data.write(archive_data)
    myzip_file = zipfile.ZipFile(zip_data)
    xls_file = myzip_file.open(in_file)
    xls = pd.ExcelFile(xls_file)
    df = xls.parse('Sheet1', skiprows=2)
    return df

if __name__ == '__main__':
    url = 'http://cdn.crcpress.com/downloads/C9500/GLM_data.zip'
    in_file = r'GLM_data/Table 2.8 Waist loss.xls'
    df = get_data_dob_json(url, in_file)
    print df
    input('All Done!')