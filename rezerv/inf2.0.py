import os
import sys
import time
numbers = str(list(range(1, 10)))
ff = 'clear'
zel = '\033[32m\033[1m'
kras = '\033[31m\033[1m'
jir = '\033[1m\033[1m'
kon = '\033[m\033[1m'
fio = '\033[35m\033[1m'
																									
def start():
		os.system(ff)
		print(f'''
{kras}══════════════════════╗{kon}
[&] Версия {fio}inf{kon} [2.0]  {kras}║{kon}
{kras}══════════════════════╣{kon}
[0] Выход             {kras}║{kon}
[1] Обновить          {kras}║{kon}
[2] Установить        {kras}║{kon}
[3] Ручной запуск     {kras}║{kon}
[4] Список контактов  {kras}║{kon}
[5] Настройка запуска {kras}║{kon}
{kras}══════════════════════╝{kon}''')
		command = input(f'{jir}--> {kon}')
		if command == '1':
				return update()
		elif command == '2':
				return install()
		elif command == '3':
				return zapusk()
		elif command == '4':
				return spisok()
		elif command == '5':
				return redakt()
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
		os.system('cd ~ ; pkg install git python3 nano ; git clone https://github.com/llll3/inf2.0 ; cd inf2.0 ; cp bash.bashrc ../../usr/etc/ ; source ../../usr/etc/bash.bashrc ; cd inf ; chmod 777 inf ; cd ~ ; yes | pkg update ; yes | pkg upgrade')
		os.sustem(ff)
		print(f'{zel}Обновление завершенно!{kon}')
		time.sleep(2)
		return start()
																											
def install():
		os.system(ff)
		print(f'{zel}Установка inf...{kon}')
		time.sleep(2)
		os.system('cd ~ ; pkg install git python3 nano ; git clone https://github.com/llll3/inf2.0 ; cd inf2.0 ; cp bash.bashrc ../../usr/etc/ ; source ../../usr/etc/bash.bashrc ; cd inf ; chmod 777 inf ; cd ~ ; yes | pkg update ; yes | pkg upgrade')
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
																												
def spisok():
		os.system(ff)
		print(f'''
{kras}══════════════════════╗{kon}
[&]Список контактов:  {kras}║{kon}
{kras}══════════════════════╣{kon}
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
{kras}══════════════════════╝{kon}''')
		global a
		a = input(f'{jir}--> {kon}')
		if a == '0':
				return start()
		if a in numbers:
				return sms()
		else:
				return spisok()
def sms():
		os.system(ff)
		print(f'''
{kras}══════════════════════╗{kon}
[&]Выбирите режим:    {kras}║{kon}
{kras}══════════════════════╣{kon}
[0] Назад             {kras}║{kon}
[1] Флуд SMS          {kras}║{kon}
[2] Флуд CALL         {kras}║{kon}
[3] CALL и SMS        {kras}║{kon}
[4] F.A.Q             {kras}║{kon}
{kras}══════════════════════╝{kon}''')
		b = input(f'{jir}--> {kon}')
		if b == '0':
				return spisok()
		if b == '4':
				return faq()
		else:
				return sms()
																										
def faq():
		os.system(ff)
		print(f'''
{kras}═══════════════════════════════════════════════╗{kon}
[&] F.A.Q:                                     {kras}║{kon}
{kras}═══════════════════════════════════════════════╣{kon}
[0] Назад.                                     {kras}║{kon}
[1] SMS - начинает флудить смс'ками.           {kras}║{kon}
[2] CALL - начинает флудить звон'ками.         {kras}║{kon}
[3] SMS и CALL - включает в себя 1 и 2 пункт.  {kras}║{kon}
{kras}═══════════════════════════════════════════════╝{kon}''')
		ww = input(f'{jir}--> {kon}')
		if ww == '0':
			return sms()
		else:
			return faq()
																										
def exit1():
		os.system(ff)
		ee = input(f'{jir}Выйти из {fio}inf{kon}?({zel}y{kon}{jir}/{kras}n{kon}): ')
		if ee == 'y' or ee == 'yes':
			return sys.exit()
		elif ee == 'n' or ee == 'no':
			return start()
		else:
			return exit1()

start()
