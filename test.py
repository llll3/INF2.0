import time, sys, os, subprocess
hio = True
list = str(list(range(1, 10)))
f = "open('numbers.txt','r')"
def glav():
    print('''
1.spisok
2.add
3.delete
4.zamenit''')
    asa = input('aaaa: ')
    if asa == '1':
        spi()
    elif asa == '2':
        add1()
    elif asa == '3':
        delet()
    elif asa == '4':
        Line()

def add1():
        with open('numbers.txt','r') as f,  open('name.txt', 'r') as f1:
            for n, line in enumerate(f1, 1):
                line = line.rstrip('\n')
                print(f'[{n}]: {line}')
        jjj()
def jjj():
      with open('numbers.txt','r+') as f,  open('name.txt', 'r+') as f1:
           s = input('Цисло')
           sa = input('Введите новое имя')
           saa = input ('Введите новый номер')
           hh = sa
           h = int(s)
           h -= 1
           x = 0
           for line in f1:
               if x == h: #строка
                  nomer = line.split()[0] #слово в строке
               else:
                  glav()
           x += 1
def spi():
    with open('numbers.txt','r') as ff1, open('name.txt', 'r') as ff2:
        for n, line in enumerate(ff2, 1):
            line = line.rstrip('\n')
            print(f'[{n}]: {line}')

def spi1():
    with open('numbers.txt','r') as ff1, open('name.txt', 'r') as ff2:
        for n, line in enumerate(ff2, 1):
            line = line.rstrip('\n')
            print(f'[{n}]: {line}')
        global jek
        jek = input('Строка: ')
        if jek in list:
           holm1()
def holm1():
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
    with open('numbers.txt','r') as ff1, open('name.txt', 'r') as ff2:
        for n, line in enumerate(ff1, 1):
            line = line.rstrip('\n')
            print(f'[{n}]: {line}')
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
  spi1()
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



if hio == True:
    glav()
