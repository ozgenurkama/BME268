sentence = input("Cümle: ")
trimmed = sentence.strip()
upper_case = trimmed.upper()
replaced = upper_case.replace("BAD", "GOOD")

print(trimmed)
print(upper_case)
print(replaced)