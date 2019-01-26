# -*- coding: utf-8 -*-

# =============================================================================
# Import
# =============================================================================
import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

x = pd.Series([16,22,22,24,25,45,46,47,48,49,50])
mean = x.sum()/x.count()
median = x[6]
x.describe()

new_var = 0.5 * 186.8 + 4.5
print(new_var)


st.norm.ppf(q=[0.005, 0.995], loc=160, scale = np.sqrt(5))
st.binom.pmf()



cloud = pd.Series([18.0, 30.7, 19.8, 27.1, 22.3, 18.8, 31.8, 23.4, 21.2, 27.9, 31.9, 27.1,25.0, 24.7, 26.9, 21.8, 29.2, 34.8, 26.7, 31.6])
cloud.describe()

st.t.ppf(q=[0.95], df=19)


beer = pd.Series([56, 59, 49, 51, 58, 57, 52, 57, 52, 57, 50, 57, 58, 54, 59])


st.probplot(beer, plot=plt)

# =============================================================================
# Aufgabe 4: Eddie vom Vögeligärtli
# =============================================================================
# Vorbereitung
beer_arr = beer - beer.mean()

# Vorzeichnentest
st.binom_test(x=9, n=15, p=0.5, alternative='less')

# Willcoxtest
st.wilcoxon(beer_arr, zero_method="wilcox", correction = True).pvalue
## TODO


((3**2)*3) + ((2**2)*2)


