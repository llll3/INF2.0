import time, sys, os, subprocess, re
list = str(list(range(1, 30)))
def glav():
    print('''
1.spisok
2.add
3.delete
4.zamenit''')
    asa = input('aaaa: ')
    if asa == '1':
        listt()
        glav()
    elif asa == '2':
        add1()
    elif asa == '3':
        delete1()
    elif asa == '4':
        Zamen()

def listt():
 nanu()
 with open('nanu.txt', 'r') as f3:
  for n, line in enumerate(f3, 1):
   line1 = line.rstrip('\n')
   print(f'[{n}] {line1}')
def nanu():
   with open('name.txt', 'r') as f1, open('numbers.txt', 'r') as f2, open('nanu.txt', 'w') as f3:
       for i, j in zip(f1.readlines(), f2.readlines()):
           f3.write(f'{i.strip()}: {j}')
def delete1():
 listt()
 stroka1()
 stroka2()
 gg = jj
 if gg in list:
  with open('name.txt') as f1:
      lines1 = f1.readlines()

  str1 = nomer1
  pattern1 = re.compile(re.escape(str1))
  with open('name.txt', 'r+') as f1:
    for line in lines1:
        result1 = pattern1.search(line)
        if result1 is None:
            f1.write(line)
            delete2()
def delete2():
  with open('numbers.txt') as f2:
      lines2 = f2.readlines()

  str2 = nomer2
  pattern2 = re.compile(re.escape(str2))
  with  open('numbers.txt', 'r+') as f2:
    for line in lines2:
        result2 = pattern2.search(line)
        if result2 is None:
            f2.write(line)
            print(f'Удaленно: {nomer1}')
            print(f'Удаленно: {nomer2}')
            glav()

def stroka1():
 with open("name.txt", "r") as ff1:
  global jj
  jj = input('Строка: ')
  h = int(jj)
  h -= 1
  x = 0
  for line1 in ff1:
   if x == h: #строка
    global nomer1
    nomer1 = line1.split()[0] #слово в строке
    print(nomer1)
   x += 1

def stroka2():
 with open("numbers.txt", "r") as ff2:
  h = int(jj)
  h -= 1
  x = 0
  for line2 in ff2:
   if x == h: #строка
    global nomer2
    nomer2 = line2.split()[0] #слово в строке
    print(nomer2)
   x += 1
def add1():
        with open('numbers.txt','a') as f,  open('name.txt', 'a') as f1:
            xx = input('Введите имя: ')
            f1.write(f'\n{xx}')
            xxx = input('Введите номер: ')
            f.write(f'\n{xxx}')
            print(f'Добавлено имя: {xx}')
            print(f'Добавлен номер: {xxx}')

def Delete(File1, File2):
  listt()
  jek = input('Строка: ')
  if jek in list:
    with open(File1, 'r') as fff1, open(File2, 'r') as fff2:
      h = int(jek) ; h -= 1 ; h = h ; x = 0
      for line1 in fff1:
        for line2 in fff2:
          if x == h: #строка
            global nomer1 ; global nomer2
            nomer1 = line1.split()[0] ; nomer2 = line2.split()[0] #слово в строке
          x += 1

def Delete2(File1, File2, FindThis1, FindThis2):
        TemporaryFile1 = File1 + '.tmp' ; TemporaryFile2 = File2 + '.tmp'   # создаём файл
        os.system("touch %s" % TemporaryFile1) ; os.system("touch %s" % TemporaryFile2)    # временный файл
        with open(File1, 'r') as f1, open(TemporaryFile1, 'w') as f2, open(File2, 'r') as ff1, open(TemporaryFile2, 'w') as ff2:
            lines1 = f1.readlines() ; lines2 = ff1.readlines()
            for line1 in lines1:
                line1 = line1.strip()
                if line1 == FindThis1:
                    f2.write('') # меняем строку
                else:
                    f2.write(line1 + '\n') # оставляем прежнюю

            for line2 in lines2:
                line2 = line2.strip()
                if line2 == FindThis2:
                    ff2.write('') # меняем строку
                else:
                    ff2.write(line2 + '\n') # оставляем прежнюю

        path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), File1) ; path2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), File2)
        os.remove(path1) ; os.remove(path2) # удаляем основной файл
        os.system("mv %s %s" % (TemporaryFile1, File1)) ; os.system("mv %s %s" % (TemporaryFile2, File2)) # переименовываем временный файл

def Zamen():
  File1 = 'name.txt'
  File2 = 'numbers.txt'
  Delete(File1, File2)
  FindThis1 = nomer1
  FindThis2 = nomer2
  result = Delete2(File1, File2, FindThis1, FindThis2)

while list:
    glav()
glav()
