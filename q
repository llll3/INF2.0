f = open("numbers.txt", "r")
h = int(input('lohin'))
h -= 1
x = 0
for line in f:
    if x == h: #строка
        print(line.split()[0]) #слово в строке
        print(h)
f.close()
