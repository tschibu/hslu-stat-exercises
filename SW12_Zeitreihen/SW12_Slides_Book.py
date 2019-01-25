# -*- coding: utf-8 -*-

# =============================================================================
# Import
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import lag_plot
from statsmodels.tsa.seasonal import seasonal_decompose

# =============================================================================
# helper methods
# =============================================================================
def boxcox(x,lambd):
    return np.log(x) if (lambd==0) else (x ** lambd-1)/lambd


# =============================================================================
# Passagierzahlen der Fluggesellschaft PAN AM (19271991) von 1949 bis 1960
# =============================================================================
AirP = pd.read_csv("data/AirPassengers.csv")
AirP.head()

# convert TravelDate as Index
AirP["TravelDate"] = pd.DatetimeIndex(AirP["TravelDate"])
AirP.set_index("TravelDate", inplace = True)

AirP.head()
AirP.describe()

# Plot
AirP.plot()

plt.xlabel("Reisedatum")
plt.ylabel("Anzahl Passagiere in 1000")
plt.show()

# Box-Cox-Transformationen
AirP["l_2"] = boxcox(AirP["Passengers"],2)
AirP["l_0"] = boxcox(AirP["Passengers"],0)
AirP["l_-05"] = boxcox(AirP["Passengers"],-0.5)
AirP.head()

plt.subplot(221)
plt.title("Original")
plt.xlabel("")

plt.subplot(222)
AirP["l_-05"].plot()
plt.title("lambda = -0.5")
plt.xlabel("")

plt.subplot(223)
AirP["l_2"].plot()
plt.title("lambda = 2")
plt.xlabel("")

plt.subplot(224)
AirP["l_0"].plot()
plt.title("lambda = 0")
plt.xlabel("")

plt.show()


# Zeitverschiebungstransformation (time-shift
# help(pd.DataFrame.shift)

AirP["s_4"] = AirP["Passengers"].shift(-4)
AirP["s_-5"] = AirP["Passengers"].shift(5)

AirP["Passengers"].plot()
AirP["s_4"].plot()
AirP["s_-5"].plot()

plt.legend(["Original", "zurückverschoben", "vorverschoben"])

plt.show()

# Bewegendes Mittel (moving average)
AirP["Trend"] = AirP["Passengers"].rolling(window = 12).mean()
AirP["Passengers"].plot()
AirP["Trend"].plot()

plt.legend(["Daten","Trend"])
plt.show()

AirP["Season"] = AirP["Passengers"] - AirP["Trend"]
AirP["Season"].plot()
plt.show()

# Gemittelte Saisonalität
# AirP["Season"] wird in eine Matrix umgewandelt
# mit den Monaten als Spalten (Jahre als Zeilen)

AirP2 = AirP["Season"].values.reshape((12, 12))
# Entlang der Spalten (axis=0) wird der Mittelwert genommen
# nanmean bedeutet, die NaN werden ignoriert

ave = np.nanmean(AirP2, axis = 0)
# Der Vektor ave wird verzwölfacht
# damit er wieder die gleiche Länge hat, wie AirP["Season"]

AirP["Season_ave"] = np.tile(A = ave, reps = 12)
AirP["Season_ave"].plot()
plt.show()

AirP["Residual"] = AirP["Season"] - AirP["Season_ave"]
AirP["Residual"].plot()
plt.show()


seasonal_decompose(AirP["Passengers"], model = "additive", freq = 12).plot()
plt.show()

seasonal_decompose(np.log(AirP["Passengers"]), model = "add").resid.plot()
plt.show()


from stldecompose import decompose
decompose(np.log(AirP["Passengers"]), period = 12).plot();

# =============================================================================
# vierteljährliche Bierproduktion in Australien (in Megaliter) zwischen 
# März 1956 und Juni 1994
# =============================================================================
AusBeer = pd.read_csv("data/AustralianBeer.csv", sep=";")
AusBeer.head()

AusBeer1 = AusBeer.copy()
AusBeer1.head()

AusBeer1["Quarter"] = pd.DatetimeIndex(AusBeer1["Quarter"])

AusBeer1.set_index("Quarter", inplace = True)
AusBeer1.head()
AusBeer1.describe()

AusBeer1.plot()
plt.title("Bierproduktion in Australien")
plt.xlabel("Jahr im Quartal")
plt.ylabel("Liter in 1000")
plt.show()

AusBeer1.loc["1980-9" : "1990-3",:].plot()
plt.title("Vierteljährliche Bierproduktion in Australien zwischen September 1980 und März 1994 ")
plt.xlabel("Jahr im Quartal")
plt.ylabel("Liter in 1000")
plt.show()


# =============================================================================
# Multivariate Zeitreihen
# =============================================================================

AusEl = pd.read_csv("data/AustralianElectricity.csv", sep = ";", header = 0)
AusEl.head()

Aussie = AusBeer.copy()

Aussie.head()
Aussie["kilowatt"] = AusEl["kilowatt"]
Aussie.head()

Aussie["Quarter"] = pd.DatetimeIndex(Aussie["Quarter"])
Aussie.set_index("Quarter", inplace = True)

Aussie.plot(subplots = True)
plt.xlabel("Jahr in Quartal")
plt.show()



# =============================================================================
# Luftqualität
# =============================================================================
AirQ = pd.read_csv("data/AirQualityUCI.csv", sep = ";", decimal = ",")
AirQ.head()

AirQ1 = AirQ.copy()

# pandas kennt das Zeitformat in der Tabelle nicht:
#Punkt muss durch - ersetzt werden
AirQ1["Time"] = AirQ1["Time"].str.replace(".", "-")
AirQ1["Date"] = pd.DatetimeIndex(AirQ1["Date"] + " " + AirQ1["Time"])
AirQ1.set_index("Date", inplace = True)

# Einige Wert der Temperatur sind -200. Diese Zeilen werden weggelassen
AirQ1 = AirQ1[AirQ1["T"] > -200]
AirQ1["T"].plot()
plt.show()

AirQ4 = AirQ1.loc["2004-3-10" : "2004-3-30" , "T"]
AirQ4.plot()

# Die Option by = "Time" erreicht, dass für jede Stunde ein Boxplot erzeugt wird.
AirQ1.boxplot("T", by = "Time", rot = 45)
plt.show()

plt.subplot(121)
lag_plot(AirQ4)
# Ohne Lag => Korrelation zu der benachbarten Stunde

plt.subplot(122)
lag_plot(AirQ4, 15)


import time
for i in range(1, 24):
    lag_plot(AirQ4, i)
    plt.show()
    time.sleep(1)

plt.show()































