import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from scipy.stats import chisquare, chi2_contingency
import numpy as np
import statsmodels.formula.api as smf

df = pd.read_csv('thesis_data.csv')
df = df.dropna(axis=1, how='all') # gets rid of empty columns,,, which the csv somehow came w?
df = df.dropna(axis=0, how='all') # and rows too!

# ---------------- W/O EXCLUSIONS ----------------
# FIXME: is this going to be ok? are there other blanks?
m0 = smf.mixedlm("Speed ~ 1", df, groups=df["Maze_ID"]).fit(reml=False) 

m1 = smf.mixedlm("Speed ~ Age", df, groups=df["Maze_ID"]).fit(reml=False)

m2 = smf.mixedlm("Speed ~ Age + Icon", df, groups=df["Maze_ID"]).fit(reml=False)

m3 = smf.mixedlm("Speed ~ Age + Icon + Website", df, groups=df["Maze_ID"]).fit(reml=False)

m4 = smf.mixedlm("Speed ~ Age * Icon + Website", df, groups=df["Maze_ID"]).fit(reml=False)

print(m0.summary())
print(m1.summary())
print(m2.summary())
print(m3.summary())
print(m4.summary())

for name, model in zip(["m0","m1","m2","m3","m4"], [m0,m1,m2,m3,m4]):
    print(name, model.aic)
