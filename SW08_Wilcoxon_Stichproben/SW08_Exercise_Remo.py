# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series
import matplotlib.mlab as mlab

# =============================================================================
# Aufgabe 8.1
# =============================================================================
st.binom.cdf(k=[2,3], n=12, p=0.5)
st.binom_test(x=7, n=12, p=0.5, alternative="less")
st.binom.cdf(k=7, n=12, p=0.5)


x = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])

st.wilcoxon(x-70, zero_method="wilcox", correction=True)
print(st.wilcoxon(x-70, zero_method="wilcox", correction=True))

# =============================================================================
# Aufgabe 8.2
# =============================================================================
diff = Series([-7,-16,-3,2,-1,-10,-11,2,-8])

mu = 0
variance = 5.78
sigma = np.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 4*sigma, 100)
plt.figure(figsize=(5,5))
plt.plot(x,mlab.normpdf(x, mu, sigma))
plt.axvline(-5.78, linewidth=4, color='b')
plt.axvline(+5.78, linewidth=4, color='b')
plt.show()


st.probplot(x=diff, plot=plt)

# Verwerfungsbereich
st.t.ppf([0.05, 0.95], loc = 0, df = diff.count()-1, scale=diff.std()/np.sqrt(diff.count()))

# x = Position = in diesem Fall ist es diff.mean()
# df = Freiheitsgrad = diff.count() - 1
# loc = Erwartungswert (mü)
# scale => Standardfehler
st.t.cdf(x = diff.mean(), df = diff.count() - 1 , loc = 0, scale=diff.std()/np.sqrt(diff.count()))

# =============================================================================
# Aufabe 8.3
# =============================================================================
jackals = pd.read_table("/Users/tluscre1/Documents/Studium.Local/STAT/repo/data/jackals.txt", sep = " ")
st.ttest_ind(jackals["M"], jackals["W"], equal_var=False)

# Test entscheid => sie unterscheiden sich 

MminusW = jackals["M"]-jackals["W"]

# Verwerfungsbereich
st.t.ppf(q = [0.05,0.95], df = MminusW.count() -1 , loc = 0, scale=MminusW.std()/np.sqrt(MminusW.count()))


st.t.cdf(x = MminusW.mean(),df = MminusW.count() -1 , loc = 0, scale=MminusW.std()/np.sqrt(MminusW.count()))

# d) Willcox
st.mannwhitneyu(jackals["M"], jackals["W"], alternative = "two-sided")



# =============================================================================
# Aufgabe 8.5
# =============================================================================
zurich = pd.Series([16.6, 12.7, 14, 53.3, 117, 62.6, 27.6])
basel = pd.Series([10.4,8.91,11.7,29.9,46.3,25,29.4])

diff = zurich - basel
diff.describe()

diffMean = diff.mean()
diffSdt = diff.std()
mu0 = 0
st.probplot(diff, plot=plt)

# b)
# ungepaarter Test, gemessen wurden zwar an der gleichen Tage, aber an verschiedenen Lokalitäten, Messgeräte

# c)
# Nullhypothese - beide Städte konsumieren gleich vile MDMA
# Alternativhypothese - Zürich wird mehr MDMA konsumiert als in Basel


## HIER DAS BEISPIEL FÜR GEPAARTE WERTE

## t-test
st.t.ppf(q = 0.95, df = 6, loc = 0, scale=diffSdt/np.sqrt(diff.count()))
# ==> 19.27585899564982

## Hier gibt es zwei Methoden:
1 - st.t.cdf(x=diff.mean(), df = 6, loc = 0,  scale=diffSdt/np.sqrt(diff.count()))
# ist gleich wie t.sf.
st.t.sf(x=diff.mean(), df = 6, loc = 0,  scale=diffSdt/np.sqrt(diff.count()))


## t-test
st.ttest_ind(zurich, basel, equal_var=False)


# Willcox
st.mannwhitneyu(zurich, basel, alternative = "greater")














