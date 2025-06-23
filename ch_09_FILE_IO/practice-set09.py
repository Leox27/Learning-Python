# Content matching of files


with open("this.txt", "r") as f:
    content1 = f.read()

with open("thi_copy.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Content of both file matches")
else:

    print("Content of both file  are differbnet")
    