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
iron = pd.read_table("data/ironF3.dat",sep=" ",index_col=False)


# =============================================================================
# Aufgabe 5.1
# =============================================================================
# a)
plt.figure(1)
plt.subplot(2,2,1)
x = st.norm.rvs(size=10)
st.probplot(x, plot=plt)
plt.subplot(2,2,2)
x = st.norm.rvs(size=20)
st.probplot(x, plot=plt)
plt.subplot(2,2,3)
x = st.norm.rvs(size=50)
st.probplot(x, plot=plt)
plt.subplot(2,2,4)
x = st.norm.rvs(size=100)
st.probplot(x, plot=plt)
plt.tight_layout()
plt.show()

# b)
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=20, df=1)
    st.probplot(x,plot=plt)
    plt.title("n=20,df=1")
    
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=100, df=1)
    st.probplot(x,plot=plt)
    plt.title("n=20,df=1")

# c)
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.chi2.rvs(size=10, df=20)
    st.probplot(x,plot=plt)
    plt.title("n=20,df=20")

# =============================================================================
# Aufgabe 5.2
# =============================================================================
# a)
# mögliche Werte
werte = np.array([0,10,11])

# X simulieren
sim = pd.Series(np.random.choice(werte, size=1000, replace=True))

# Plot
plt.subplot(4,2,1)

sim.hist(bins=[0,1,10,11,12], edgecolor="black")
plt.title("Original")

plt.subplot(4,2,2)
st.probplot(sim, plot=plt)
plt.title("Normal Q-Q Plot")


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
       