import time, sys, os, subprocess, re
list = str(list(range(2, 30)))

def Z():
 print('''
1.spisok
2.add
3.delete
4.zamenit''')
 asa = input('aaaa: ')
 if asa == '1':
  z1()
 elif asa == '2':
  z2()
 elif asa == '3':
  z3()
 elif asa == '4':
  z4()

def z1():
 z1_2()
 with open('nanu.txt') as f3:
  for n, line in enumerate(f3, 1):
   line1 = line.rstrip('\n')
   print(f'[{n}] {line1}')

def z1_2():
 File1 = 'name.txt'
 File2 = 'numbers.txt'
 File3 = 'nanu.txt'
 TemporaryFile3 = File3 + '.tmpp' # создаём файл
 os.system("touch %s" % TemporaryFile3) # временный файл
 with open(File1, 'r') as f1, open(File2, 'r') as f2, open(TemporaryFile3, 'w') as f4:
  for i, j in zip(f1.readlines(), f2.readlines()):
   f4.write(f'{i.strip()}: {j}')
 path3 = os.path.join(os.path.abspath(os.path.dirname(__file__)), File3)
 os.remove(path3) # удаляем основной файл
 os.system("mv %s %s" % (TemporaryFile3, File3))

def z3():
 File1 = 'name.txt'
 File2 = 'numbers.txt'
 z3z4_2(File1, File2)
 hh = int(jek)
 hh -= 1
 if str(hh) in list:
  with open(File1) as f1, open(File2) as ff1:
   lines1 = f1.readlines() # список текста в линию
   lines2 = ff1.readlines() # [(1, 2, 3, 4, 5)]
   del lines1[hh]
   del lines2[hh]
  with open('name.txt', 'w') as f1, open('numbers.txt', 'w') as ff1: # открытие файла
   f1.writelines(lines1)
   ff1.writelines(lines2)

def z2():
 with open('numbers.txt','a') as f,  open('name.txt', 'a') as f1:
  xx = input('Введите имя: ')
  f1.write(f'\n{xx}')
  xxx = input('Введите номер: ')
  f.write(f'\n{xxx}')
  print(f'Добавлено имя: {xx}')
  print(f'Добавлен номер: {xxx}')

def z3z4_2(File1, File2):
 z1()
 global jek
 jek = input('Строка: ')
 if jek in list:
  with open(File1) as fff1, open(File2) as fff2:
   h = int(jek)
   h -= 1
   h = h
   x = 0
   xx = 0
   for line1 in fff1:
    if x == h: #строка
     global nomer1
     nomer1 = line1.split()[0]
    x += 1
   for line2 in fff2:
    if xx == h: #строка
     global nomer2
     nomer2 = line2.split()[0] #слово в строке
    xx += 1

def z4_3(File1, File2, FindThis1, FindThis2, new1, new2):
 TemporaryFile1 = File1 + '.tmp' ; TemporaryFile2 = File2 + '.tmp'   # создаём файл
 os.system("touch %s" % TemporaryFile1) ; os.system("touch %s" % TemporaryFile2)    # временный файл

 with open(File1, 'r') as f1, open(TemporaryFile1, 'w') as f2, open(File2, 'r') as ff1, open(TemporaryFile2, 'w') as ff2:
  lines1 = f1.readlines() ; lines2 = ff1.readlines()
  for line1 in lines1:
   line1 = line1.strip()
   if line1 == FindThis1:
    f2.write(f'{new1}') # меняем строку
   else:
    f2.write(line1 + '\n') # оставляем прежнюю
  for line2 in lines2:
   line2 = line2.strip()
   if line2 == FindThis2:
    ff2.write(f'{new2}') # меняем строку
   else:
    ff2.write(line2 + '\n') # оставляем прежнюю

 path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), File1) ; path2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), File2)
 os.remove(path1) ; os.remove(path2) # удаляем основной файл
 os.system("mv %s %s" % (TemporaryFile1, File1)) ; os.system("mv %s %s" % (TemporaryFile2, File2)) # переименовываем временный файл

def z4():
 File1 = 'name.txt'
 File2 = 'numbers.txt'
 z3z4_2(File1, File2)
 FindThis1 = nomer1
 FindThis2 = nomer2
 new1 = input('Введите новое имя: ')
 new2 = input('Введите новый номер: ')
 result12 = z4_3(File1, File2, FindThis1, FindThis2, new1, new2)

while list:
    Z()

Z()
