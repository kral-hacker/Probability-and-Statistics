import scipy.stats as stats

x = 80
mean = 75
stdeviation = 10
z = (x - mean) / stdeviation

print("Value of z score is:", z)
print("Probability:",1-stats.norm.cdf(z))
