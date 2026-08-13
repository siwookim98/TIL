alphabet = input()
letter = ''
for i, text in enumerate(alphabet):
    if i % 2 == 0:
        letter += text
print(letter)