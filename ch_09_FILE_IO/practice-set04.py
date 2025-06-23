word = "Mayur"

with open("file04.txt", "r") as f:
    content = f.read()

contentnew = content.replace("Donkey", "######")

with open("file04.txt", "w") as f:
    f.write(contentnew)  # ✅ Write the modified content
