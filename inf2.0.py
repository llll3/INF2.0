import os
import sys
import time
menu1 = True
menu2 = True
menu3 = True
def exit():
	print('exit')

def redakt():
	global menu
	menu1 = False
	global  menu2
	menu2 = False
	os.system('clear')
	print('[Меню редактирования контактов]\n')
	print('[Выберите контакт]:')
	print('[0] Назад')
	print('[1] {name}')
	kon = input('--> ')
	if kon == '0':
		os.system('clear')
		menu1 = True
	else:
		os.system('clear')
		redakt()
	
	
def faq():
	global menu1
	menu1 = False
	global  menu2
	menu2 = False
	os.system('clear')
	print('[F.A.Q]:')
	print('''
[1] SMS - эта опция позволяет флудить смс'ками.
[2] CALL - эта опция позволяет флудить звон'ками.
[3] SMS in CALL - эта опция делает 1 и 2 пункт одновременно.''')
	print('[0] Назад')
	ww = input('--> ')
	if ww == '0':
		sms()
	else:
	    faq()
        

############inf1
def inf1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
	inf1= os.system('cd ~ ; cd inf2.0 ; cd inf ; ./inf 79283984241 1 1 0')
	sys.exit()
def inf2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def inf3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
############inf1
##############
###########ang2
def ang1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def ang2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def ang3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
##########ang2
#############
##########geo3
def geo1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def geo2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def geo3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
##########geo3
#############
##########bio4
def bio1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def bio2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def bio3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
##########bio4
#############
##########alg5
def alg1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def alg2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def alg3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
##########alg5
##############
##########rus6
def rus1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def rus2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def rus3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
##########rus6
#############
##########ist7
def ist1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def ist2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def ist3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
##########ist7
############
##########fiz8
def fiz1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def fiz2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def fiz3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
##########fiz8
#############
##########xim9
def xim1():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def xim2():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
def xim3():
	global menu2
	menu2 = False
	os.system('clear')
	print('Запуск inf....')
	time.sleep(1)
##########xim9


def install():
	os.system('clear')
	global menu1
	menu1 = False
	print('Установка inf...')
    
def update():
	os.system('clear')
	global menu1
	menu1 = False
	print('Обновление inf...')
 
def spisok():
    global menu1
    menu1 = False
    os.system('clear')
    print('[Список контактов]:')
    print('[0] Назад')
    print('[1] Информатика')
    print('[2] Английский')
    print('[3] География')
    print('[4] Биология')
    print('[5] Алгебра')
    print('[6] Русский')
    print('[7] История')
    print('[8] Физика')
    print('[9] Химия')
    global a
    a = input('--> ')
    if a == '0':
       os.system('clear')
       menu1 = True
    if a >= '1' and a <= '9':
    	sms()
    else:
    	spisok()
 
def sms():
     os.system('clear')
     print('[Выбирите режим]:')
     print('[0] Назад')
     print('[1] Флуд SMS')
     print('[2] Флуд CALL')
     print('[3] CALL и SMS')
     print('[4] F.A.Q')
     b = input('--> ')
     if b == '0':
     	os.system('clear')
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
          os.system('clear')
          sms()
             
		     	
	
     	
     	
     	
     	
while menu1 == True:
    os.system('clear')
    print('[Версия inf 2.0]\n')   
    print('[Выберите пункт]: ')
    print('[1] Установить inf.')
    print('[2] Обновить inf.')
    print('[3] Список контактов.')
    print('[4] Изменить список')
    print('[5] Выйти')
    command = input('--> ')
    if command == '1':
        install()
    elif command == '2':
        update()
    elif command == '3':
        spisok()
    elif command == '4':
        redakt()
    elif command == '5': 
        print('Выход из inf...')
        time.sleep(1)        
        break
    else:
    	os.system('clear')
    	menu1 = True
