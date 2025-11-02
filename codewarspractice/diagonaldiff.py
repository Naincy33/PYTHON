def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - i - 1]
    
    return abs(primary_sum - secondary_sum)
