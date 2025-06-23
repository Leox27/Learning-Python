
lineno = 1

with open("log.txt") as f:
    lines = f.readlines()

for line in lines:

    if("python" in line):
        print(f"python in present line no.:{lineno}")
        break
    lineno += 1

else:
    print("python is Absent")

