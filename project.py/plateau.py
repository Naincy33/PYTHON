def find_peak_with_duplicates(arr, low, high):
    if low > high:
        return None

    mid = (low + high) // 2

    # Safe neighbors
    left = arr[mid - 1] if mid - 1 >= 0 else float('-inf')
    right = arr[mid + 1] if mid + 1 < len(arr) else float('-inf')

    # Case 1: mid is a peak
    if arr[mid] >= left and arr[mid] >= right:
        return arr[mid]

    # Case 2: move left
    if left > arr[mid]:
        return find_peak_with_duplicates(arr, low, mid - 1)

    # Case 3: move right
    if right > arr[mid]:
        return find_peak_with_duplicates(arr, mid + 1, high)

    # Case 4: when left == mid == right, search both sides
    left_peak = find_peak_with_duplicates(arr, low, mid - 1)
    if left_peak is not None:
        return left_peak

    return find_peak_with_duplicates(arr, mid + 1, high)

# Example usage:
arr = [1, 2, 2, 2, 2, 3, 2, 1]
print(find_peak_with_duplicates(arr, 0, len(arr) - 1))
