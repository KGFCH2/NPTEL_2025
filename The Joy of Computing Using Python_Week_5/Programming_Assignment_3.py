def exact_count(para: str, n: int) -> bool:
    # Split paragraph into words
    words = para.split()
    
    # Count occurrences of each word
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    
    # Check if any word occurs exactly n times
    return any(count == n for count in freq.values())
