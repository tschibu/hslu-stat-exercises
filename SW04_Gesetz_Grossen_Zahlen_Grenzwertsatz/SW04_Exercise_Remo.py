#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:05:38 2019

@author: tluscre1
"""

# =============================================================================
# Aufgabe 4.2
# a)
# =============================================================================
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

n = 5
m = 500

ran = np.array(norm.rvs(size=n*m))
sim = ran.reshape((n,m))

plt.plot(sim)
plt.show()

# =============================================================================
# b)
# =============================================================================
plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x)
plt.plot(x,y)

plt.title("Histogramm sim")
plt.show()

sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))
plt.plot(x,y)
plt.title("Histogramm sim_mean")
plt.show()


# =============================================================================
# c) Wiederholen Sie die Aufgabe für n = 2, 10, 100.
# =============================================================================
n = 2
m = 500

ran = np.array(norm.rvs(size=n*m))
sim = ran.reshape((n,m))

plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x)
plt.plot(x,y)

plt.title("Histogramm sim mit n=" + str(n))
plt.show()

sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))
plt.plot(x,y)
plt.title("Histogramm sim_mean n=" + str(n))
plt.show()

# n = 10
n = 10
m = 500

ran = np.array(norm.rvs(size=n*m))
sim = ran.reshape((n,m))

plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x)
plt.plot(x,y)

plt.title("Histogramm sim mit n=" + str(n))
plt.show()

sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))
plt.plot(x,y)
plt.title("Histogramm sim_mean n=" + str(n))
plt.show()

# n = 20
n = 20
m = 500

ran = np.array(norm.rvs(size=n*m))
sim = ran.reshape((n,m))

plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x)
plt.plot(x,y)

plt.title("Histogramm sim mit n=" + str(n))
plt.show()

sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))
plt.plot(x,y)
plt.title("Histogramm sim_mean n=" + str(n))
plt.show()


# =============================================================================
# Aufgabe 4.3
# =============================================================================
norm.cdf(x=95, loc=100, scale=2)



