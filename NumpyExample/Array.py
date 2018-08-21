# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:13:59 2018

@author: baman
"""



from sqlalchemy import create_engine

import pymssql

conn = pymssql.connect('192.168.5.90\MSSQL2012CI', 'sc_ci_user', 'sc_ci_user', "bcbssc_ci")
cursor = conn.cursor()
cursor.execute('SELECT * FROM enc_act WHERE act_idn=%s', '77650')

for row in cursor:
    print('row = %r' % (row,))

conn.close()
