words =["Donkey", "bad ", "Ganda"]

with open("file04.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" *len(word))

with open("file04.txt", "w") as f:
    f.write(content)