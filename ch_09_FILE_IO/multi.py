# For multi cout word


count = 0  # To store total number of occurrences

with open("log.txt") as f:
    lines = f.readlines()

for lineno, line in enumerate(lines, start=1):
    if "python" in line:
        count += line.count("python")  # Count all occurrences in the line

if count > 0:
    print(f'"python" is present {count} time(s) in the file.')
else:
    print('"python" is absent in the file.')
