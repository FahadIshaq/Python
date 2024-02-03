# Function to calculate the GCD using the Euclidean algorithm
def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

# Given values
M = 1069811
N = 1056617

# Calculate the GCD
result = gcd_euclidean(M + 9365326, N + 856957)

# Print the result
print("GCD of (M + 9365326) and (N + 856957) is:", result)
