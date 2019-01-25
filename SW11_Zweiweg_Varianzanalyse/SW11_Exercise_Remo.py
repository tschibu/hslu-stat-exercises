#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:01:31 2019

@author: tluscre1
"""

from pandas import DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as st
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt
from patsy.contrasts import Sum

Daten = DataFrame({
        "Batch": np.tile(["1", "2", "3", "4", "5", "6"], 4),
        "Methode": np.repeat(["8500", "8700", "8900", "9100"], 6),
        "Y": np.array([90.3, 89.2, 98.2, 93.9, 87.4, 97.9, 92.5, 89.5, 90.6, 94.7, 87, 95.8,85.5,90.8, 89.6, 86.2, 88, 93.4, 82.5, 89.5, 85.6, 87.4, 78.9, 90.7])
        })

interaction_plot(x=Daten["Batch"], trace=Daten["Methode"], response=Daten["Y"])
plt.ylabel("Daten Y")
plt.show()



# =============================================================================
# Zweiweg-Varianzanalyse mit Blöcken
# =============================================================================
from patsy.contrasts import Sum
fit = ols("Y ~ C(Methode, Sum)+C(Batch,Sum)", data=Daten).fit()
fit.params


fit = ols("Y ~ C(Methode, Sum)+C(Batch, Sum)", data=Daten).fit()
anova_lm(fit)






# =============================================================================
# Flugzeugfarbe
# =============================================================================
Farbe = DataFrame({
        "Grund": np.repeat(["A", "B", "C"], 6),
        "Methode": np.tile(np.repeat(["Eintauchen", "Besprühen"], 3), 3),
        "Y": np.array([4, 4.5, 4.3, 5.4, 4.9, 5.6, 5.6, 4.9, 5.4, 5.8, 6.1, 6.3, 3.8, 3.7, 4, 5.5, 5, 5])
        })

interaction_plot(x=Farbe["Grund"], trace=Farbe["Methode"], response=Farbe["Y"])

plt.xlabel("Grundierungstypen")
plt.ylabel("Mittelwerte Haltungsfestigkeit")

plt.show()



# =============================================================================
# Gift / Elritzen
# =============================================================================
El = DataFrame({
        "Konz": np.repeat(["A", "B", "C","D"], 6),
        "Temp": np.tile(np.repeat(["15C", "25C"],3),4),
        "Y": np.array([82, 46, 16, 20, 13, 7, 20, 14, 17, 6, 7, 5, 8, 6, 5, 4, 3, 5, 10, 7, 5, 6, 4, 5])
        })

interaction_plot(x=El["Konz"], trace=El["Temp"], response=El["Y"], legendtitle="Methode")

plt.xlabel("Cyanid-Konzentration")
plt.ylabel("Mediane Experimente")

plt.show()

fit = ols("Y~C(Konz,Sum)*C(Temp,Sum)",data=El).fit()

fit.params





# =============================================================================
# Aufgabe 11.1
# =============================================================================

luftf = DataFrame({
        "Luftfeuchtigkeitsniveau" : np.tile(["1", "2", "3", "4"], 5),
        "Marke": np.repeat(["1", "2", "3", "4", "5"], 4),
        "Energieverbrauch" : np.array([685, 792, 838, 875, 722, 806, 893, 953, 733, 802, 880, 941, 811, 888, 952, 1005, 828, 920, 978, 1023])
        })
luftf.head()

fit = ols("Energieverbrauch ~ C(Marke, Sum) + C(Luftfeuchtigkeitsniveau, Sum)", data=luftf).fit()
anova_lm(fit)

interaction_plot(x=luftf["Marke"], trace=luftf["Luftfeuchtigkeitsniveau"], response=luftf["Energieverbrauch"])
plt.ylabel("luftf Y")
plt.show()



# =============================================================================
# Aufgabe 11.2
# =============================================================================
# a)
automob = pd.read_csv("data/automob.dat", sep=" ")
df = DataFrame(automob)
sns.stripplot(x="STADT", y="KMP4L", hue="AUTO", jitter=True, data=automob)

# b)
fit = ols("KMP4L ~ C(STADT,Sum) * C(AUTO,Sum)", data=automob).fit()
anova_lm(fit)


# c)
df = DataFrame(automob)
# Data frame row index should start from 0
df.reset_index(inplace = True)
interaction_plot(x = df["STADT"], trace = df["AUTO"], response = df["KMP4L"])


# d)
fit2 = ols("KMP4L ~ C(STADT,Sum) + C(AUTO,Sum)", data=automob[automob["STADT"]=="Los Angeles"]).fit()
anova_lm(fit2)

# e)
df3 = DataFrame(automob)
df3.reset_index(inplace=True)
fit3 = ols("KMP4L ~ C(STADT,Sum) * C(AUTO,Sum)", data=df3[df3["STADT"]!="San Francisco"]).fit()
print(anova_lm(fit3))

# =============================================================================
# Aufgabe 11.3
# =============================================================================
# a)
stream = pd.read_csv('data/stream.dat', sep=" ")

stream["ZNGROUP"] = stream["ZNGROUP"].apply(str)
sns.stripplot(x="ZNGROUP", y="DIVERSITY", data=stream)
plt.xlabel("Zink-Gruppe")
plt.ylabel("Diversitaet")
sns.boxplot(x="ZNGROUP", y="DIVERSITY", data=stream)
plt.xlabel("Zink-Gruppe")
plt.ylabel("Diversitaet")

# b)
dfStream = DataFrame(stream)
dfStream.reset_index(inplace = True)
interaction_plot(x = dfStream["STREAM"], trace = dfStream["ZNGROUP"], response = dfStream["DIVERSITY"])

fit113 = ols("DIVERSITY ~ C(STREAM,Sum) * C(ZNGROUP,Sum)", data=dfStream).fit()
anova_lm(fit113)


# c)



