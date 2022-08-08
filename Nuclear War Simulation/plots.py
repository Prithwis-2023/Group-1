import numpy as np
import math
from sklearn import svm
from sklearn.svm import SVR
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
import random
from random import randrange
from csv import writer


df1 = read_csv('nuclear.csv')

x = []
for elements in df["Year"]:
  if elements not in x:
    x.append(elements) 
for i in range(2015, 2023):
  x.append(i)


years = []
for elements in df["Year"]:
  if elements not in years:
    years.append(elements)

whole = []
for year in years:
  new = df.loc[df['Year'] == year, 'Nuclear weapons inventory by country (FAS Nuclear Notebook)'].tolist()
  total = sum(new)
  whole.append(total)
plt.rcParams.update({'font.size': 22})
plt.rcParams["figure.figsize"] = (15,13)
plt.title("Estimated Global Nuclear Warheads Inventory (1945-2022)")
plt.xlabel("Years")
plt.ylabel("Nuclear Weapons Inventory")
plt.plot(x,whole, color="b", label="Global")
plt.savefig('nuclear_global.png', dpi=500)


df2 = pd.read_csv('Total nuclear result.csv')
x = []
for elements in df2["Average TNT equivalent(tons)"]:
    x.append(elements)
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []

for elements in df["10000Mt"]:
    y1.append(elements)

for elements in df["5000Mt"]:
    y2.append(elements)

for elements in df["3000Mt"]:
    y3.append(elements)

for elements in df["1000Mt"]:
    y4.append(elements)

for elements in df["500Mt"]:
    y5.append(elements)

for elements in df["100Mt"]:
    y6.append(elements)

plt.title("Average number of surviving years in different scenarios")
plt.ylabel("Average surviving years")
plt.ylabel("Average TNT equivalent in each nuclear weapon (tons)")
plt.plot(x,y1, label="10000Mt")
plt.plot(x,y2, label="5000Mt")
plt.plot(x,y3, label="3000Mt")
plt.plot(x,y4, label="1000Mt")
plt.plot(x,y5, label="500Mt")
plt.plot(x,y6, label="100Mt")

plt.legend()
plt.savefig('results.png', dpi=500)
