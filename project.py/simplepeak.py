def find_peak(arr):
    n = len(arr)

    if n == 0:
        return None  # No elements

    if n == 1:
        return arr[0]  # Only one element

    # Check first element
    if arr[0] >= arr[1]:
        return arr[0]

    # Check last element
    if arr[n - 1] >= arr[n - 2]:
        return arr[n - 1]

    # Check middle elements
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]

    return None  # No peak found (theoretically not possible if array has at least one element)

# Example usage:
arr = [1, 3, 3, 4, 1, 1]
print(find_peak(arr))  # Output: 20
