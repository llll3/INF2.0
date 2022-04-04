import time, sys, os, subprocess
list = str(list(range(1, 50)))

def listt():
 nanu()
 with open('nanu.txt', 'r') as f3:
  for n, line in enumerate(f3, 1):
   line1 = line.rstrip('\n') ; print(f'[{n}] {line1}')
def nanu():
   with open('name.txt', 'r') as f1, open('numbers.txt', 'r') as f2, open('nanu.txt', 'w') as f3:
       for i, j in zip(f1.readlines(), f2.readlines()):
           f3.write(f'{i.strip()}: {j}')




def Delete(File1, File2):
  listt()
  jek = input('Строка: ')
  if jek in list:
    with open(File1, 'r') as fff1, open(File2, 'r') as fff2:
      h = int(jek) ; h -= 1 ; h = h ; x = 0 ; xx = 0
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

def Delete2(File1, File2, FindThis1, FindThis2, new1, new2):
        TemporaryFile1 = File1 + '.tmp' ; TemporaryFile2 = File2 + '.tmp'   # создаём файл
        os.system("touch %s" % TemporaryFile1) ; os.system("touch %s" % TemporaryFile2)    # временный файл
        with open(File1, 'r') as f1, open(TemporaryFile1, 'w') as f2, open(File2, 'r') as ff1, open(TemporaryFile2, 'w') as ff2:
            lines1 = f1.readlines()
            lines2 = ff1.readlines()
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

File1 = 'name.txt'
File2 = 'numbers.txt'

Delete(File1, File2)

FindThis1 = nomer1
FindThis2 = nomer2

new1 = input('Введите новое имя: ')
new2 = input('Введите новый номер: ')

result = Delete2(File1, File2, FindThis1, FindThis2, new1, new2)

listt()
