# -*- coding: utf-8 -*-
# =============================================================================
# Imports
# =============================================================================
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

# =============================================================================
# Aufgabe 4.1
# =============================================================================
st.chi2.ppf(q=[0.05,0.95], df=27)

# =============================================================================
# Aufgabe 4.2
# =============================================================================
st.norm.interval(alpha=0.99, loc=160, scale=5/np.sqrt(36))

# =============================================================================
# Aufgabe 3
# =============================================================================
cloud = pd.Series([18.0, 30.7, 19.8, 27.1, 22.3, 18.8, 31.8, 23.4, 21.2, 27.9, 31.9, 27.1,25.0, 24.7, 26.9, 21.8, 29.2, 34.8, 26.7, 31.6])

st.probplot(x = cloud, plot=plt)

# Variante 1 mit t-test
st.t.cdf(x=25, df=cloud.count()-1, loc=cloud.mean(), scale=cloud.std()/np.sqrt(cloud.count()))

# Variante 2 mit ttest_1samp
st.ttest_1samp(cloud, popmean=25).pvalue/2

# d)
st.t.ppf(q=0.05, df=cloud.count()-1, loc=cloud.mean(), scale=cloud.std()/np.sqrt(cloud.count()))

# hier mit Intervall => alpha = 90% --> unterer Wert
st.t.interval(alpha=0.90, df=cloud.count()-1, loc=cloud.mean(), scale=cloud.std()/np.sqrt(cloud.count()))

# =============================================================================
# Eddie
# =============================================================================
beer = pd.Series([56, 59, 49, 51, 58, 57, 52, 57, 52, 57, 50, 57, 58, 54, 59])
beer.describe()

