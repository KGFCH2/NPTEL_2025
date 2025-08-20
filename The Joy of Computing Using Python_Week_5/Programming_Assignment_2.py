import sys

def read_nonempty():
    """Read next non-empty stripped line (skips blank lines)."""
    while True:
        s = sys.stdin.readline()
        if s == "":      # EOF
            return ""
        s = s.strip()
        if s != "":
            return s

station_dict = {}

# read number of trains
n_line = read_nonempty()
if n_line == "":
    sys.stdout.write("{}")
    sys.exit(0)
n = int(n_line)

for _ in range(n):
    train_name = read_nonempty()
    m = int(read_nonempty())

    compartments = {}
    for _ in range(m):
        line = read_nonempty()                   # handles accidental blank lines
        comp, passengers = map(str.strip, line.split(",", 1))
        compartments[comp] = int(passengers)

    station_dict[train_name] = compartments

# Build a deterministically ordered dict (sorted trains, sorted compartments)
ordered = {}
for train in sorted(station_dict):               # alphabetical train order
    inner = station_dict[train]
    ordered_inner = {}
    for comp in sorted(inner):                   # alphabetical compartment order
        ordered_inner[comp] = inner[comp]
    ordered[train] = ordered_inner

# Print without an extra newline to avoid presentation issues
sys.stdout.write(str(ordered))
