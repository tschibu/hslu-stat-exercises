#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 23:01:50 2019

@author: Remo Schwarzentruber
"""

# =============================================================================
# Import
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import lag_plot
from statsmodels.tsa.seasonal import seasonal_decompose

# =============================================================================
# Aufgabe 12.1
# =============================================================================
pw_electric = pd.read_csv("data/PW_electric.csv", sep = ",", skiprows=2, header=0, encoding = "utf-8", index_col=0)
pw_electric.head()


# Luzern
pw_electric_luzern = pd.DataFrame(pw_electric.ix["Luzern", 1:])
pw_electric_luzern.head()
pw_electric_luzern["Year"] = pd.DatetimeIndex(pw_electric_luzern.index)
pw_electric_luzern.set_index("Year", inplace=True)
pw_electric_luzern.head()
pw_electric_luzern.plot()
plt.title("Anzahl Elektro-Autos in Luzern")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Elektro-Autos Luzern")
plt.show()


# Zürich
pw_electric_zurich = pd.DataFrame(pw_electric.ix["Zürich", 1 : ])
pw_electric_zurich["Year"] = pd.DatetimeIndex(pw_electric_zurich.index)
pw_electric_zurich.set_index("Year", inplace=True)
pw_electric_zurich.plot()
plt.title("Anzahl Elektro-Autos in Zürich")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Elektro-Autos Zürich")
plt.show()

# Daten miteinander vergleichen
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(pw_electric_luzern)
ax1.plot(pw_electric_zurich)


# Daten aus Luzern und Zürich vergleichen (log) --> shift

# Relativer Zuwachs in Luzern
pw_electric_luzern["rel"] = np.log(pw_electric_luzern.astype('float')) - np.log(pw_electric_luzern.shift(1).astype('float'))
# Relativer Zuwachs in Zürich
pw_electric_zurich["rel"] = np.log(pw_electric_zurich.astype('float')) - np.log(pw_electric_zurich.shift(1).astype('float'))

pw_rel = pd.DataFrame({
        "Luzern" : pd.Series(pw_electric_luzern["rel"]),
        "Zürich" : pd.Series(pw_electric_zurich["rel"])
        })
pw_rel.plot()

# Lösung
## --> Ein grossen Hype war am 2009. Weiter kann man auch sagen, dass in Zürich
##     ein Jahr vor Luzern den Hype ausgebrochen war.

# =============================================================================
# Aufgabe 12.2
# =============================================================================
# a)
AusBeer = pd.read_csv("data/AustralianBeer.csv", sep = ";", header = 0)
AusBeer.head()
AusBeer["Quarter"] = pd.DatetimeIndex(AusBeer["Quarter"])
AusBeer.set_index("Quarter", inplace = True)
AusBeer.columns=["Megalitres"]
AusBeer.head()
AusBeer.describe()
AusBeer.plot()
plt.ylabel("Megalitres Beer")
plt.show()


# b)
AusBeer.resample("A").mean().plot()
AusBeer['quarter'] = AusBeer.index.quarter
AusBeer.boxplot(by="quarter")

# Lösung:   In den Sommermonaten in Australien wird mehr Bier getrunken als im
#           Winter. 

# c)
seasonal_decompose(AusBeer["Megalitres"], model="additive", freq=4).plot()
# Die Graphik der Zeitreihe aus Teilaufgabe (a) legt nahe, dass die saisonalen
# Effekte ziemlich stabil über den Zeitraum verteilt sind, d.h. die Varianz
# über die Zeit kann als konstant betrachtet werden. Für die Zerlegung ist 
# somit keine Transformation nötig.

# d)
AusBeer_stl = decompose(AusBeer["Megalitres"], period=12)
AusBeer_stl.plot()

# =============================================================================
# Aufgabe 12.3
# =============================================================================














