import sys
#cd=''
#cd = ("\ "[:-1]).join(['C:','Users', 'User','Desktop','fm','code',''])
file = open("adress_coda.txt", "r")
cd = file.read().split('\n')
try:
    cd2 = cd[1]
except IndexError:
    cd2 = ''
try:
    cd=cd[0]
except IndexError:
    cd = ''
file.close()
sys.path.insert(0, cd)
#from C:.Users.User.Desktop.fm.code. 
import filemanager_itogp_z as f
import bcrypt

name = input('Здравствуйте. Представьтесь, пожалуйста: ')
try:
    file = open(cd+"pas"+name+".bin", "rb")
    key = file.read()
    file.close()
except FileNotFoundError:
    
    print('Мы ещё не знакомы.')
    msg = input('Введите ваш пароль: ')
    msg = bcrypt.hashpw(bytes(msg, encoding='utf-8'), bcrypt.gensalt())
    file = open(cd+"pas"+str(name)+".bin", "wb")
    file.write(msg)
    file.close()
    msg = input('Введите имя вашей папки (желательно без пробелов): ')
    home = cd2+msg
    file = open(cd+"pap"+str(name)+".txt", "w")
    file.write(home)
    file.close()
    home = home.split('\\')
    f.sozd_direk(("\ "[:-1]).join(home))
else:
    print('Мы уже встречались')
    
    while True:
        msg = input('Введите ваш пароль: ')
        if bcrypt.checkpw(bytes(msg, encoding='utf-8'), key):
            print('Пароль принят')
            break
        else:
            print('Неверный пароль')

    file = open(cd+"pap"+name+".txt", "r")
    home = file.read().split('\\')
    file.close()
    del(key)
del(msg)

f.chdirr(("\ "[:-1]).join(home), home, home)
#print(f.mesto(home))
while True:
    print('\nВ именах файлов надо писать .txt или проч.')
    print("exitt - выход; pwdd - текущая директория; lss - все папки из в директории; zipuy {name} - зазиповать; dezip {name} - раззиповать; openn {name} - содержимое текста; chdirr {name} - изменить рабочую директорию; mkdirr {name} - создать директорию; remdirr {name} - удалить директорию; touchh {name} - создать файл; dell {name} - удалить файл; movetoo {name1} {name2} - перенести в указанную директорию; renamee {name1} {name2} - переименовать; copyfilee {name1} {name2} - копировать файл внутри директории; copytoo {name1} {name2} - копировать в другую директорию;")
    
    put = str(f.os.getcwd()) + ': '#получить рабочую директорию
    kom = input(put).split(' ')
    try:
        dlin = len (kom)
        if dlin == 1:
            if kom[0] == 'pwdd':#текущая директория
                f.tekush()
            elif kom[0] == 'lss':#все папки из в директории
                f.iz_direk()
            elif kom[0] == 'exitt':
                break
            else:
                print('Обнаружена неизвестная пользовательская команда. Выполнение невозможно\n')
        elif f.analiz(kom[1], home, put):
            if dlin == 2:
                if kom[0] == 'openn':#содержимое текста
                    f.open_file(kom[1])
                elif kom[0] == 'chdirr':#изменить рабочую директорию
                    f.chdirr(kom[1], home, put)
                elif kom[0] == 'mkdirr':#создать директорию
                    f.sozd_direk(kom[1])
                elif kom[0] == 'remdirr':#удалить директорию
                    f.kill_it(kom[1])
                elif kom[0] == 'touchh':#создать файл
                    f.stroi(kom[1])
                elif kom[0] == 'dell':#удалить файл
                    f.exterminate(kom[1])
                elif kom[0] == 'zipuy':
                    f.zazipovat(kom[1])
                elif kom[0] == 'dezip':
                    f.razzipovka(kom[1])
                else:
                    print('Обнаружена неизвестная пользовательская команда. Выполнение невозможно\n')
            elif f.analiz(kom[2], home, put):
                    if dlin == 3:
                        if kom[0] == 'movetoo':#перенести в указанную директорию
                            f.movetoo(kom[1], kom[2])
                        elif kom[0] == 'renamee':
                            f.renamee(kom[1], kom[2])
                        elif kom[0] == 'copyfilee':#копировать файл внутри директории
                            f.copy_file(kom[1], kom[2])
                        elif kom[0] == 'copytoo':
                            f.copy_folder(kom[1], kom[2])#копировать в другую дтректорию
                        else:
                            print('Обнаружена неизвестная пользовательская команда. Выполнение невозможно\n')
                    else:
                        print('Слишком... Много... Слов!!!')
            else:
                print('Не выходить за пределы папки')
        else:
            print('Не выходить за пределы папки')
    except FileNotFoundError:
        print('Требуемый объект не обнаружен')
    except PermissionError:
        print('Доступ запрещён')
    except:
        print('Невыполнимое требование. Проверьте корректность запроса')
#'''

