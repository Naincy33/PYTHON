# Input Matrix A
print("Enter elements of 3x3 Matrix A:")
A = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    A.append(row)

# Input Matrix B
print("Enter elements of 3x3 Matrix B:")
B = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    B.append(row)

# Create empty 3x3 result matrix
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Multiply matrices
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]

# Print result
print("Resultant Matrix:")
for row in result:
    print(row)
