p=0.02
x=7
def pmf():
    formu=p*((1-p)**(x-1))
    return formu
print("Probability: ",pmf())
print("Expectation : ",(1/p))