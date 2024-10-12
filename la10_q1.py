import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.pyplot as plt
import random
import statistics

def sn(n):
  a = 2
  cr = 5
  cd = 4
  s = (a + (n-1)*cd) * (cr **(n-1))
  return s


l = []
for i in range(1 , 201):
  for j in range(0 , i):
    l.append(sn(i))
print(len(l))

arr = np.array(l)
logmean = []
logmedian = []
logmode = []
for i in range(1 ,51):
  data = random.sample(l , i * 10)
  mean = sum(data) / len(data)
  mode = statistics.mode(data)
  median = statistics.median(data)
  logmean.append(round(np.log(mean / 10**130), 2))
  logmedian.append(round(np.log(median / 10**130), 2))
  logmode.append(round(np.log(mode / 10**130), 2))

plt.bar(range(len(logmedian)), logmean)
plt.show()