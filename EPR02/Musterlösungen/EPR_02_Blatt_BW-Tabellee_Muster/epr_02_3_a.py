__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"

# User input for the number of Fibonacci numbers to calculate
n = int(input("Enter the number of Fibonacci numbers: "))

# Starting values for the Fibonacci sequence
fibonacci_sequence = [1, 1]  # The sequence begins with 1, 1

# Calculate the Fibonacci sequence up to the nth number
for i in range(2, n):
    # The next number in the sequence is the sum of the two previous numbers
    next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_number)  # Add the new number to the sequence

# Output the calculated Fibonacci sequence
print("Fibonacci Sequence:", ", ".join(map(str, fibonacci_sequence[:n])))
