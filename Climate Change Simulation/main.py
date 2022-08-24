# -*- coding: utf-8 -*-

import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt
from random import randrange
from sklearn.metrics import r2_score
import math
from scipy.optimize import curve_fit


df = read_csv('global_temp.csv')
df = df[["Year","No_Smoothing"]]

X = df['Year'].to_numpy()[:-1].reshape(-1, 1)
y = df["No_Smoothing"].to_numpy()[:-1]
y = [float(i) for i in y]

x_data = []
x_data_pred = []
y_data = []
y_pred = []
for year in df["Year"]:
  x_data.append(int(year))

for i in range(1880, 2101):
  x_data_pred.append(i)

for data in df["No_Smoothing"]:
  y_data.append(data)


x_data2 = np.array(x_data)
y_data2 = np.array(y_data)

def fit_func(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

params = curve_fit(fit_func, x_data2, y_data2)
[a, b, c, d] = params[0]


for years in x_data_pred:
  y_pred.append(a*years**3 + b*years**2 + c*years + d)


plt.rcParams.update({'font.size': 22})
plt.scatter(x_data, y_data)
plt.xlabel("Years")
plt.ylabel("Differences in average temperature (ºC)")
plt.title("Global Average Temperature")
plt.plot(x_data_pred, y_pred, color="r")
plt.savefig('High_res__climate_model.png', dpi=500)
r2score = r2_score(y_data, y_pred[0:142])
print(r2score)


# 1. Assuming the tipping point starts at 2 degrees Celcius, and become absolutely unbearable at 10 degrees Celcius.
# 2. Let P(x) be the probebility of a catastrophic event occuring during the same year that we reached 12 degrees Celcius
# 3. Assume Linear probability mapping (2, 12) => (0, 99)
# 4. According to our model, we will reach 1.5 at 2141

# Steps to do for simulation:
# 1. Create mapping (1.5, 10) => (0%, 99%)
#    99/(12-2) = 9.9% # This means for every degree increase in temperature, we have a 9.9% increase in chance of catastrophe
# 2. Start Simulation

#y_pred  => temperate of that year, use it to minus 1.5 and then times by 11.647 to yield percentage.
# For example for a given year, we are at 4.5 degrees C => leads to roughly 33% catastrophe. 
# if randrange(100) smaller than ur percentage, then catastrophe heppened, therefore you break.

years = 0
n_epochs = 100000
res = []

for i in range(n_epochs):
  epoch_year = 0
  while True:
    temperature = y_pred[epoch_year] # temperature of that year
    chance = (temperature-2)*9.9 # probability of catastrophe
    chance = max(0,chance) 
    chance = min(99,chance)
    rand = randrange(101) #represents percentage
    if rand<chance: #catastrophe heppened
      res.append(epoch_year)
      break
    else:
      years += 1
      epoch_year += 1

print(years/n_epochs)

plt.rcParams.update({'font.size': 22})
plt.hist(res, bins=20)
plt.title('Climate Change Simulation Distribution')
plt.ylabel('Number of Simulations')
plt.xlabel('Years Survived')
plt.savefig("High resoltion climate dist.png",dpi=500)

