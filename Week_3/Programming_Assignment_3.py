# Read the size of the square matrices
n = int(input())

# Read matrix A
A = []
for _ in range(n):
    row = list(map(int, input().split(',')))
    A.append(row)

# Read matrix B
B = []
for _ in range(n):
    row = list(map(int, input().split(',')))
    B.append(row)

# Initialize result matrix with zeros
result = [[0 for _ in range(n)] for _ in range(n)]

# Perform matrix multiplication: result[i][j] = sum of A[i][k] * B[k][j]
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += A[i][k] * B[k][j]

# Output the result matrix with comma-separated values
for row in result:
    print(','.join(map(str, row)))
