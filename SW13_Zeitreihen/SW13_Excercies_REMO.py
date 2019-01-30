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

# b)
# mit pi=0.5 => np.sqrt(N)
np.sqrt(1000)

## Allgemeint Funktion:
pi=0.5
N=1000
np.sqrt(4*(N*pi**2+N**2*pi**2)+N**2-4*N**2*pi)



# =============================================================================
# Aufgabe d)
# =============================================================================
sp2012 = pd.read_table('data/sp2012.txt', header=None)
sp2012.columns=['sp2012']
df = pd.DataFrame(sp2012)

plt.plot(df)
plt.xlabel("Zeit (Tage)")
plt.ylabel("Wert")
plt.title('S&P 500 - Aktienkurs 2012')
plt.show()

df.head(1)
df.tail(1)
df["sp2012"].describe()


m=0.483
s=11
steps = np.array(st.norm.rvs(size=250, loc=m, scale=s))
sp_simulated = np.empty([250])
sp_simulated[0] = 1257.7

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
# a)
2.5 / np.exp(-np.log(2))

# b)
1 - st.norm.cdf(x=1, loc=5, scale=2)
st.norm.sf(x=1, loc=5, scale=2)

# e)
np.exp(-np.log(0.5))
np.exp(np.log(0.5))