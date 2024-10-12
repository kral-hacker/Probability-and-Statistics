import random
import  statistics
import math 
x_data=[]
y_data=[]
for i in range(50):
    a=random.randrange(1,100)
    x_data.append(a)
for i in range(50):
    b=random.randrange(1,100)
    y_data.append(b)
#finding the mean of both the datasets
print("Mean of x_data",statistics.mean(x_data))
print("Mean y_data",statistics.mean(y_data))

def calculate_Correlation(x_data,y_data):
    sigmaxy=0
    for i in range(len(x_data)):
        sigmaxy+=(x_data[i]*y_data[i])
    sigmax=0
    for i in range(len(x_data)):
        sigmax+=x_data[i]
    sigmay=0
    for i in range(len(x_data)):
        sigmay+=y_data[i]
    sigmaxsqr=0
    for i in range(len(x_data)):
        sigmaxsqr+=(x_data[i]**2)
    sigmaysqr=0
    for i in range(len(x_data)):
        sigmaysqr+=(y_data[i]**2)
    n=len(x_data)
    num = n*sigmaxy-sigmax*sigmay
    den = math.sqrt(n*sigmaxsqr-sigmax**2)*math.sqrt(n*sigmaysqr-sigmay**2)
    r=num/den
    return r
print("Correlation coefficient: ")
print(calculate_Correlation(x_data,y_data))

