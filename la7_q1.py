def nCr(n, r):
 
    return (fact(n) / (fact(r)
                * fact(n - r)))
 
def fact(n):
    if n == 0:
        return 1
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res

p=0.4
q=0.6               
n=10
def pmf(x):
    formula = nCr(n,x)*(p**x)*(q**(n-x))
    return formula
pmf()
# print(nCr(3,2))
# print("Random Variable ","Probability ")
# for i in range(4):
#     print("X = ",i," ",pmf(i))

    

