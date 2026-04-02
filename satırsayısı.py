xfile = open('dosya.txt')
count = 0

for line in xfile:
    count = count + 1

print('Satır Sayısı:', count)