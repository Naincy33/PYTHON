def sum_primes_sieve(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]  # 0 and 1 are not primes

    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num*num, limit, num):
                sieve[multiple] = False

    # Sum of indices (i.e., the primes)
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

# Example usage
limit = 2000000
print("Sum of all primes below", limit, "is:", sum_primes_sieve(limit))
