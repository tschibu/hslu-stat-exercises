#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:42:31 2019

@author: tluscre1
"""
# =============================================================================
# Import
# =============================================================================
from pandas import DataFrame
from statsmodels.formula.api import ols
from patsy.contrasts import Sum
from statsmodels.stats.anova import anova_lm
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import warnings

# =============================================================================
# Aufgabe 1
# =============================================================================
x = pd.Series([0.3, 0.5, 0.7])
x.sum()/x.count()

# =============================================================================
# Aufgabe 2
# =============================================================================
schiri = pd.read_csv("data/Schiedsrichter_Lebenserwartung.txt", delim_whitespace = True, header = None)
schiri.head()
schiri.count()

# filter
schiri.columns=["Alter", "lebendig", "Lebenserwartung"]
NotDeadSchiri = schiri[schiri["lebendig"] == 0]

# T-Test
# QQ-Plot
diff = NotDeadSchiri["Lebenserwartung"] - NotDeadSchiri["Alter"]
st.probplot(diff, plot = plt)
diff.plot(kind='box')

# mit cdf
1 - st.t.cdf(x = diff.mean(), df = diff.count() -1 , loc = 0, scale = diff.std()/np.sqrt(diff.count()))

# mit sf
st.t.sf(x = diff.mean(), df = diff.count() -1 , loc = 0, scale = diff.std()/np.sqrt(diff.count()))


# c)
st.t.interval(alpha=0.98, df = diff.count()-1 , loc= diff.mean(), scale = diff.std()/np.sqrt(diff.count()))

st.t.ppf(q=0.01,df = diff.count()-1 , loc= diff.mean(), scale = diff.std()/np.sqrt(diff.count()))

# d)
st.wilcoxon(diff, zero_method="wilcox", correction=True).pvalue / 2

1 - st.wilcoxon(diff, zero_method="wilcox", correction=True).pvalue /2

# e)
schiedsrichter_lebend = schiri[schiri["lebendig"]==1]
alter_schiedsrichter_lebend = schiedsrichter_lebend["Alter"]
schiedsrichter_lebend_mittel = alter_schiedsrichter_lebend.mean()
abs_fehler = alter_schiedsrichter_lebend.std()/np.sqrt(alter_schiedsrichter_lebend.size)
rel_fehler = abs_fehler/schiedsrichter_lebend_mittel
print(rel_fehler)


# =============================================================================
# Aufgabe 3: Varianzanalyse
# =============================================================================
warnings.filterwarnings("ignore")
df = DataFrame(
        {
                "Person": np.repeat(["P1", "P2", "P3", "P4", "P5"],3),
                "Wein": np.tile(["W1", "W2", "W3"],5),
                "Y": np.array([1,7,5,0,4,0,1,6,4,1,5,2,1,8,10])
        })
fit = ols("Y ~ C(Person,Sum)+C(Wein,Sum)",data=df).fit()
anova_lm(fit)


fit.params

fit.summary()


# =============================================================================
# Aufgabe 3c:
# =============================================================================
fit2 = ols("Y ~ C(Person,Sum) * C(Wein,Sum)", data=df).fit()



# =============================================================================
# MEP Vorbereitung
# =============================================================================
st.binom.ppf(q=0.05, n=200, p=0.45)

st.binom_test(x=70, n=200, p=0.45, alternative="less")

help(st.binom.ppf)


legierung = pd.Series([1.00781, 1.00646, 1.00801, 1.00833, 1.00738, 1.00687,
1.00783, 1.00936, 1.00564, 1.00543, 1.00794, 1.01060])








