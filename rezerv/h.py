import time, sys, os, subprocess, re ; zel = '\033[32m' ; kras = '\033[31m' ; jir = '\033[1m' ; kon = '\033[m' ; fio = '\033[35m' ; 
kjir = kon + jir ; list2 = str(list(range(1, 5))) ; ff = "('clear')"
ff = 'clear'
list1 = list(range(1, 13))
File1 = "names.txt"
File2 = "numbers.txt"


def z1():
 asa = '0'
 key = '0'
 z1_2()
 z1_3()
 x = 0
 if asa == '1':
  key = kras
  os.system(ff)
  print(f'''
{kras}══════════════════════════════╗{kjir}
[&] Список:                   {kras}║{kjir}
{kras}══════════════════════════════╣{kjir}
{zel}[0]{kon + jir} Назад                     {kras}║{kjir}''')
 if asa == '3':
  print(f'''
{kras}══════════════════════════════╗{kjir}
[&] Удалить:                  {kras}║{kjir}
{kras}══════════════════════════════╣{kjir}''')
  key = zel
 if asa == '4':
  print(f'''
{kras}══════════════════════════════╗{kjir}
[&] Изменить:                 {kras}║{kjir}
{kras}══════════════════════════════╣{kjir}''')
  key = zel

 with open('nanu.txt') as f3:
  Num = len(f3.readlines())
  Num += 1
  global list1
  list1 = list(range(1, Num))
 with open('nanu.txt') as f3:
  for n, line in enumerate(f3, 1):
   line1 = line.strip('\n')
   print(f'{key + jir}[{n}]{kon + jir} {line1}')

 print(f'{kras}══════════════════════════════╝{kon}')
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
 with open('names.txt') as f1, open("numbers.txt") as ff1:
  with open('nnames.txt', 'w') as f2, open("nnumbers.txt", "w") as ff2:
   for line1 in f1:
    if line1.strip():
     f2.write(line1)
   for line2 in ff1:
    if line2.strip():
     ff2.write(line2)
 os.rename("nnames.txt", "names.txt") ; os.rename("nnumbers.txt", "numbers.txt")

def z1_3():
 File1 = 'names.txt'
 File2 = 'numbers.txt'
 File3 = 'nanu.txt'

 TemporaryFile3 = File3 + '.tmpp' # создаём файл
 os.system("touch %s" % TemporaryFile3) # временный файл

 with open(File1, 'r') as f1, open(File2, 'r') as f2, open(TemporaryFile3, 'w') as f4:
  os.system("mv %s %s" % (File1, 'names.tmp')) ; os.system("mv %s %s" % (File2, 'numbers.tmp')) # переименовываем временный файл
  os.system("mv %s %s" % ('names.tmp', File1)) ; os.system("mv %s %s" % ('numbers.tmp', File2)) # пер
  for i, j in zip(f1.readlines(), f2.readlines()):
   f4.write(f'{i.strip()}: {j}')

 path3 = os.path.join(os.path.abspath(os.path.dirname(__file__)), File3)
 os.remove(path3) # удаляем основной файл
 os.system("mv %s %s" % (TemporaryFile3, File3))
 
def z3z4_2(File1, File2):
   os.system(ff)
   z1()
   try:
     global jek
     jek = int(input(f'{jir}Введите поряд.номер: {kon}'))
   except ValueError:
     os.system(ff)
     print(f'{kras}Вводить только цифры!{kon}')
     time.sleep(1)
     return z3z4_2(File1, File2)
   aa = type(jek)
   aa1 = type(list1)
   print(aa, aa1)
   time.sleep(2)
   if  jek in  list1:
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
   if jek == 0:
     return start()
   else:
     File1 = "names.txt"
     File2 = "numbers.txt"
     os.system(ff)
     print(f'{kras + jir}Неверный ввод!{kon}')
     time.sleep(1)
     z3z4_2(File1, File2)

z3z4_2(File1, File2)
