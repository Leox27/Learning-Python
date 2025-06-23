
def generateTable(n): # The value "n" is aking automatically by calling function at the end of the loop

    table = "" 
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)
