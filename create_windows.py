import numpy as np

def overlapping_windows(df, window_size, overlap):
    arr = df.values
    num_arrays = int(np.ceil((len(arr) - window_size) / overlap)) + 1

    # Create an empty list to store the smaller arrays
    small_arrays = []

    # Extract the smaller arrays from the larger array using a loop
    for i in range(num_arrays):
        start = i * overlap
        end = start + window_size
        small_arrays.append(arr[start:end, :])

    # Print the shape of the first smaller array to verify that it has the desired size
    print(small_arrays[7])
   