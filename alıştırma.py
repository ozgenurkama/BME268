word = input("Bir kelime girin: ").lower()
count = 0
vowels = "aeiou"

for letter in word:
    if letter in vowels:
        count = count + 1

print("Sesli harf sayısı:", count)