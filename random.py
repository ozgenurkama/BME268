message = input("Enter message: ")
result = ""

for char in message:
    if char.isalpha():
        new_char = chr(ord(char) + 3)
        result = result + new_char
    else:
        result = result + char

print("Encrypted:", result)