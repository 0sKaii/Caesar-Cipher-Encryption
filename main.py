text = input(" Enter the text you want to encrypt (CAPITAL letters only): ")

k = 3
result = ""

for i in range (len(text)):
    char = text[i]

    s = chr((ord(char) - 65 + k) % 26 + 65)
    result += s

print(f" Encrypted result: {result}")
