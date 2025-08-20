def list_util(L, command):
    if command == "is_empty":
        return len(L) == 0

    elif command == "first":
        return L[0] if L else None

    elif command == "last":
        return L[-1] if L else None

    elif command == "init":
        return L[:-1] if L else []

    elif command == "rest":
        if not L:
            return None
        return L[1:]

    else:
        raise ValueError("Invalid command")
