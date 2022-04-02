import time, sys, os, subprocess
list = str(list(range(1, 10)))
y = 0
def spi1():
    with open('numbers.txt','r') as ff1, open('name.txt', 'r') as ff2:
        for line, in enumerate(ff2, 1)
               line = line.rstrip('\n')
               linee = linee.strip('\n')
               print(f'[{n}]: {line} {linee}')
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
def holm2():
   ff2 =  open("numbers.txt", "r")
   h = int(jek)
   h -= 1
   x = 0
   for line in ff2:
      if x == h: #строка
           global nomer2
           nomer2 = line.split()[0] #слово в строке
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
spi1()
ff22 = 'numbers.txt'
ff11 = 'name.txt'
File = ff11
FindThis1 = nomer1 #input("Старое имя: ")
ReplaceByThis = input("Новое имя: ")
result = Line1(File, FindThis1, ReplaceByThis)
holm2()
File = ff22
FindThis2 = nomer2 #input("Старый номер: ")
ReplaceByThis = input("Новый номер ")
result = Line2(File, FindThis2, ReplaceByThis)

