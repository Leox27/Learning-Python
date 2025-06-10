# replace name and date given string

letter = '''Dear <|name|>
You are selected !
<|Date|>
'''

print(letter.replace("<|name|>", "Mayur").replace("<|Date|>", "Oct 10th"))