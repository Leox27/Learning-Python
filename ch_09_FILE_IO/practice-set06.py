with open("log.txt") as f:
    content = f.read()

if("python" in content):
        print("python in log.txt file")
else:
        print("python is not in log.txt file")
