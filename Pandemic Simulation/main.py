import numpy as np
import matplotlib.pyplot as plt
import random
from random import randrange

years = 0
n_epochs = 100000
res1 = []

for i in range(n_epochs):
  year = 0
  while True:
    rand = randrange(100000)
    if rand<5768:
      res1.append(year)
      break
    else:
      years += 1
      year += 1

print(years/n_epochs)

plt.rc('font', weight='bold')
plt.rcParams.update({'font.size': 22})
plt.rcParams["figure.figsize"] = (15,15)
plt.hist(res1, bins=20, range = (0,800))
plt.title('Pandemic Simulation Distribution', fontweight="bold")
plt.ylabel('Number of Simulations', fontweight="bold")
plt.xlabel('Years Survived', fontweight="bold")
plt.savefig('pandemic.png', dpi=500)