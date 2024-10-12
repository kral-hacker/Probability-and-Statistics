pmf_X = {-2: 0.25, -1: 0.125, 0: 0.125, 1: 0.25, 2:0.25 }

def pmf_Y(pmf_X):
    pmf_Y = {}
    for x, px in pmf_X.items():
        y = (x + 1)**2
        if y in pmf_Y:
            pmf_Y[y] += px
        else:
            pmf_Y[y] = px
    return pmf_Y

# Calculate the PMF of Y
pmf_Y_result = pmf_Y(pmf_X)

# Find the range of Y
range_Y = sorted(pmf_Y_result.keys())

print("Range of Y:", range_Y)
print("PMF of Y:")
for y in range_Y:
    print(f"Y = {y}: P(Y = {y}) = {pmf_Y_result[y]}")