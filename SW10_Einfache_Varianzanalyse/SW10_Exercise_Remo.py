# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from scipy.stats import norm, binom
import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series
import matplotlib.mlab as mlab
from pandas import DataFrame
import seaborn as sns
import statsmodels.formula.api as sm

df = DataFrame({
        "Treatment": np.repeat(["Kommerziell", "Vakuum", "Gemischt", "CO2"], [3, 3, 3, 3]),
        "steak_id":[7.66, 6.98, 7.80, 5.26, 5.44, 5.80, 7.41, 7.33, 7.04, 3.51, 2.91, 3.66]
        })

df = DataFrame({
        "Treatment": np.repeat(["Kommerziell", "Vakuum", "XO2", "Yemischt"], [3, 3, 3, 3]),
        "steak_id":[7.66, 6.98, 7.80, 5.26, 5.44, 5.80, 7.41, 7.33, 7.04, 10.51, 10.91, 10.66]
        })

fit = sm.ols("steak_id~Treatment", data=df).fit()
fit.summary()

help(sm.ols)

fit_pred = fit.get_prediction()
fit_pred.conf_int()

print(fit.summary())
print(fit.params)


print("T.CO2: " + str(3.3600 + 0))
print("T.Gemischt: " + str(3.3600 + 3.9000))
print("T.Kommerziell: " + str(3.3600 + 4.1200))
print("T.Vakuum]: " + str(3.3600 + 2.1400))
