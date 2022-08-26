import numpy as np
import math
from sklearn import svm
from sklearn.svm import SVR
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
import random
from random import randrange
from csv import writer


#plot based on global nuclear warheads data

df1 = read_csv('nuclear.csv')

x1 = []
for elements in df1["Year"]:
  if elements not in x1:
    x1.append(elements) 
for i in range(2015, 2023):
  x1.append(i)

years = []
for elements in df1["Year"]:
  if elements not in years:
    years.append(elements)

whole = []
for year in years:
  new = df1.loc[df1['Year'] == year, 'Nuclear weapons inventory by country (FAS Nuclear Notebook)'].tolist()
  total = sum(new)
  whole.append(total)

df1 = df1.groupby(by=["Year"]).sum()
X = df1.index.to_numpy().reshape(-1, 1)
y = df1.to_numpy()
clf = svm.SVC()
clf.fit(X, y)
years_want_to_predict = np.array(range(2015,2023)).reshape(-1, 1)
results = clf.predict(years_want_to_predict)
whole.extend(results)

rc('font', weight='bold')
plt.rcParams.update({'font.size': 22})
plt.rcParams["figure.figsize"] = (15,13)
plt.title("Estimated Global Nuclear Warheads Inventory\n(1945-2022)", fontweight='bold')
plt.xlabel("Years", fontweight='bold')
plt.ylabel("Nuclear Weapons Inventory", fontweight='bold')
plt.plot(x1,whole, color="b", label="Global", linewidth=5)
plt.savefig('nuclear_global.png', dpi=500)


#plot based on total nuclear resuls

df2 = pd.read_csv('Total nuclear result.csv')
x2 = []
for elements in df2["Average TNT equivalent(tons)"]:
    x2.append(elements)
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []

for elements in df2["10000Mt"]:
    y1.append(elements)

for elements in df2["5000Mt"]:
    y2.append(elements)

for elements in df2["3000Mt"]:
    y3.append(elements)

for elements in df2["1000Mt"]:
    y4.append(elements)

for elements in df2["500Mt"]:
    y5.append(elements)

for elements in df2["100Mt"]:
    y6.append(elements)

rc('font', weight='bold')
plt.title("Average number of surviving years in different scenarios", fontweight='bold')
plt.ylabel("Average surviving years", fontweight='bold')
plt.ylabel("Average TNT equivalent in each nuclear weapon (tons)", fontweight='bold')
plt.plot(x2,y1, label="10000Mt", linewidth = 3)
plt.plot(x2,y2, label="5000Mt", linewidth = 3)
plt.plot(x2,y3, label="3000Mt", linewidth = 3)
plt.plot(x2,y4, label="1000Mt", linewidth = 3)
plt.plot(x2,y5, label="500Mt", linewidth = 3)
plt.plot(x2,y6, label="100Mt", linewidth = 3)

plt.legend()
plt.savefig('results.png', dpi=500)
