#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:20:50 2019

@author: tluscre1
"""
import matplotlib.pyplot as plt 
import scipy.stats as st
import seaborn as sns
import pandas as pd
import numpy as np

# =============================================================================
# Import
# =============================================================================
iron = pd.read_table("../data/ironF3.dat",sep=" ",index_col=False)

# =============================================================================
# Aufgabe 5.3
# =============================================================================
# a)
iron.plot(kind='box', title='Maeuse Daten')

# b)
np.log(iron).plot(kind='box', title="Maeuse Daten mit log")

# c)
st.probplot(iron['medium'], plot=plt)

st.probplot(np.log(iron['medium']), plot=plt)
# Log ist viel besser

# d)
mean = iron['medium'].mean()
var = iron['medium'].var()
p = 1 - st.norm.cdf(x=10, loc=mean, scale=np.sqrt(var))
print(p)



# =============================================================================
# Aufgabe 5.4
# =============================================================================

# a)
       