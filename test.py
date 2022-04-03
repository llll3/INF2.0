import time, sys, os, subprocess, re
hio = True
list = str(list(range(1, 20)))
f = "open('numbers.txt','r')"
def glav():
    print('''
1.spisok
2.add
3.delete
4.zamenit''')
    asa = input('aaaa: ')
    if asa == '1':
        listt()
    elif asa == '2':
        add1()
    elif asa == '3':
        delete1()
    elif asa == '4':
        Line()

def listt():
 nanu()
 with open('nanu.txt', 'r') as f3:
  for n, line in enumerate(f3, 1):
   line = line.rstrip('\n')
   print(f'[{n}] {line}')

def nanu():
   with open('name.txt', 'r') as f1, open('numbers.txt', 'r') as f2, open('nanu.txt', 'w') as f3:
       for i, j in zip(f1.readlines(), f2.readlines()):
           f3.write(f'{i.strip()}: {j}')
def delete1():
 listt()
 stroka1()
 gg = jj
 if gg in list:
  with open('name.txt') as f1:
      lines1 = f1.readlines()

  str1 = nomer1
  pattern1 = re.compile(re.escape(str1))
  with open('name.txt', 'w') as f1:
    for line in lines1:
        result1 = pattern1.search(line)
        if result1 is None:
            f1.write(line)
            delete2()
def delete2():
  with  open ('numbers.txt') as f2:
      lines2 = f2.readlines()

  str2 = nomer2
  pattern2 = re.compile(re.escape(str2))
  with  open('numbers.txt', 'w') as f2:
    for line in lines2:
        result2 = pattern2.search(line)
        if result2 is None:
            f2.write(line)

def stroka1():
  ff1 = open("name.txt", "r")
  global jj
  jj = input('Строка: ')
  h = int(jj)
  h -= 1
  x = 0
  for line in ff1:
   if x == h: #строка
    global nomer1
    nomer1 = line.split()[0] #слово в строке
    print(nomer1)
    stroka2()
   x += 1
def stroka2():
  ff2 = open("numbers.txt", "r")
  h = int(jj)
  h -= 1
  x = 0
  for line in ff2:
   if x == h: #строка
    global nomer2
    nomer2 = line.split()[0] #слово в строке
    print(nomer2)
   x += 1
def add1():
        with open('numbers.txt','a') as f,  open('name.txt', 'a') as f1:
            xx = input('Введите имя: ')
            f1.write(f'{xx}')
            xxx = input('Введите номер: ')
            f.write(f'{xxx}')

def spi1():
 global jek
 jek = input('Строка: ')
 if jek in list:
  holm1()

def holm1():
 listt()
 jek = input('Строка: ')
 if jek in list:
  ff1 =  open("name.txt", "r")
  h = int(jek)
  h -= 1
  x = 0
  for line in ff1:
   if x == h: #строка
    global nomer1
    nomer1 = line.split()[0] #слово в строке
   x += 1

def spi2():
        nanu()
        global jek
        jek = input('Строка: ')
        if jek in list:
           holm2()
def holm2():
   ff2 =  open("numbers.txt", "r")
   h = int(jek)
   h -= 1
   x = 0
   for line in ff2:
      if x == h: #строка
           global nomer2
           nomer2 = (line.split()[0]) #слово в строке
      x += 1

def Line1(File, FindThis1, ReplaceByThis):
        TemporaryFile = File + '.tmp'            # создаём
        os.system("touch %s" % TemporaryFile)    # временный файл
        global result
        result = 0 # счетчик измененных строк

        with open(File, 'r') as f1, open(TemporaryFile, 'w') as f2:
            lines = f1.readlines()
            for line in lines:
                line = line.strip()
                if line == FindThis1:
                    f2.write(ReplaceByThis + '\n') # меняем строку
                    result = result + 1 # инкрементирование счетчика измененных строк
                else:
                    f2.write(line + '\n') # оставляем прежнюю

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), File)
        os.remove(path) # удаляем основной файл
        os.system("mv %s %s" % (TemporaryFile, File)) # переименовываем временный файл
def Line2(File, FindThis2, ReplaceByThis):
        TemporaryFile = File + '.tmp'            # создаём
        os.system("touch %s" % TemporaryFile)    # временный файл
        result = 0 # счетчик измененных строк
        with open(File, 'r') as f1, open(TemporaryFile, 'w') as f2:
            lines = f1.readlines()
            for line in lines:
                line = line.strip()
                if line == FindThis2:
                      f2.write(ReplaceByThis + '\n') # меняем строку
                      result = result + 1 # инкрементирование счетчика измененных строк
                else:
                    f2.write(line + '\n') # оставляем прежнюю

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), File)
        os.remove(path) # удаляем основной файл
        os.system("mv %s %s" % (TemporaryFile, File)) # переименовываем временный файл

def Line():
  holm1()
  ff22 = 'numbers.txt'
  ff11 = 'name.txt'
  File = ff11
  FindThis1 = nomer1 #input("Старое имя: ")
  ReplaceByThis = input("Новое имя: ")
  result = Line1(File, FindThis1, ReplaceByThis)
  spi2()
  File = ff22
  FindThis2 = nomer2 #input("Старый номер: ")
  ReplaceByThis = input("Новый номер ")
  result = Line2(File, FindThis2, ReplaceByThis)
  glav()

def Linee():
  spi1()
  ff22 = 'numbers.txt'
  ff11 = 'name.txt'
  File = ff11
  FindThis1 = nomer1 #input("Старое имя: ")
  ReplaceByThis = ''
  result = Line1(File, FindThis1, ReplaceByThis)
  spi2()
  File = ff22
  FindThis2 = nomer2 #input("Старый номер: ")
  ReplaceByThis = ''
  result = Line2(File, FindThis2, ReplaceByThis)
  glav()


if hio == True:
    glav()

