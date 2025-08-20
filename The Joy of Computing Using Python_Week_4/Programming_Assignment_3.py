def birthday_twins(names_str, bdays_str):
    names = names_str.strip().split(",")
    bdays = list(map(int, bdays_str.strip().split(",")))

    by_day = {}
    for n, d in zip(names, bdays):
        by_day.setdefault(d, []).append(n)

    pairs = []
    for people in by_day.values():
        if len(people) > 1:
            people.sort()  # ensure name1 < name2 inside each pair
            for i in range(len(people) - 1):
                for j in range(i + 1, len(people)):
                    pairs.append(f"{people[i]},{people[j]}")

    # Required for TC2: sort all pairs globally (lexicographic)
    pairs.sort()
    return "\n".join(pairs)


if __name__ == "__main__":
    import sys
    names = sys.stdin.readline().strip()
    bdays = sys.stdin.readline().strip()
    sys.stdout.write(birthday_twins(names, bdays))  # no trailing newline
