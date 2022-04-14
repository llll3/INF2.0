import time
import sys
import os
numbers = str(list(range(1, 10)))
list2 = str(list(range(1, 6)))
ff = 'clear'
zel = '\033[32m\033[1m'
kras = '\033[31m\033[1m'
jir = '\033[1m\033[1m'
kon = '\033[m\033[1m'
fio = '\033[35m\033[1m'
jel = '\033[33m\033[1m'
kjir = kon + jir


def start():
    os.system(ff)
    pwd = 'nanu/'
    F1 = f'{pwd}names.txt'
    F2 = f'{pwd}numbers.txt'
    F3 = f'{pwd}nanu.txt'
    bmb = 'bmb/inf'
    print(f'''
{kras}══════════════════════╗{kon}
[&] Версия {fio}INF{kon} [2.0]  {kras}║{kon}
{kras}══════════════════════╣{kon}
{zel}[0]{kon} Выход             {kras}║{kon}
{zel}[1]{kon} Удалить           {kras}║{kon}
{zel}[2]{kon} Обновить          {kras}║{kon}
{zel}[3]{kon} Ручной запуск     {kras}║{kon}
{zel}[4]{kon} Запуск по списку  {kras}║{kon}
{zel}[5]{kon} Редактор списка   {kras}║{kon}
{kras}══════════════════════╝{kon}''')
    global command
    command = input(f'{jir}--> {kon}')
    if command == '1':
        return delete()
    elif command == '2':
        return update()
    elif command == '3':
        return zapusk(bmb)
    elif command == '4':
        return spzapusk(F1, F2, F3, bmb)
    elif command == '5':
        return Z(F1, F2, F3)
    elif command == '0':
        print(f'{kras}Выход{kon} из {fio}INF{kon}...{kon}')
        time.sleep(1)
        sys.exit()
    else:
        os.system(ff)
        return start()

def delete():
    kill = input(f'{jel}Вы уверены что хотите {jel}удалить{kon} {fio}INF{kon}({zel}Y{kon}/{kras}N{kon})?')
    if kill == 'yes' or kill == 'y' or kill == 'Y' or kill == 'YES':
        os.system('rm -rf $HOME/INF2.0')
    elif kill == 'n' or kill == 'no' or kill == 'N' or  kill == 'NO':
        return start()

def update():
    os.system(ff)
    print(f'{zel}Обновление{kon} {fio}INF{kon}...')
    time.sleep(2)
    os.system('cd ~ ; pkg install git python3 nano')
    os.system('cd ~ ; git clone https://github.com/llll3/INF2.0')
    os.system('cp ~/INF2.0/bmb/bash.bashrc ../usr/etc/')
    os.system('cd ~ ; source ../usr/etc/bash.bashrc')
    os.system('yes | pkg update ; yes | upgrade')
    time.sleep(4)
    os.system(ff)
    print(f'{zel}Обновление завершенно!{kon}')
    time.sleep(2)
    return start()


#def install():
#    os.system(ff)
#    print(f'{zel}Установка{kon} {fio}INf{kon}...')
#    time.sleep(2)
#    os.system('cd ~ ; pkg install git python3 nano')
#    os.system('cd ~ ;git clone https://github.com/llll3/INF2.0')
#    os.system('cp ~/INF2.0/bmb/bash.bashrc ../usr/etc/')
#    os.system('cd ~ ; source ../usr/etc/bash.bashrc')
#    os.system('yes | pkg update ; yes | pkg upgrade')
#    time.sleep(4)
#    os.system(ff)
#    print(f'{zel}Установка завершенна!{kon}')
#    time.sleep(1)
#    return start()


def zapusk(bmb):
    os.system(ff)
    print(f'{zel}Запуск{kon} {fio}INF{kon}...')
    time.sleep(1)
    os.system(f'chmod 777 {bmb} ; {bmb}')
    return exit1()


def spzapusk(F1, F2, F3, bmb):
    os.system(ff)
    z3z4_2(F1, F2, F3, gg=1)
    number = nomer2
    return sms(F1, F2, F3, bmb, number)


def sms(F1, F2, F3, bmb, number):
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
    try:
        b = int(input(f'{jir}--> {kon}'))
    except ValueError:
        os.system(ff)
        print(f'{kras}Ошибка{kon}: {jel}вводить только цифры{kon}!')
        time.sleep(2)
        return sms(F1, F2, F3, bmb, number)
    if b == 0:
        spzapusk(F1, F2, F3, bmb)
    if b == 4:
        faq(F1, F2, F3, bmb, number)

    list3 = list(range(1, 4))
    with open(F1):
        if b in list3:
            os.system(f'chmod 777 {bmb} ; {bmb} {number} {b} 1 0')
            return exit1()
        if b not in list3:
            os.system(ff)
            print(f'{kras}Ошибка{kon}: {jel}неверный ввод{kon}!')
            time.sleep(2)
            return sms(F1, F2, F3, bmb, number)


def faq(F1, F2, F3, bmb, number):
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
        return sms(F1, F2, F3, bmb, number)
    else:
        os.system(ff)
        print(f'{kras}Ошибка{kon}: {jel}Неверный ввод{kon}!')
        time.sleep(1)
        return faq(F1, F2, F3, bmb, number)


def exit1():
    os.system(ff)
    ee = input(
        f'{kras}Выйти{kon} из {fio}INF{kon}?({zel}Y{kon}{jir}/{kras}N{kon}): ')
    if ee == 'y' or ee == 'yes' or ee == 'Y' or ee == 'YES':
        return sys.exit()
    elif ee == 'n' or ee == 'no' or ee == 'N' or ee == 'NO':
        return start()
    else:
        return exit1()
#################################################################


def Z(F1, F2, F3):
    os.system(ff)
    print(f'''
{kras}══════════════════════╗{kjir}
[&] Редактор списка:  {kras}║{kjir}
{kras}══════════════════════╣{kjir}
{zel}[0]{kon} Назад             {kras}║{kjir}
{zel}[1]{kon} Список            {kras}║{kjir}
{zel}[2]{kon} Удалить           {kras}║{kjir}
{zel}[3]{kon} Добавить          {kras}║{kjir}
{zel}[4]{kon} Изменить          {kras}║{kjir}
{zel}[5]{kon} Резерв списка     {kras}║{kjir}
{kras}══════════════════════╝{kon}''')
    global abba
    abba = input(f'{jir}--> {kon}')
    if abba == '0':
        return start()
    if abba == '1':
        return z1(F1, F2, F3, abba)
    elif abba == '2':
        return z3(F1, F2, F3)
    elif abba == '3':
        return z2(F1, F2, F3)
    elif abba == '4':
        return z4(F1, F2, F3)
    elif abba == '5':
        return z5(F1, F2, F3)
    elif abba != list2:
        return Z(F1, F2, F3)
    else:
        os.system(ff)
        print(f'{kras}Ошибка{kon}:{jel}Неверный ввод{kon}!')
        time.sleep(1)


def z1(F1, F2, F3, abba):
    z1_2(F1, F2, F3)
    z1_3(F1, F2, F3)
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
    if abba == '2':
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

    with open(F3) as f3:
        Num = len(f3.readlines())
        Num += 1
        global list1
        list1 = list(range(0, Num))
    with open(F3) as f3:
        for n, line in enumerate(f3, 1):
            line1 = line.strip('\n')
            print(f'{key}{jir}[{n}]{kjir} {line1}')
        print(f'{kras}══════════════════════════════╝{kon}')
    if abba == '1':
        cc = input(f'{jir}--> {kon}')
        if cc == '0':
            return Z(F1, F2, F3)
        else:
            os.system(ff)
            print(f'{kras}Ошибка{kon}: {jel}Неверный ввод{kon}!')
            time.sleep(1)
            return z1(F1, F2, F3, abba)


def z1_2(F1, F2, F3):
    with open(F1) as f1, open(F2) as ff1, open('nnames.txt', 'w') as f2, open("nnumbers.txt", "w") as ff2:
        for line1 in f1:
            if line1.strip():
                f2.write(line1)
        for line2 in ff1:
            if line2.strip():
                ff2.write(line2)
    os.rename("nnames.txt", F1)
    os.rename("nnumbers.txt", F2)


def z1_3(F1, F2, F3):
    TF3 = F3 + '.tmpp'  # создаём файл
    os.system("touch %s" % TF3)  # временный файл
    with open(F1) as f1, open(F2) as f2, open(TF3, 'w') as f4:
        # переименовываем временный файл
        os.system("mv %s %s" % (F1, 'nnames.tmp'))
        os.system("mv %s %s" % (F2, 'nnumbers.tmp'))
        os.system("mv %s %s" % ('nnames.tmp', F1))
        os.system("mv %s %s" % ('nnumbers.tmp', F2))
        for i, j in zip(f1.readlines(), f2.readlines()):
            f4.write(f'{i.strip()}: {j}')
    path3 = os.path.join(os.path.abspath(os.path.dirname(__file__)), F3)
    os.remove(path3)  # удаляем основной файл
    os.system("mv %s %s" % (TF3, F3))


def z3(F1, F2, F3):
    os.system(ff)
    print(f'''
{kras}════════════════╗{kjir}
[&] Удалить:    {kras}║{kjir}
{kras}════════════════╣{kjir}
{zel}[0]{kon} Назад       {kras}║{kjir}
{zel}[1]{kon} Продолжить  {kras}║{kjir}
{kras}════════════════╝{kon}''')
    tt = input(f'{jir}--> {kon}')
    if tt == '0':
        Z(F1, F2, F3)

    if tt == '1':
        z3_3(F1, F2, F3)
        os.system(ff)
        print(f'{zel}Удаленно имя:{kon} {kras}{nomer11}{kon}')
        print(f'{zel}Удален номер:{kon} {kras}{nomer22}{kon}')
        time.sleep(2)
        z3(F1, F2, F3)
    else:
        os.system(ff)
        print(f'{kras}Ошибка{kon}: {jel}Неверный ввод{kon}!')
        time.sleep(1)
        z3(F1, F2, F3)


def z3_3(F1, F2, F3):
    z3z4_2(F1, F2, F3, gg=3)
    global nomer11
    nomer11 = nomer1
    global nomer22
    nomer22 = nomer2
    hh = jek
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


def z2(F1, F2, F3):
    os.system(ff)
    print(f'''
{kras}════════════════╗{kjir}
[&] Добавить:   {kras}║{kjir}
{kras}════════════════╣{kjir}
{zel}[0]{kon} Назад       {kras}║{kjir}
{zel}[1]{kon} Продолжить  {kras}║{kjir}
{kras}════════════════╝{kon}''')
    xx = input(f'{jir}--> {kon}')
    if xx == '0':
        return Z(F1, F2, F3)
    if xx == '1':
        return z2_22(F1, F2, F3)
    else:
        os.system(ff)
        print(f'{kras}Ошибка{kon}: {jel}Неверный ввод{kon}!')
        time.sleep(1)
        return z2(F1, F2, F3)


def z2_22(F1, F2, F3):
    os.system(ff)
    with open(F1, 'a') as f1, open(F2, 'a') as ff1:
        print(f'''{jel}
Подсказка: Имя должно быть не больше 12 символов, а номер должен состоять {kras}только{kon}{jel} из 11 цифр.
Подсказка: Номер должен начинаться с 7(без +).{kon}''')
        xx = input('Введите имя: ')
        F11 = open(F1)
        gg = F11.readlines()
        F11.close()
        if str(xx) + '\n' in gg:
            os.system(ff)
            print(f'{kras}Ошибка{kon}: {jel}имя уже существует{kon}!')
            time.sleep(2)
            return z2_22(F1, F2, F3)
        elif str(xx) in gg:
            os.system(ff)
            print(f'{kras}Ошибка{kon}: {jel}имя уже существует{kon}!')
            time.sleep(2)
            return z2_22(F1, F2, F3)

        if len(xx) <= 12:
            try:
                xxx = int(input('Введите номер: '))
                F22 = open(F2)
                gg1 = F22.readlines()
                F22.close()
                if str(xxx) + '\n' in gg1:
                    os.system(ff)
                    print(f'{kras}Ошибка{kon}: {jel}номер уже существует{kon}!')
                    time.sleep(2)
                    return z2_22(F1, F2, F3)
                elif str(xxx) in gg1:
                    os.system(ff)
                    print(f'{kras}Ошибка{kon}: {jel}номер уже существует{kon}!')
                    time.sleep(2)
                    return z2_22(F1, F2, F3)

            except ValueError:
                os.system(ff)
                print(
                    f'{kras}Ошибка{kon}: {jel}номер должен состоять {kras}только{kon} {jel}цифр{kon}!')
                time.sleep(3)
                return z2_22(F1, F2, F3)
            xxx = str(xxx)
            if len(xxx) == 11 and xxx[0] == '7':
                xxx = int(xxx)
                f1.write(f'\n{xx}')
                ff1.write(f'\n{xxx}')
                os.system(ff)
                print(f'{zel}Добавлено имя:{kon}{jel} {xx}{kon}')
                print(f'{zel}Добавлен номер:{kon}{jel} {xxx}{kon}')
                time.sleep(3)

            else:
                os.system(ff)
                print(
                    f"""{kras}Ошибка{kon}:{jel} номер должен начинаться с 7(без +),
                а также должен состоять из 11 цифр{kon}!""")
                time.sleep(2)
        else:
            os.system(ff)
            print(
                f'{kras}Ошибка{kras}:{jel} имя не должно превышать 12 символов{kon}!')
            time.sleep(2)
    z2(F1, F2, F3)


def z3z4_2(F1, F2, F3, gg):
    os.system(ff)
    if gg == 1:
        z1(F1, F2, F3, abba=1)
    elif gg == 3 or gg == 4:
        z1(F1, F2, F3, abba)
    try:
        global jek
        jek = int(input(f'{jir}Введите поряд.номер: {kon}'))
    except ValueError:
        os.system(ff)
        print(f'{kras}Вводить только цифры!{kon}')
        time.sleep(1)
        return z3z4_2(F1, F2, F3, gg)
    if jek == 0:
        return start()
    if jek in list1:
        with open(F1) as fff1, open(F2) as fff2:
            h = jek
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
    else:
        os.system(ff)
        print(f'{kras + jir}Неверный ввод!{kon}')
        time.sleep(1)
        return z3z4_2(F1, F2, F3, gg)
    return


def z4_3(F1, F2, F3, FT1, FT2, new1, new2):
    TF1 = F1 + '.tmp'
    TF2 = F2 + '.tmp'   # создаём файл
    os.system("touch %s" % TF1)
    os.system("touch %s" % TF2)    # временный файл

    with open(F1) as f1, open(TF1, 'w') as f2, open(F2) as ff1, open(TF2, 'w') as ff2:
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
    print(f'{zel}Успешно{kon}, изменено имя{kon}: {kras}{FT1}{kon} на {jel}{new1}{kon}')
    print(f'{zel}Успешно{kon}, изменён номер{kon}: {kras}{FT2}{kon} на {jel}{new2}{kon}')
    time.sleep(5)
    return z4(F1, F2, F3)


def z4(F1, F2, F3):
    os.system(ff)
    print(f'''
{kras}════════════════╗{kjir}
[&] Изменить:   {kras}║{kjir}
{kras}════════════════╣{kjir}
{zel}[0]{kon} Назад       {kras}║{kjir}
{zel}[1]{kon} Продолжить  {kras}║{kjir}
{kras}════════════════╝{kon}''')
    kl = input(f'{jir}--> {kon}')
    if kl == '0':
        return Z(F1, F2, F3)
    if kl == '1':
        os.system(ff)
        z3z4_2(F1, F2, F3, gg=4)
        FT1 = nomer1
        FT2 = nomer2
        return z4_22(F1, F2, F3, FT1, FT2)
    else:
        os.system(ff)
        print(f'{kras + jir}Неверный ввод!{kon}')
        time.sleep(1)
        return z4(F1, F2, F3)


def z4_22(F1, F2, F3, FT1, FT2):
    os.system(ff)
    print(f'''{jel}
Подсказка: Имя должно быть не больше 12 символов, а номер должен состоять {kras}только{kon}{jel} из 11 цифр.
Подсказка: Номер должен начинаться с 7(без +).{kon}''')
    new1 = input('Введите новое имя: ')
    F11 = open(F1)
    gg1 = F11.readlines()
    F11.close()
    if str(new1) + '\n' in gg1:
        os.system(ff)
        print(f'{kras}Ошибка{kon}: {jel}имя уже существует{kon}!')
        time.sleep(2)
        return z4_22(F1, F2, F3, FT1, FT2)
    elif str(new1) in gg1:
        os.system(ff)
        print(f'{kras}Ошибка{kon}: {jel}имя уже существует{kon}!')
        time.sleep(2)
        return z4_22(F1, F2, F3, FT1, FT2)

    if len(new1) <= 12:
        try:
            new2 = int(input('Введите новый номер: '))
            F22 = open(F2)
            gg2 = F22.readlines()
            new2 = str(new2)
            F22.close()
            if str(new2) + '\n' in gg2:
                os.system(ff)
                print(f'{kras}Ошибка{kon}: {jel}номер уже существует{kon}!')
                time.sleep(2)
                return z4_22(F1, F2, F3, FT1, FT2)
            elif str(new2) in gg2:
                os.system(ff)
                print(f'{kras}Ошибка{kon}: {jel}номер уже существует{kon}!')
                time.sleep(2)
                return z4_22(F1, F2, F3, FT1, FT2)

        except ValueError:
            os.system(ff)
            print(f'{kras}Вводить только цифры!{kon}')
            time.sleep(1)
            return z4_22(F1, F2, F3, FT1, FT2)
        new2 = str(new2)
        if len(new2) == 11 and new2[0] == '7':
            new2 = int(new2)
            return z4_3(F1, F2, F3, FT1, FT2, new1, new2)
        else:
            os.system(ff)
            print(
                f'''{kras}Ошибка{kon}:{jel} номер должен начинаться с 7(без +),
             а также должен состоять из 11 цифр{kon}!''')
            time.sleep(2)
    else:
        os.system(ff)
        print(f'{kras}Ошибка{kon}:{jel} имя не должно превышать 12 символов{kon}!')
        time.sleep(2)
    return z4_22(F1, F2, F3, FT1, FT2)

def z5(F1, F2, F3):
    os.system(ff)
    print(f'''
{kras}════════════════════╗{kjir}
[&] Резерв списка:  {kras}║{kjir}
{kras}════════════════════╣{kjir}
{zel}[0]{kon} Назад           {kras}║{kjir}
{zel}[1]{kon} Создать         {kras}║{kjir}
{zel}[2]{kon} Удалить         {kras}║{kjir}
{zel}[3]{kon} Восстановить    {kras}║{kjir}
{kras}════════════════════╝{kon}''')
    hhh = input(f'{jir}--> {kon}')
    if hhh == '0':
        return Z(F1, F2, F3)
    elif hhh == '1':
        return z5_1(F1, F2, F3)
    elif hhh == '2':
        return z5_2(F1, F2, F3)
    elif hhh == '3':
        return z5_3(F1, F2, F3)
    else:
        return z5(F1, F2, F3)

def z5_1(F1, F2, F3):
    os.system(ff)
    print(f'{jel}Резервирование...{kon}')
    time.sleep(3)
    os.system('rm -rf $HOME/rezerv')
    os.system('cp $HOME/INF2.0/nanu $HOME/ -r')
    os.system('mv $HOME/nanu $HOME/rezerv')
    os.system(ff)
    print(f'{zel}Резервная копия создана!{kon}')
    time.sleep(3)
    return z5(F1, F2, F3)

def z5_2(F1, F2, F3):
    os.system(ff)
    print(f'{kras}Удаление...{kon}')
    time.sleep(3)
    os.system('rm -rf $HOME/rezerv')
    os.system(ff)
    print(f'{zel}Удалено!{kon}')
    time.sleep(3)
    return z5(F1, F2, F3)


def z5_3(F1, F2, F3):
    os.system(ff)
    print(f'{zel}Восстановление...{kon}')
    time.sleep(3)
    os.system('cp $HOME/rezerv/ $HOME/INF2.0/ -r')
    os.system('rm -rf $HOME/INF2.0/nanu')
    os.system('mv $HOME/INF2.0/rezerv/ $HOME/INF2.0/nanu')
    os.system(ff)
    print(f'{zel}Восстановленно!{kon}')
    time.sleep(3)
    return z5(F1, F2, F3)




start()
