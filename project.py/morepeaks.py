def find_all_peaks(arr, low, high):
    peaks = []  # List to store all peaks found

    if low > high:
        return peaks

    mid = (low + high) // 2

    # Safe neighbors
    left = arr[mid - 1] if mid - 1 >= 0 else float('-inf')
    right = arr[mid + 1] if mid + 1 < len(arr) else float('-inf')

    # Case 1: mid is a peak
    if arr[mid] >= left and arr[mid] >= right:
        peaks.append(arr[mid])

    # Case 2: move left
    if left > arr[mid]:
        peaks.extend(find_all_peaks(arr, low, mid - 1))

    # Case 3: move right
    if right > arr[mid]:
        peaks.extend(find_all_peaks(arr, mid + 1, high))

    # Case 4: when left == mid == right, search both sides
    if left == arr[mid] == right:
        peaks.extend(find_all_peaks(arr, low, mid - 1))
        peaks.extend(find_all_peaks(arr, mid + 1, high))

    return peaks


# Example usage:
arr = [1, 2, 1, 4, 1, 1, 5, 0]
print(find_all_peaks(arr, 0, len(arr) - 1))
