import time, sys, os, subprocess
list = str(list(range(1, 50)))

def listt():
 nanu()
 with open('nanu.txt', 'r') as f3:
  for n, line in enumerate(f3, 0):
    line1 = line.rstrip('\n')
    print(f'[{n}] {line1}')

def nanu():
   with open('name.txt', 'r') as f1, open('numbers.txt', 'r') as f2, open('nanu.txt', 'w') as f3:
       for i, j in zip(f1.readlines(), f2.readlines()):
             f3.write(f'{i.strip()}: {j}')
def Add():
        File1 = 'name.txt'
        File2 = 'numbers.txt'
        with open(File1, 'a') as f1, open(File2, 'a') as ff1:
                xx = input('Введите имя: ')
                f1.write(f'\n{xx}')
                xxx = input('Введите номер: ')
                ff1.write(f'\n{xxx}')
                print(f'Добавлено имя: {xx}')
                print(f'Добавлен номер: {xxx}')

Add()
listt()
