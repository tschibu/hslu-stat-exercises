# -*- coding: utf-8 -*-

# =============================================================================
# Imports
# =============================================================================
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

# =============================================================================
# Aufgabe 3a)
# =============================================================================

# Aufgabe: Relativer Fehler berechnen
gamma = pd.read_csv("data/gamma.txt", delim_whitespace = True)
gamma.head()

gamma["gamma"].describe()

str(gamma["gamma"])

rel_fehler_gamma = gamma["gamma"].std() / np.sqrt(gamma["gamma"].count()) / (gamma["gamma"].mean()) * 100
print("Der relativer Fehler lautet: " + str(rel_fehler_gamma))

# =============================================================================
# Aufgabe 3b
# =============================================================================

# Zusatzaufgabe:
# Nullhypothese H0: µ0 = 1
# Alternativhypothese HA: µA < (µ0 = 1)

# Da wir hier das µ wie auch das σ schätzen müssen. kommt die T-Verteilung zum Zuge.

t_x = (gamma["gamma"].mean()-1) / (gamma["gamma"].std()/np.sqrt(gamma["gamma"].count()))
p_value_t_test_gamma = st.t.cdf(x = t_x, df = gamma["gamma"].count()-1)
print("P-Value von T-Test " + str(p_value_t_test_gamma))

## Lösung => 0.1532
## Weiter Lösung:
pvalue_do = st.ttest_1samp(gamma["gamma"], popmean=1).pvalue/2
print("Weiter Lösung von P-Value via: ttest_1samp" + str(p_value_t_test_gamma))

# =============================================================================
# Aufgabe 3c
# =============================================================================

st.probplot(gamma["gamma"], plot = plt)
st.norm.ppf(q = 0.98, loc =1 )
## Falsch!

# =============================================================================
# Aufgabe Plot
# =============================================================================

# Lösung (x) -> Ungefähr 50% der Werte befinden sicher ausserhalb der Box


# =============================================================================
# Aufgabe Ueberzeit
# =============================================================================

intervall = 15 - 0
erwartungswert_ueberzeit = intervall/2 * 100
print("Die erwartete Überzeit in 100 Tagen beträgt " + str(erwartungswert_ueberzeit) + ".")
print("Mann geht von einer Normalverteilung aus, da ein Arbeiter mal 2 min Überzeit macht und dann mal 14...")


# =============================================================================
# Quizfrage 05
# =============================================================================

print("B -> 1 / A -> 3 / C -> 2")

# =============================================================================
# Quizfrage 06
# =============================================================================
