#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:42:31 2019

@author: tluscre1
"""




# =============================================================================
# Aufgabe 3: Varianzanalyse
# =============================================================================

from pandas import DataFrame
from statsmodels.formula.api import ols
from patsy.contrasts import Sum
from statsmodels.stats.anova import anova_lm
import numpy as np
import warnings

warnings.filterwarnings("ignore")
df = DataFrame(
        {
                "Person": np.repeat(["P1", "P2", "P3", "P4", "P5"],3),
                "Wein": np.tile(["W1", "W2", "W3"],5),
                "Y": np.array([1,7,5,0,4,0,1,6,4,1,5,2,1,8,10])
        })
fit = ols("Y ~ C(Person,Sum)+C(Wein,Sum)",data=df).fit()




# =============================================================================
# Aufgabe 3c:
# =============================================================================
fit2 = ols("Y ~ C(Person,Sum) * C(Wein,Sum)", data=df).fit()