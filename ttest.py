import time, sys, os, subprocess, re
zel = '\033[32m'
kras = '\033[31m'
jir = '\033[1m'
kon = '\033[m'
fio = '\033[35m'
kjir = kon + jir
list2 = str(list(range(1, 5)))
ff = "('clear')"

def Z():
 os.system(ff)
 print(f'''{jir}[&] ?
[0] Выход
[1] список
[2] добавить
[3] удалить
[4] редактировать{kjir}''')
 global asa
 asa = input('--> ')
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
 z1_2()
 x = 0
 if asa == '1':
  os.system(ff)
  print('[&] Список: \n[0] Назад')
 if asa == '3':
  print('[&] Удалить: ')
 if asa == '4':
  print('[&] Изменить')

 with open('nanu.txt') as f3:
  Num = len(f3.readlines())
  Num += 1
  global list1
  list1 = list(range(1, Num))
 with open('nanu.txt') as f3:
  for n, line in enumerate(f3, 1):
   kk = '[&] Список:\n[0] Назад'
   line1 = line.strip(' \n: ')
   print(f'[{n}] {line1}')
 if asa == '1':
  cc = input('--> ')
  if cc == '0':
   Z()
  else:
   os.system(ff)
   print(f'{kras + jir}Неверный ввод!{kon}')
   time.sleep(1)
   z1()

def z1_2():
 File1 = 'names.txt'
 File2 = 'numbers.txt'
 File3 = 'nanu.txt'

 TemporaryFile3 = File3 + '.tmpp' # создаём файл
 os.system("touch %s" % TemporaryFile3) # временный файл

 with open(File1, 'r') as f1, open(File2, 'r') as f2, open(TemporaryFile3, 'w') as f4:
  os.system("mv %s %s" % (File1, 'names.tmp')) ; os.system("mv %s %s" % (File2, 'numbers.tmp')) # переименовываем временный файл
  os.system("mv %s %s" % ('names.tmp', File1)) ; os.system("mv %s %s" % ('numbers.tmp', File2)) # пер
  for i, j in zip(f1.readlines(), f2.readlines()):
#   for line1 in f1:
 #   jj = line1.rstrip('\n:')
  #  global i1
   # i1 = jj
#    for line2 in f2:
 #    jj2 = line2.rstrip('\n:')
  #   global j1
   #  j1 = jj2

   f4.write(f'{i.strip()}: {j}')

 path3 = os.path.join(os.path.abspath(os.path.dirname(__file__)), File3)
 os.remove(path3) # удаляем основной файл
 os.system("mv %s %s" % (TemporaryFile3, File3))

def z3():
 os.system(ff)
 File1 = 'names.txt'
 File2 = 'numbers.txt'
 print('[&] Удалить\n[0] Назад\n[1] Продолжить')
 tt = input('--> ')
 if tt == '0':
  Z()
 if tt == '1':
  z3z4_2(File1, File2)
  hh = int(jek)
  hh -= 1
  if hh in list1:
   with open(File1, "r") as f1, open(File2, "r") as ff1, open("tmp1.txt", "w") as f2, open("tmp2.txt", "w") as ff2:
    for line1 in f1:
     if line1.strip("\n") != nomer1:
      f2.write(line1)

    for line2 in ff1:
     if line2.strip("\n") != nomer2:
      ff2.write(line2)

    os.system(ff)
    print(f'{zel + jir}Удаленно имя: {nomer1}\b\nУдален номер: {nomer2}{kon}')
    time.sleep(2)
#    os.system("mv %s %s" % (File1, 'names.tmpp')) ; os.system("mv %s %s" % (File2, 'numbers.tmpp')) # переименовываем временный файл
    os.system("mv %s %s" % ('tmp1.txt', File1)) ; os.system("mv %s %s" % ('tmp2.txt', File2)) # пере
    z3()
  else:
   os.system(ff)
   print(f'{kras + jir}Неверный ввод!{kon}')
   time.sleep(1)
   z3()
# with open(File1) as f1, open(File2) as ff1:
#   os.rename("File1", "names.txt.mmm") ; os.rename("File2", "numbers.txt.mmm")
 #  os.rename("names.txt.mmm", "File1") ; os.rename("numbers.txt.mmm", "File2")
def z2():
 os.system(ff)
 print('[&] Добавить\n[0] Назад\n[1] Продолжить')
 File1 = 'names.txt'
 File2 = 'numbers.txt'
 xx = input('--> ')
 if xx == '0': Z()
 if xx == '1':
  File1 = 'names.txt'
  File2 = 'numbers.txt'
  File3 = 'nanu.txt'
  os.system(ff)
  with open(File1,'a') as f1,  open(File2, 'a') as ff1:
   xx = input('Введите имя: ')
   f1.write(f'\n{xx}')
   xxx = input('Введите номер: ')
   ff1.write(f'\n{xxx}')
   os.system(ff)
   print(f'{ jir + zel}Добавлено имя: {xx}{kjir}')
   print(f'{zel}Добавлен номер: {xxx}{kon}')
   time.sleep(4)
 else:
  os.system(ff)
  print(f'{kras + jir}Неверный ввод!{kon}')
  time.sleep(1)
  z2()
 z2()

def z3z4_2(File1, File2):
 os.system(ff)
 z1()
 global jek
 jek = input('Введите поряд.номер: ')
 if int(jek) in list1:
  with open(File1) as fff1, open(File2) as fff2:
   h = int(jek)
   h -= 1
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
 else:
  os.system(ff)
  print(f'{kras + jir}Неверный ввод!{kon}')
  time.sleep(1)
  z3z4_2(File1, File2)

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
 os.system(ff)
 print(f'{zel + jir}Изменено имя: {FindThis1} на {new1}\nИзменён номер: {FindThis2} на {new2}{kon}')
 time.sleep(4)
 z4()

def z4():
 os.system(ff)
 print('[&] Изменить\n[0] Назад\n[1] Продолжить')
 kl = input('--> ')
 if kl == '0':
  Z()
 if kl == '1':
  os.system(ff)
  File1 = 'names.txt'
  File2 = 'numbers.txt'
  z3z4_2(File1, File2)
  FindThis1 = nomer1
  FindThis2 = nomer2
  os.system(ff)
  new1 = '\n' #input('Введите новое имя: ')
  new2 = '\n' #input('Введите новый номер: ')
  result12 = z4_3(File1, File2, FindThis1, FindThis2, new1, new2)
 else:
  os.system(ff)
  print(f'{kras + jir}Неверный ввод!{kon}')
  time.sleep(1)
  z4()

Z()

