import math
Mean=((10*2)+(15*1)+(20*1)+(25*1)+(30*2))/7
print(Mean)
def fact(n):
    if n == 0:
        return 1
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res
def pmf(x):
    formu=math.exp(-Mean)*Mean**x/fact(x)
    return formu
print("20 croissants: ",pmf(20))
print("15 croissants: ")
sum1=0
for i in range(15):
    sum1+=pmf(i)
print(sum1)
print("Standard Deviation: ",math.sqrt(Mean))