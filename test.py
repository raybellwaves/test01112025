import random
import pandas as pd
import numpy as np


def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


# Example usage
random_list = generate_random_list(10, 1, 100)
print(random_list)

# Create a pandas DataFrame from the random list
df = pd.DataFrame(random_list, columns=["Random Numbers"])

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv("random_numbers.csv", index=False)

# Create a random numpy array
random_array = np.random.randint(1, 100, size=10)
print("NumPy array:", random_array)

x = np.array(
    [
        1,
        2,
        3,
        4,
        5,
    ]
)
