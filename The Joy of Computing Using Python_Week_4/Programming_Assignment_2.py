def is_perfect(n: int) -> bool:
    if n <= 1:
        return False  # no perfect numbers below 2
    
    divisors_sum = 1  # start with 1 (always a divisor)
    
    # Check divisors only up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # avoid adding sqrt twice for perfect squares
                divisors_sum += n // i
    
    return divisors_sum == n
