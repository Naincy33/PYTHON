def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
n = int(input("Enter a non-negative integer: "))
print("Single-digit result:", digital_root(n))
