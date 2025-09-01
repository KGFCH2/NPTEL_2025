def multiply(a, b):
    # Base case: anything multiplied by 0 is 0
    if b == 0:
        return 0
    
    # Recursive case: add 'a' once and reduce 'b'
    return a + multiply(a, b - 1)