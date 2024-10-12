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
x_m=statistics.mean(x_data)
y_m=statistics.mean(y_data)

sum=0
for i in range(len(x_data)):
    sum+=(x_data[i]-x_m)*(y_data[i]-y_m)
N=len(x_data)
cov=sum/N
print("Covariance = ",cov)

