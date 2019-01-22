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

# =============================================================================
# Aufgabe 4.4
# =============================================================================

# b)
norm.cdf(x=2, loc=1, scale=2) - norm.cdf(x=0, loc=1, scale=2)

# c)
norm.cdf(x=51, loc=50, scale=np.sqrt(200)) - norm.cdf(x=49, loc=50, scale=np.sqrt(200))

# d)
norm.cdf(x=2, loc=1, scale=np.sqrt(2/25)) - norm.cdf(x=0, loc=1, scale=np.sqrt(2/25))



# =============================================================================
# Aufgabe 4.5
# =============================================================================

a = [79.98, 80.04, 80.02, 80.04, 80.03, 80.03, 80.04, 79.97, 80.05, 80.03,
     80.02, 80.00, 80.02]
b = [80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 80.03, 79.95, 79.97]

# a)
mean_a = np.mean(a)
mean_b = np.mean(b)
se_a = np.std(a) / np.sqrt(len(a))
se_b = np.std(b) / np.sqrt(len(b))
print('μa={:.4f}'.format(mean_a))
print('σa={:.4f}'.format(se_a))
print('μb={:.4f}'.format(mean_b))
print('σb={:.4f}'.format(se_b))

print('Methode A: ({:.3f}±{:.3f})cal/g'.format(mean_a, se_a))
print('Methode B: ({:.3f}±{:.3f})cal/g'.format(mean_b, se_b))

# b)
ser_a = se_a / mean_a
ser_b = se_b / mean_b
print('Methode A: {:.3f}cal/g ±{:.3f}%'.format(mean_a, ser_a*100))
print('Methode B: {:.3f}cal/g ±{:.3f}%'.format(mean_b, ser_b*100))
