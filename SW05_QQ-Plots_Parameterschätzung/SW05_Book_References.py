# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from scipy.stats import norm, binom
import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series
import matplotlib.mlab as mlab

# =============================================================================
# Q-Q-Plot
# -> muehsam 
# =============================================================================
x = Series([24.4, 27.6, 27.8, 27.9, 28.5, 30.1, 30.3, 31.7, 32.2, 32.8, 33.3, 33.5, 34.1, 34.6, 35.8, 35.9, 36.8, 37.1, 39.2, 39.7])

alphak = (np.arange(1, x.size + 1) - 0.5) / x.size

quantile_theor = norm.ppf(q = alphak, loc = x.mean(), scale = x.std())
quantile_empir = np.sort(x)


plt.xlabel("Theor. Quantile")
plt.ylabel("Empirische Quantile")
plt.plot(quantile_theor, quantile_empir, "o")
plt.show()

# =============================================================================
# Q-Q-Plot
# -> Einfach
# =============================================================================
x = Series([24.4, 27.6, 27.8, 27.9, 28.5, 30.1, 30.3, 31.7, 32.2, 32.8, 33.3, 33.5, 34.1, 34.6, 35.8, 35.9, 36.8, 37.1, 39.2, 39.7])
st.probplot(x, plot=plt)


# =============================================================================
# Parameterschätzung für stetige Wahrscheinlichkeitsverteilungen
# Momentenmethode
# =============================================================================

test = pd.Series([11.96, 5.03, 67.40, 16.07, 31.50, 7.73, 11.10,22.38])
test.describe()

LamdaGeschaetzt = 1 / test.mean()
print(LamdaGeschaetzt)

# =============================================================================
# Parameterschätzung für stetige Wahrscheinlichkeitsverteilungen
# Maximum-Likelihood-Methode
# =============================================================================
st.binom.pmf(k=58, n=100, p=0.5)
st.binom.pmf(k=58, n=100, p=0.6)





