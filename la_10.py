# import scipy.stats as st


# mean = 527
# std_dev = 112


# score_a = 500
# z_score_a = (score_a - mean) / std_dev
# probability_a = 1 - st.norm.cdf(z_score_a)
# print(f"a) Probability of scoring above 500: {probability_a:.4f}")


# percentile_95 = st.norm.ppf(0.95)
# score_b = percentile_95 * std_dev + mean
# print(f"b) GMAT score to be in the highest 5%: {score_b:.2f}")






# import math

# # Given parameter lambda
# lambda_param = 2

# # a) Probability that a shower will last more than three minutes
# probability_a = math.exp(-lambda_param * 3)
# print(f"a) Probability that a shower will last more than three minutes: {probability_a:.4f}")

# # b) Probability that a shower lasting 2 minutes will last for at least one more minute
# probability_b = math.exp(-lambda_param * 1)
# print(f"b) Probability that a shower lasting 2 minutes will last for at least one more minute: {probability_b:.4f}")


# score_c1 = 527
# z_score_c1 = (score_c1 - mean) / std_dev
# score_c2 = 554
# z_score_c2 = (score_c2 - mean) / std_dev
# probability_c = st.norm.cdf(z_score_c2) - st.norm.cdf(z_score_c1)
# print(f"c) Probability of scoring between 527 and 554: {probability_c:.4f}")

# import math


# lambda_original = 0.0003
# lambda_redesigned = 0.00035


# probability_original = math.exp(-lambda_original * 10000)
# print(f"a) Proportion of fans (original) lasting at least 10000 hours: {probability_original:.4f}")


# probability_redesigned = math.exp(-lambda_redesigned * 10000)
# print(f"b) Proportion of fans (redesigned) lasting at least 10000 hours: {probability_redesigned:.4f}")



import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)

random_numbers = np.random.normal(loc=7, scale=8, size=9000)


logged_numbers = np.log(random_numbers)

logged_numbers = logged_numbers[~np.isnan(logged_numbers)]

# Calculate mean and standard deviation of the remaining numbers
mean_logged = np.mean(logged_numbers)
std_dev_logged = np.std(logged_numbers)

print(f"Mean of logged numbers: {mean_logged:.4f}")
print(f"Standard Deviation of logged numbers: {std_dev_logged:.4f}")

# Plot histogram of the logged array
plt.hist(logged_numbers, bins=30, density=True, alpha=0.6, color='g')
plt.title('Histogram of Logged Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Check if the transformed array follows lognormal distribution or not
plt.figure()
plt.hist(np.exp(logged_numbers), bins=30, density=True, alpha=0.6, color='b')
plt.title('Histogram of Exponentiated Logged Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()