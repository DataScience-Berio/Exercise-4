import matplotlib.pyplot as plt
from mergesort import merge_sort

# Sample data
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot before sorting
plt.plot(my_list)
plt.title("Before sorting")
plt.show()

# Sort the list
merge_sort(my_list)

# Plot after sorting
plt.plot(my_list)
plt.title("After sorting")
plt.show()s