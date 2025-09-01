def matmul(X, Y):
    """Multiply two square matrices X and Y."""
    n = len(X)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def power(A, m):
    """Recursively compute matrix power A^m."""
    if m == 1:
        return A
    
    if m % 2 == 0:
        half = power(A, m // 2)
        return matmul(half, half)
    else:
        return matmul(A, power(A, m - 1))