import numpy as np
import math
from csv import writer
from sklearn import svm
from sklearn.svm import SVR
from pandas import read_csv
import matplotlib.pyplot as plt
from random import randrange
from sklearn.linear_model import LinearRegression

df = read_csv('flops.csv')

#plotting FLOPS vs Year
ye = [] #x
fl = [] #y
for elements in df["FLOPS"]:
    fl.append(elements)
for elements in df["Year"]:
    ye.append(elements)

plt.rc('font', weight='bold')
plt.rcParams.update({'font.size': 22})    
plt.rcParams['figure.figsize'] = (15,13)

plt.xlabel("Years", fontweight='bold')
plt.ylabel("Floating Point Operations per Second", fontweight='bold')
plt.title("FLOPS of Supercomputers from 1993-2021", fontweight='bold')
plt.plot(ye,fl)
plt.savefig('flops.png', dpi=500)

#plotting log base 10 of FLOPS for linearity
flops_log = [] #y
for elements in df["FLOPS"]: 
    flops_log.append(math.log(elements))

plt.xlabel("Years", fontweight='bold')
plt.ylabel("Log Base 10 of FLOPS", fontweight='bold')
plt.title("Log Base 10 of FLOPS of Supercomputers from 1993-2021", fontweight='bold')
plt.scatter(ye,flops_log)
plt.savefig('log_flops.png', dpi=500)

#prediction in FLOPS
for elements in df["FLOPS"]:
    df['FLOPS'] = df['FLOPS'].replace({elements: math.log(elements, 10)})

X = df['Year'].to_numpy().reshape(-1, 1)
y = df["FLOPS"].to_numpy()

reg = LinearRegression().fit(X, y)

years_want_to_predict = np.array(range(1993,2051)).reshape(-1, 1)
results = reg.predict(years_want_to_predict) 

for result in results:
    if 10**result >= 10**25:  
        print("----------------------------------------")
        print(result)

print(results)

plt.scatter(X,y)
plt.plot(years_want_to_predict,results, color="r")
plt.xlabel("Years", fontweight='bold')
plt.ylabel("Log Base 10 of FLOPS of Supercomputers", fontweight='bold')
plt.title("Predictions on FLOPS using Linear Regression", fontweight='bold')
plt.savefig('pred.png', dpi=500)

#for HPL-AI
x = ["Nov 2019", "June 2020", "Nov 2020", "June 2021", "Nov 2021"]
y = [0.45*10**18, 1.42*10**18, 2.0*10**18, 2.0*10**18, 2.000*10**18]
plt.plot(x,y)
plt.xlabel("Time", fontweight='bold')
plt.ylabel("HPL-AI readings (Eflop/s)", fontweight='bold')
plt.title("Readings based on HPL-AI benchmark 2019-2021", fontweight='bold')
plt.savefig('hpl-ai.png', dpi=500)