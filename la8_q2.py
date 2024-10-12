dataset = {1: 0.25, 2: 0.65, 3: 0.10, 4: 0.50, 5: 0.80, 6: 0.30, 7: 0.70, 8: 0.40, 9: 0.20, 10: 0.60}

min_value = min(dataset.values())
max_value = max(dataset.values())

# pdf = 1 / (max_value - min_value)

# def cdf(x):
#     return (x - min_value) / (max_value - min_value)

# lower_bound = 0.4
# upper_bound = 0.7
# probability_within_interval = cdf(upper_bound) - cdf(lower_bound)

# print(f"Interval[{min_value}, {max_value}]")
# print(f"(PDF): {pdf:.2f}")
# print(f"(CDF): F(x) = (x - {min_value}) / ({max_value} - {min_value})")
# print(f"Q4:Interval [{lower_bound}, {upper_bound}]: {probability_within_interval:.4f}")jj





mean = sum(dataset.values()) / len(dataset)

variance = sum((x - mean) ** 2 for x in dataset.values()) / len(dataset)




values_outside_interval = [key for key, value in dataset.items() if value < min_value or value > max_value]


print(f"1. E(x): {mean:.2f}")
print(f"2. Variance: {variance:.2f}")
print("3. Values outside the specified interval:")
if values_outside_interval:
    print(values_outside_interval)
else:
    print("None")

