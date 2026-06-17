# Clean code: function name in snake_case & shorter variable name
def merge_sort(list_to_sort):
    """
    Sorts a list using the Merge Sort algorithm (in-place).
    """
    
    # Clean code: replace complex condition with return
    # Base case: a list of 0 or 1 element is already sorted
    if len(list_to_sort) <= 1:
        return 

    # Split list in two halves
    mid = len(list_to_sort) // 2
    left = list_to_sort[:mid]
    right = list_to_sort[mid:]

    # Recursive calls: sort both halves
    merge_sort(left)
    merge_sort(right)

    # Clean code: replaced unclear variable names (l, r, i)
    # Index pointers for left, right, and merged array
    left_index = 0
    right_index = 0
    merged_index = 0

    # Merge both sorted halves into original array
    while left_index < len(left) and right_index < len(right):
        
         # Compare elements from both halves and take the smaller one
        if left[left_index] <= right[right_index]:
            # Clean code: Removed unnecessary helper function (ASSIGNMENT)
            list_to_sort[merged_index] = left[left_index]
            left_index += 1
        else:
            list_to_sort[merged_index] = right[right_index]
            right_index += 1
        
        merged_index += 1

    # Copy remaining elements from left half (if any)
    while left_index < len(left):
        list_to_sort[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1

    # Copy remaining elements from right half (if any)
    while right_index < len(right):
        list_to_sort[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1


import matplotlib.pyplot as plt

# Sample data
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot before sorting
original = my_list.copy()

# Sort the list
merge_sort(my_list)

# Plots comparison
plt.plot(original, label="Before sorting")
plt.plot(my_list, label="After sorting")

plt.title("Merge Sort Comparison")
plt.legend()
plt.show()

