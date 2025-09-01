def search(L, k):
    # Base case: empty list means not found
    if not L:
        return False
    
    mid = len(L) // 2
    
    if L[mid] == k:
        return True
    elif k < L[mid]:
        return search(L[:mid], k)      # search in left half
    else:
        return search(L[mid+1:], k)    # search in right half