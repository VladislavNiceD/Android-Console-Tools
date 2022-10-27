import os
import colorama
from colorama import Fore, Back, Style
import time
import requests

#colors
yellow = Fore.YELLOW
green = Fore.GREEN
black = Fore.BLACK
grey = Fore.BLACK + Style.BRIGHT
red = Fore.RED
blue = Fore.BLUE

warning = yellow + '[!] ' + grey
error = red + '[×] ' + grey
success = green + '[✓] ' + grey

def connect(host):
	print(warning + 'Соединение с Android хостом')
	time.sleep(1)
	try:
		os.system(f'adb connect {host}')
		print(success + 'Успешное подключение к хосту')
	except:
		print(error + f'Не удалось подключиться к хосту {host}')
		time.sleep(2)

def reboot_recovery():
	print(warning + 'Перезагрузка Android устройства в recovery')
	time.sleep(1)
	try:
		os.system('adb reboot recovery')
		print(success + 'Android устройство успешно перезагружено в recovery')
	except:
		print(error + 'Не удалось перезагрузить Android устройство в recovery, проверьте, возможно хост не подключён к adb')
		time.sleep(2)

def reboot_bootloader():
	print(warning + 'Перезагрузка Android устройства в bootloader')
	time.sleep(1)
	try:
		os.system('adb reboot bootloader')
		print(success + 'Android устройство успешно перезагружено в bootloader')
	except:
		print(error + 'Не удалось перезагрузить Android устройство в bootloader, проверьте, возможно хост не подключён к adb')
		time.sleep(2)

def install(file):
	print(warning + f'Установка приложения {file} на Android устройство')
	time.sleep(1)
	try:
		os.system(f'adb install {file}')
		print(success + 'Приложение установлено')
	except:
		print(error + 'Не удалось установить приложение')
		time.sleep(2)

def devices():
	print(warning + 'Список устройств')
	time.sleep(1)
	try:
		os.system('adb devices')
	except:
		print(error + 'Не удалось отобразить список устройств, подключённых к adb')
		time.sleep(2)

def fastboot_devices():
	print(warning + 'Список устройств')
	time.sleep(1)
	try:
		os.system('fastboot devices')
	except:
		print(error + 'Не удалось отобразить список устройств, подключённых к ПК в режиме fastboot')
		time.sleep(2)

def flash(section, file):
	print(warning + f'Прошиваем файл {file} в раздел {section}')
	time.sleep(1)
	try:
		os.system(f'fastboot flash {section} {file}')
		print(success + 'Файл успешно прошит в раздел')
	except:
		print(error + f'Не удалось прошить файл {file} в раздел  {section}')
		time.sleep(2)

def fastboot_reboot():
	print(warning + 'Перезагрузка')
	time.sleep(1)
	try:
		os.system('fastboot reboot')
		print(success + 'Устройство перезагружено')
	except:
		print(error + 'Не удалось перезагрузить устройство')
		time.sleep(2)

def flash_boot(type):
	print(warning + 'Прошиваем анимацию загрузки')
	time.sleep(1)
	try:
		if type =='1':
			os.system('adb remount')
			os.system('adb push bootanimation.zip /data/local')
		elif type =='2':
			os.system('adb remount')
			os.system('adb push bootanimation.zip /product/media')
		print(success + 'Анимация загрузки прошита')
	except:
		print(error + 'Не удалось прошить анимацию загрузки')
		time.sleep(2)

def clear():
	os.system('clear||cls')

def install_modules():
	os.system('pip install colorama')
	os.system('pip install requests')

def main():
	clear()
	menu=input(grey + f'''
—————————————————————————
| Android Console Tools |
——————————————————{blue}ʙʏ ɴɪᴄᴇᴅ{grey}

1. ADB Функции
2. Fastboot Функции
: ''')
	clear()
	if menu =='1':
		adb_menu=input('''
—————————————
| ADB Tools |
—————————————

1. Подключиться к хосту
2. Перезагрузить в recovery
3. Перезагрузить в загрузчик
4. Установить приложение
5. Список устройств
0. Выйти
: ''')
		if adb_menu =='0':
			raise SystemExit
		elif adb_menu =='1':
			clear()
			host=input(grey + 'Введите IP хоста...\n: ')
			clear()
			connect(host)
		elif adb_menu =='2':
			clear()
			reboot_recovery()
		elif adb_menu =='3':
			clear()
			reboot_bootloader()
		elif adb_menu =='4':
			clear()
			path=input(grey + 'Введите полный путь до файла...\n: ')
			clear()
			install(path)
		elif adb_menu =='5':
			clear()
			devices()
	elif menu =='2':
		clear()
		fastboot_menu=input('''
——————————————————
| Fastboot Tools |
——————————————————

1. Список устройств
2. Прошить файл в раздел
3. Перезагрузить устройство
4. Прошить анимацию загрузки (Бета)
0. Выйти
: ''')
		if fastboot_menu =='0':
			raise SystemExit
		elif fastboot_menu =='1':
			clear()
			fastboot_devices()
		elif fastboot_menu =='2':
			clear()
			section=input(grey + 'Введите название раздела... (recovery, boot, system...)\n: ')
			clear()
			file=input(grey + 'Введите полный путь до файла...\n: ')
			clear()
			flash(section, file)
		elif fastboot_menu =='3':
			fastboot_reboot()
		elif fastboot_menu =='4':
			type=input(grey + 'Введите тип прошивки анимации... (У разных прошивок свой способ)\n: ')
			clear()
			flash_boot(type)