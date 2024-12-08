__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"


# User input for the number of terms to calculate in the sum
n = int(input("Enter the value of n: "))

# Initialize the sum S to 0
S = 0

# Calculate the summation
for k in range(1, n + 1):
    # Calculate factorial of k directly
    k_factorial = 1
    for i in range(1, k + 1):
        k_factorial *= i  # Multiply k_factorial by each integer up to k
    
    # Calculate the term k! / (k + 1)
    term = k_factorial / (k + 1)
    # Add the term to the total sum S
    S += term

# Output the calculated sum
print("The calculated sum S is:", S)
