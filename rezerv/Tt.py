import time
import sys
import os
numbers = str(list(range(1, 10)))
list2 = str(list(range(1, 5)))
ff = "('clear')"
zel = '\033[32m\033[1m'
kras = '\033[31m\033[1m'
jir = '\033[1m\033[1m'
kon = '\033[m\033[1m'
fio = '\033[35m\033[1m'
kjir = kon + jir


def start():
    F1 = 'names.txt'
    F2 = 'numbers.txt'
    os.system(ff)
    print(f'''
{kras}══════════════════════╗{kon}
[&] Версия {fio}inf{kon} [2.0]  {kras}║{kon}
{kras}══════════════════════╣{kon}
{zel}[0]{kon} Выход             {kras}║{kon}
{zel}[1]{kon} Обновить          {kras}║{kon}
{zel}[2]{kon} Установить        {kras}║{kon}
{zel}[3]{kon} Ручной запуск     {kras}║{kon}
{zel}[4]{kon} Запуск по списку  {kras}║{kon}
{zel}[5]{kon} Редактор списка   {kras}║{kon}
{kras}══════════════════════╝{kon}''')
    global command
    command = input(f'{jir}--> {kon}')
    if command == '1':
        return update()
    elif command == '2':
        return install()
    elif command == '3':
        return zapusk()
    elif command == '4':
        return Z(F1, F2)
    elif command == '5':
        return 
    elif command == '0':
        print(f'{kras}Выход из inf...{kon}')
        time.sleep(1)
        sys.exit()
    else:
        os.system(ff)
        return start()


def update():
    os.system(ff)
    print(f'{zel}Обновление inf...{kon}')
    time.sleep(2)
    os.system('cd ~ ; pkg install git python3 nano')
    os.system('git clone https://github.com/llll3/inf2.0')
    os.system('cd inf2.0 ; cp bash.bashrc ../../usr/etc/')
    os.system('source ../../usr/etc/bash.bashrc')
    os.system('cd inf ; chmod 777 inf ; cd ~ ; yes | pkg update')
    os.system('yes | pkg upgrade')
    os.system(ff)
    print(f'{zel}Обновление завершенно!{kon}')
    time.sleep(2)
    return start()


def install():
    os.system(ff)
    print(f'{zel}Установка inf...{kon}')
    time.sleep(2)
    os.system('cd ~ ; pkg install git python3 nano')
    os.system('git clone https://github.com/llll3/inf2.0')
    os.system('cd inf2.0 ; cp bash.bashrc ../../usr/etc/')
    os.system('source ../../usr/etc/bash.bashrc ; cd inf ; chmod 777 inf')
    os.system('cd ~ ; yes | pkg update ; yes | pkg upgrade')
    os.system(ff)
    print(f'{zel}Установка завершенна!{kon}')
    time.sleep(1)
    return start()


def zapusk():
    os.system(ff)
    print(f'{zel}Запуск inf...{kon}')
    time.sleep(1)
    os.system('cd ~ ; cd inf2.0 ; cd inf ; ./inf')
    return exit1()


def spzapusk(F1, F2):
    os.system(ff)
    z3z4_2(F1, F2)
    number = nomer2
    return sms(F1, F2, number)


def sms(F1, F2, number):
    os.system(ff)
    print(f'''
{kras}══════════════════════╗{kon}
[&]Выбирите режим:    {kras}║{kon}
{kras}══════════════════════╣{kon}
{zel}[0]{kon} Назад             {kras}║{kon}
{zel}[1]{kon} Флуд SMS          {kras}║{kon}
{zel}[2]{kon} Флуд CALL         {kras}║{kon}
{zel}[3]{kon} CALL и SMS        {kras}║{kon}
{zel}[4]{kon} F.A.Q             {kras}║{kon}
{kras}══════════════════════╝{kon}''')
    b = input(f'{jir}--> {kon}')
    list3 = str(list(range(1, 4)))
    if b == '0':
        spzapusk()
    with open('names.txt'):
        if b in list3:
            os.system(f'cd ~/inf2.0/inf ; ./inf {number} {b} 1 0')
            return exit1()
    if b == '4':
        return faq(F1, F2, number)
    else:
        os.system(ff)
        print(f'{kras}Неверный ввод{kon}')
        time.sleep(1)
        return sms(F1, F2, number)


def faq(F1, F2, number):
    os.system(ff)
    print(f'''
{kras}═══════════════════════════════════════════════╗{kon}
[&] F.A.Q:                                     {kras}║{kon}
{kras}═══════════════════════════════════════════════╣{kon}
{zel}[0]{kon} Назад.                                     {kras}║{kon}
{kras}[1]{kon} SMS - начинает флудить смс'ками.           {kras}║{kon}
{kras}[2]{kon} CALL - начинает флудить звон'ками.         {kras}║{kon}
{kras}[3]{kon} SMS и CALL - включает в себя 1 и 2 пункт.  {kras}║{kon}
{kras}═══════════════════════════════════════════════╝{kon}''')
    ww = input(f'{jir}--> {kon}')
    if ww == '0':
        return sms(F1, F2, number)
    else:
        os.system(ff)
        print(f'{kras}Неверный ввод{kon}')
        time.sleep(1)
        return faq(F1, F2, number)


def exit1():
    os.system(ff)
    ee = input(
        f'{jir}Выйти из {fio}inf{kon}?({zel}y{kon}{jir}/{kras}n{kon}): ')
    if ee == 'y' or ee == 'yes':
        return sys.exit()
    elif ee == 'n' or ee == 'no':
        return start()
    else:
        return exit1()
#################################################################


def Z(F1, F2):
    error1 = '12345678910111213141516'
    error2 = '12345678910111213141516'
    os.system(ff)
    print(f'''
{kras}══════════════════════╗{kjir}
[&] Редактор списка:  {kras}║{kjir}
{kras}══════════════════════╣{kjir}
{zel}[0]{kon} Назад             {kras}║{kjir}
{zel}[1]{kon} Список            {kras}║{kjir}
{zel}[2]{kon} Добавить          {kras}║{kjir}
{zel}[3]{kon} Удалить           {kras}║{kjir}
{zel}[4]{kon} Изменить          {kras}║{kjir}
{kras}══════════════════════╝{kon}''')
    global abba
    abba = input(f'{jir}--> {kon}')
    if abba == '0':
        return start()
    if abba == '1':
        return spzapusk(F1, F2)
    elif abba == '2':
        return z2(F1, F2, error1, error2)
    elif abba == '3':
        return z3()
    elif abba == '4':
        return z4(F1, F2, error1, error2)
    elif abba != list2:
        return Z(F1, F2)
    else:
        os.system(ff)
        print(f'{kras}Неверный ввод{kon}')
        time.sleep(1)


def z1(abba, F1, F2):
    abba = 0
    key = 0
    z1_2()
    z1_3()
    if command == '4':
        key = zel
        os.system(ff)
        print(f'''
{kras}══════════════════════════════╗{kjir}
[&] Список:                   {kras}║{kjir}
{kras}══════════════════════════════╣{kjir}
{zel}[0]{kon + jir} Назад                     {kras}║{kjir}''')
    if abba == '1':
        key = kras
        os.system(ff)
        print(f'''
{kras}══════════════════════════════╗{kjir}
[&] Список:                   {kras}║{kjir}
{kras}══════════════════════════════╣{kjir}
{zel}[0]{kon + jir} Назад                     {kras}║{kjir}''')
    if abba == '3':
        print(f'''
{kras}══════════════════════════════╗{kjir}
[&] Удалить:                  {kras}║{kjir}
{kras}══════════════════════════════╣{kjir}''')
        key = zel
    if abba == '4':
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
            print(f'{key}{jir}[{n}]{kjir} {line1}')
        print(f'{kras}══════════════════════════════╝{kon}')
# if command == '4':
#  if jek == '0':
#   return start()
#  else:
#   os.system(ff)
#   print(f'{kras + jir}Неверный ввод!{kon}')
#   time.sleep(1)
#   return spzapusk()
    if abba == '1':
        cc = input(f'{jir}--> {kon}')
        if cc == '0':
            return Z(F1, F2)
        else:
            os.system(ff)
            print(f'{kras + jir}Неверный ввод!{kon}')
            time.sleep(1)
            return z1(F1, F2)


def z1_2():
    with open('names.txt') as f1, open("numbers.txt") as ff1:
        with open('nnames.txt', 'w') as f2, open("nnumbers.txt", "w") as ff2:
            for line1 in f1:
                if line1.strip():
                    f2.write(line1)
            for line2 in ff1:
                if line2.strip():
                    ff2.write(line2)
    os.rename("nnames.txt", "names.txt")
    os.rename("nnumbers.txt", "numbers.txt")


def z1_3():
    F1 = 'names.txt'
    F2 = 'numbers.txt'
    F3 = 'nanu.txt'

    TF3 = F3 + '.tmpp'  # создаём файл
    os.system("touch %s" % TF3)  # временный файл

    with open(F1) as f1, open(F2) as f2, open(TF3, 'w') as f4:
        os.system("mv %s %s" % (F1, 'names.tmp'))
        # переименовываем временный файл
        os.system("mv %s %s" % (F2, 'numbers.tmp'))
        os.system("mv %s %s" % ('names.tmp', F1))
        os.system("mv %s %s" % ('numbers.tmp', F2))  # пер
        for i, j in zip(f1.readlines(), f2.readlines()):
            f4.write(f'{i.strip()}: {j}')

    path3 = os.path.join(os.path.abspath(os.path.dirname(__file__)), F3)
    os.remove(path3)  # удаляем основной файл
    os.system("mv %s %s" % (TF3, F3))


def z3(F1, F2):
    os.system(ff)
    print(f'''
{kras}════════════════╗{kjir}
[&] Удалить:    {kras}║{kjir}
{kras}════════════════╣{kjir}
[0] Назад       {kras}║{kjir}
[1] Продолжить  {kras}║{kjir}
{kras}════════════════╝{kon}''')
    tt = input(f'{jir}--> {kon}')
    if tt == '0':
        Z(F1, F2)
    if tt == '1':
        z3_3(F1, F2)
        os.system(ff)
        print(f'{zel}Удаленно имя: {nomer11}{kon}')
        print(f'{zel}Удален номер: {nomer22}{kon}')
        time.sleep(2)
        z3()
    if tt not in list1:
        with open("names.txt"), open("numbers.txt"):
            del nomer1
            del nomer2
    else:
        os.system(ff)
        print(f'{kras + jir}Неверный ввод!{kon}')
        time.sleep(1)
        z3(F1, F2)


def z3_3(F1, F2):
    F1 = "names.txt"
    F2 = "numbers.txt"
    z3z4_2(F1, F2)
    global nomer11
    nomer11 = nomer1
    global nomer22
    nomer22 = nomer2
    hh = int(jek)
    hh -= 1
    if hh in list1:
        with open(F1) as f1, open(F2) as ff1:
            data1 = f1.readlines()
            data2 = ff1.readlines()
            data1 = filter(lambda line: f"{nomer1}" not in line, data1)
            data2 = filter(lambda line: f"{nomer2}" not in line, data2)
        with open(F1, "w") as f1, open(F2, "w") as ff1:
            f1.write("".join(data1))
            ff1.write("".join(data2))


def z2(F1, F2, error1, error2):
    os.system(ff)
    print(f'''
{kras}════════════════╗{kjir}
[&] Добавить:   {kras}║{kjir}
{kras}════════════════╣{kjir}
[0] Назад       {kras}║{kjir}
[1] Продолжить  {kras}║{kjir}
{kras}════════════════╝{kon}''')
    F3 = 'nanu.txt'
    xx = input(f'{jir}--> {kon}')
    if xx == '0':
        Z(F1, F1)
    if xx == '1':
        z2_22(F1, F2, F3, error1, error2)
    else:
        os.system(ff)
        print(f'{kras + jir}Неверный ввод!{kon}')
        time.sleep(1)
        z2(F1, F2, error1, error2)


def z2_22(F1, F2, F3, error1, error2):
    os.system(ff)
    if error1[0] == 'О':
        print(f'{kras+jir}{error1}')
    if error2[0] == 'О':
        print(f'{kras+jir}{error2}')
    with open(F1, 'a') as f1, open(F2, 'a') as ff1:
        xx = input('Введите имя: ')
        if len(xx) <= 12:
            f1.write(f'\n{xx}')
            xxx = input('Введите номер: ')
            if len(xxx) == 11 and xxx[0] == '7':
                ff1.write(f'\n{xxx}')
                os.system(ff)
                print(f'{ jir + zel}Добавлено имя: {xx}{kjir}')
                print(f'{zel}Добавлен номер: {xxx}{kon}')
                time.sleep(3)
                error1 = '12345678910111213141516'
                error2 = '12345678910111213141516'
            else:
                error2 = f'''Ошибка: номер должен начинаться с 7(без +),
                 а также должен состоять из 11 цифр.{kon}'''
        else:
            error1 = f'Ошибка: имя не должно превышать 12 символов.{kon}'
    z2(F1, F2, error1, error2)


def z3z4_2(F1, F2):
    os.system(ff)
    z1(abba, F1, F2)
    try:
        global jek
        jek = int(input(f'{jir}Введите поряд.номер: {kon}'))
    except ValueError:
        os.system(ff)
        print(f'{kras}Вводить только цифры!{kon}')
        time.sleep(1)
        return z3z4_2(F1, F2)
    aa = type(jek)
    aa1 = type(list1)
    print(aa, aa1)
    time.sleep(2)
    if int(jek) in list1:
        with open(F1) as fff1, open(F2) as fff2:
            h = int(jek)
            h -= 1
            x = 0
            xx = 0
            for line1 in fff1:
                if x == h:  # строка
                    global nomer1
                    nomer1 = line1.split()[0]
                x += 1
            for line2 in fff2:
                if xx == h:  # строка
                    global nomer2
                    nomer2 = line2.split()[0]  # слово в строке
                xx += 1
    if jek == 0:
        return start()
    else:
        os.system(ff)
        print(f'{kras + jir}Неверный ввод!{kon}')
        time.sleep(1)
        z3z4_2(F1, F2)


def z4_3(F1, F2, FT1, FT2, new1, new2, error1, error2):
    TF1 = F1 + '.tmp'
    TF2 = F2 + '.tmp'   # создаём файл
    os.system("touch %s" % TF1)
    os.system("touch %s" % TF2)    # временный файл

    with open(F1) as f1:
        with open(TF1, 'w') as f2, open(F2) as ff1, open(TF2, 'w') as ff2:
            lines1 = f1.readlines()
            lines2 = ff1.readlines()
            for line1 in lines1:
                line1 = line1.strip()
            if line1 == FT1:
                f2.write(f'{new1}')  # меняем строку
            else:
                f2.write(line1 + '\n')  # оставляем прежнюю
            for line2 in lines2:
                line2 = line2.strip()
            if line2 == FT2:
                ff2.write(f'{new2}')  # меняем строку
            else:
                ff2.write(line2 + '\n')  # оставляем прежнюю

    path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), F1)
    path2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), F2)
    os.remove(path1)
    os.remove(path2)  # удаляем основной файл
    os.system("mv %s %s" % (TF1, F1))
    # переименовываем временный файл
    os.system("mv %s %s" % (TF2, F2))
    os.system(ff)
    print(f'{zel}Изменено имя: {FT1} на {new1}{kon}')
    print(f'{zel}Изменён номер: {FT2} на {new2}{kon}')
    time.sleep(4)
    z4(F1, F2, error1, error2)


def z4(F1, F2, error1, error2):
    os.system(ff)
    print(f'''
{kras}════════════════╗{kjir}
[&] Изменить:   {kras}║{kjir}
{kras}════════════════╣{kjir}
[0] Назад       {kras}║{kjir}
[1] Продолжить  {kras}║{kjir}
{kras}════════════════╝{kon}''')
    kl = input('--> ')
    if kl == '0':
        Z(F1, F2)
    if kl == '1':
        os.system(ff)
        z3z4_2(F1, F2)
        FT1 = nomer1
        FT2 = nomer2
        z4_22(F1, F2, FT1, FT2, error1, error2)
    else:
        os.system(ff)
        print(f'{kras + jir}Неверный ввод!{kon}')
        time.sleep(1)
#  error1 = '12345678910111213141516'
#  error2 = '12345678910111213141516'
        z4(F1, F2, error1, error2)


def z4_22(F1, F2, FT1, FT2, error1, error2):
    os.system(ff)
    if error1[0] == 'О':
        print(f'{kras+jir}{error1}')
    if error2[0] == 'О':
        print(f'{kras+jir}{error2}')
    new1 = input('Введите новое имя: ')
    if len(new1) <= 12:
        new2 = input('Введите новый номер: ')
        if len(new2) == 11 and new2[0] == '7':
            error1 = '12345678910111213141516'
            error2 = '12345678910111213141516'
            z4_3(
                F1,
                F2,
                FT1,
                FT2,
                new1,
                new2,
                error1,
                error2)
        else:
            error2 = f'''{zel}Ошибка: номер должен начинаться с 7(без +),
             а также должен состоять из 11 цифр.{kon}'''
    else:
        error1 = f'Ошибка: имя не должно превышать 12 символов.{kon}'
    z4_22(F1, F2, error1, error2)


start()
