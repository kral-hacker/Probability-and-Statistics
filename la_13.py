import numpy as np
import matplotlib.pyplot as plt


r1 = 0.35
samplesize = 30
num_cities = 500

customer_1 = np.random.exponential(scale=1/r1, size=(num_cities, samplesize))
mean_1 = np.mean(customer_1)
std_1 = np.std(customer_1)
sampling_mean_1 = np.mean(customer_1, axis=1)
std_dev_sampling_1 = np.std(sampling_mean_1)
print("Test Case 1 (r=0.35):")
print("Customer behavior mean:", mean_1)
print("Customer behavior standard deviation:", std_1)
print("Sampling distribution standard deviation:", std_dev_sampling_1*5.477)



r2 = 0.65
customer_2 = np.random.exponential(scale=1/r2, size=(num_cities, samplesize))
mean_2 = np.mean(customer_2)
std_2 = np.std(customer_2)
sampling_mean_2 = np.mean(customer_2, axis=1)
std_dev_sampling_2 = np.std(sampling_mean_2)

print("\nTest Case 2 (r=0.65):")
print("Customer behavior mean:", mean_2)
print("Customer behavior standard deviation:", std_2)
print("Sampling distribution standard deviation:", std_dev_sampling_2*5.477)



