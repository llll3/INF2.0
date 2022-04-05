import time, sys, os, subprocess, re
list1 = str(list(range(2, 51)))
zel = '\033[32m'
kras = '\033[31m'
jir = '\033[1m'
kon = '\033[m'
fio = '\033[35m'
kjir = kon + jir
list2 = str(list(range(1, 5)))
ff = "('clear')"
def test():
 with open('nanu.txt') as f:
  jj = len(f.readlines())
  print(jj)
def Z():
 os.system(ff)
 print(f'''{jir}[&] ?
[0] Выход
[1] список
[2] добавить
[3] удалить
[4] редактировать{kjir}''')
 global asa
 asa = input('-->: ')
 if asa == '0':
  sys.exit()
 if asa == '1':
  z1()
 elif asa == '2':
  z2()
 elif asa == '3':
  z3()
 elif asa == '4':
  z4()
 elif asa != list2:
  Z()

def z1():
 j = jir
 z1_2()
 x = 0
 test()
 if asa == '1':
  os.system(ff)
  print('[&] Список: ')
  print('[0] Назад')
 if asa == '3':
  print('[&] Удалить: ')
 if asa == '4':
  print('[&] Изменить')

 with open('nanu.txt') as f3:
  for n, line in enumerate(f3, 1):
   kk = '[&] Список:\n[0] Назад'
   line1 = line.rstrip('\n')
   print(f'[{n}] {line1}')
 if asa == '1':
  cc = input('--> ')
  if cc == '0':
   Z()
  else:
   os.system(ff)
   z1()

def z1_2():
 File1 = 'names.txt'
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
 jj = kjir
def z3():
 os.system(ff)
 z1()
 File1 = 'names.txt'
 File2 = 'numbers.txt'
 z3z4_2(File1, File2)
 hh = jek
 hh -= 1
 hh = hh
 if hh in list1:
  with open(File1) as f1, open(File2) as ff1:
   lines1 = f1.readlines() # список текста в линию
   lines2 = ff1.readlines() # [(1, 2, 3, 4, 5)]
   g1 = lines1[hh]
   g2 = lines2[hh]
   print(f'Удалено имя: {g1}')
   print(f'Удалён номер: {g2}')
   del lines1[hh]
   del lines2[hh]
  with open(File1, 'w') as f1, open(File2, 'w') as ff1: # открытие файла
   f1.writelines(lines1)
   ff1.writelines(lines2)
 else: z3()

def z2():
 os.system(ff)
 print('[&] Добавить')
 print('[0] Назад')
 print('[1] Продолжить')
 File1 = 'names.txt'
 File2 = 'numbers.txt'
 xx = input('--> ')
 if xx == '0': Z()
 if xx == '1':
  with open(File1,'a') as f1,  open(File2, 'a') as ff1:
   xx = input('Введите имя: ')
   f1.write(f'\n{xx}')
   xxx = input('Введите номер: ')
   ff1.write(f'\n{xxx}')
   os.system(ff)
   print(f'{ jir + zel}Добавлено имя: {xx}{kjir}')
   print(f'{zel}Добавлен номер: {xxx}{kon}')
   time.sleep(2)
   z2()
 else: z2()

def z3z4_2(File1, File2):
 global jek
 jek = str(input('Введите поряд.номер: '))
 if jek == list1:
  with open(File1) as fff1, open(File2) as fff2:
   h = jek
   h -= 1
   h = h
   x = 0
   xx = 0
   for line1 in fff1:
    if x == str(f'{h}'): #строка
     global nomer1
     nomer1 = line1.split()[0]
    x += 1
   for line2 in fff2:
    if xx == h: #строка
     global nomer2
     nomer2 = line2.split()[0] #слово в строке
    xx += 1
 else: z3()
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
 Z()

def z4():
 os.system(ff)
 File1 = 'names.txt'
 File2 = 'numbers.txt'
 z3z4_2(File1, File2)
 z1_2()
 print(f'''
[&] Редактирование:
[0] Назад''')
 with open('nanu.txt') as f3:
  for n, line in enumerate(f3, 1):
   kk = '[&] Список:\n[0] Назад'
   line1 = line.rstrip('\n')
   print(f'[{n}] {line1}')
 FindThis1 = nomer1
 FindThis2 = nomer2
 new1 = input('Введите новое имя: ')
 new2 = input('Введите новый номер: ')
 result12 = z4_3(File1, File2, FindThis1, FindThis2, new1, new2)

Z()
