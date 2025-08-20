def find_factors(n):
    """Return all positive factors of n"""
    return [i for i in range(1, n + 1) if n % i == 0]

def common_factors(a, b):
    """Return common factors of a and b"""
    return [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]

def factors_upto_n(n):
    """Return dictionary of factors for all numbers from 1 to n"""
    return {i: find_factors(i) for i in range(1, n + 1)}

# Main program
choice = int(input().strip())

if choice == 1:
    n = int(input().strip())
    print(find_factors(n))

elif choice == 2:
    a = int(input().strip())
    b = int(input().strip())
    print(common_factors(a, b))

elif choice == 3:
    n = int(input().strip())
    print(factors_upto_n(n))

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
