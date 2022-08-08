import numpy as np
#from matplotlib import pyplot as plt


M=100000                                   #The running epoch
N_0=5158274.0                              #The critical number of nuclear warheads in the unit of Hiroshima nuclear bomb
baseline=3000.0*10**6
Hiroshima=20000.0
NW=baseline/Hiroshima
# a_0=3.26897*10**-8
# a_1=-1.37096*10**-13
# a_2=1.56108*10**-19
# a_3=-2.53493*10**-26
N=np.zeros(M+1)                            #Create an array to save the number of nuclear warheads in each year
year=np.zeros(M+1)                         #Create an array to save the surviving year in each epoch
epoch=0.0                                  #The counter and it will be M(100000) in theory
C=np.array([[12.0*N_0,6*N_0**2,4.0*N_0**3,3.0*N_0**4],[1.0,N_0,N_0**2,N_0**3],[1.0,NW,NW**2,NW**3],[0.0,1.0,2.0*NW,3.0*NW**2]])
B=np.array([12,0,0,0])
A=np.dot(np.linalg.inv(C),B)
D=np.array([190575.0,254100.0,317625.0,381150.0,444675.0,508200.0,571725.0,635250.0])



def P(x):                                  #Define the probability function
    P=A[0]+A[1]*x**2+A[2]*x**3+A[3]*x**4
    return P

for k in range(8):
    N=np.zeros(M+1)
    year=np.zeros(M+1)
    epoch=0.0
    N[0]=D[k]
    for i in range (M):                        #Program loop in each epoch
        for j in range (20000):                #Program loop in one epoch
            t=np.random.normal(0.0,0.01541)    #Random sampling in a normal distribution for the increasing or decreasing rate
            N[j+1]=N[j]*(1+t)                  #Calculate the number nuclear warheads of next year according to that of the last year
            P_j=P(N[j])                        #Calculate the probability
            trial=np.random.uniform(0.0,1.0)   #Random sampling in a uniform distribution in the range from 0 to 1 as a criterion
            if P_j<=trial:                     #Determine whether civilization can survive
                year[i]+=1                     #Succeed in surviving into the next year
            else:
                break                          #Fail in surviving into the next year
        epoch+=1                                  #One epoch is end and move to next epoch

    average_surviving_year=sum(year)/epoch     #Calculate the average surviving year in each epoch
    print('The average survive epoch is ',epoch)                    #Print the result
    print(k)
    print('The average survive year is ',average_surviving_year)    #Print the result





