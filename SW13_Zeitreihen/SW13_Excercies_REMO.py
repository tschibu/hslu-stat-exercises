# -*- coding: utf-8 -*-

# =============================================================================
# Imports
# =============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

# =============================================================================
# Aufgabe 13.1
# =============================================================================
# a) Binominaltest (2er)
print(st.binom.pmf(k=1000, n=1000, p=0.5))

d = np.random.choice(a=[-1,1], size = 1000, replace=True)
x = np.cumsum(d)
plt.plot(x)


help(np.cumsum)



# =============================================================================
# Aufgabe d)
# =============================================================================
sp2012 = pd.read_table('data/sp2012.txt')
df = pd.DataFrame(sp2012)

plt.plot(df)
plt.xlabel("Zeit (Tage)")
plt.ylabel("Wert")
plt.title('S&P 500 - Aktienkurs 2012')

plt.show()



steps = np.array(st.norm.rvs(size=250, loc=0.483, scale=11))
sp_simulated = np.empty([250])
sp_simulated[0] = -1257.7

for i in range(249):
    sp_simulated[i+1] = sp_simulated[i]+ steps[i]
    
plt.plot(sp_simulated)
plt.xlabel("Zeit (Tage)")
plt.ylabel("Wert")
plt.title('S&P 500 - Simulierter Aktienkurs 2012')
plt.show()



# =============================================================================
# Aufgabe 13.3
# =============================================================================
2.5 / np.exp(-np.log(2))

np.exp(-np.log(2))

10 / np.exp(-np.log(0.5))


