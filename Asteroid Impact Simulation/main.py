import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.svm import SVR
from pandas import read_csv
import matplotlib.pyplot as plt
import random
from random import randrange

df = pd.read_csv("asteroid.csv")

df2 = df[(df['Estimated Diameter (km)'] > 0.14) & (df['H (mag)'] <= 22)]

dia = []
pal = []
dia2 = []
pal2 = []

for diam in df2["Estimated Diameter (km)"][2:]:
    dia.append(diam)
for palermo in df2["Palermo Scale (max.)"][2:]:
    pal.append(palermo)
for element in df2["Estimated Diameter (km)"][:2]:
    dia2.append(element)
for element in df2["Palermo Scale (max.)"][:2]:
    pal2.append(element)    
plt.rcParams.update({'font.size': 22})
plt.rcParams["figure.figsize"] = (12,10)
plt.rc('font', weight='bold')
plt.scatter(pal, dia, s=500)
plt.scatter(pal2, dia2, s=500, color="red")
plt.title('Potentialy Hazardous Asteroids', fontweight='bold')
plt.xlabel("Palermo Scale (max.)", fontweight='bold')
plt.ylabel("Estimated Diameter (km)", fontweight='bold')
plt.savefig('asteroid_data.png', dpi=500)

impact_probs = []
for elements in df2["Impact Probability (cumulative)"]:
  impact_probs.append(elements)

upper_bound = max(impact_probs)*100000
lower_bound = min(impact_probs)*100000


years = 0
n_epochs = 100000
res1 = []
data1 = []
for i in range(n_epochs):
  year = 0
  probs = randrange(12, 57)
  data1.append(probs/100000)
  while True:
    rand = randrange(100000)
    if rand < 57:
      res1.append(year)
      break
    else:
      years += 1
      year += 1

print("Number of Survival years for this simulation run: ", years/n_epochs)

plt.hist(res1, bins=20, range = (0,20000))
plt.title('Asteroid Impact Simulation Distribution')
plt.ylabel('Number of Simulations')
plt.xlabel('Years Survived')
plt.savefig('distribution.png', dpi=500)

