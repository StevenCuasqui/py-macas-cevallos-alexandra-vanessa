# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:42:21 2020

@author: Ale
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import nltk
import seaborn as sns

path_csv = "C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\06-spider-items\\arania_fybeca\\arania_fybeca\\tmp\\productos-fybeca_final.csv"
data_frame_test = pd.read_csv(path_csv,  encoding = 'unicode_escape',sep = ",")
data_frame_test.dropna()
data_frame_test.dtypes

data_frame_test['ahorro'] = data_frame_test['precio_normal'] - data_frame_test['precio_descuento']

ahorro_total = data_frame_test['ahorro'].sum()
maximo_descuento = data_frame_test['ahorro'].max()
minimo_descuento = data_frame_test['ahorro'].min()
print("Precio maximo de descuento:",maximo_descuento)
print('Precio minimo de descuento:', minimo_descuento)
print('El ahorro total es:', ahorro_total)