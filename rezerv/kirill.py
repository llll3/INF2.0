def jjj():
 n1 = float(input('Первое число: '))
 n2 = float(input('Второе число: '))
 z = input('Введите значение: ')
 r = 'Результат: '
 o = 'Ошибка: неверное значение: '

 if z == '+':
  print(r + str(n1 + n2))
 elif z == '-':
  print(r + str(n1 - n2))
 elif z == '*':
  print(r + str(n1 * n2))
 elif z == '/':
  print(r + str(n1 / n2))
 else:
  print(o)
  jjj()
jjj()
