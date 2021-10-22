import os
import shutil
import zipfile
'''
def mesto (home):
    disk = os.statvfs(("\ "[:-1]).join(home))
    print(disk.f_blocks, disk.f_bfree, disk.f_blocks-disk.f_bfree)#'''
    
def zazipovat(file_name):
    if zipfile.is_zipfile(file_name):
        print('Он уже зазипован')
    else:
        z = zipfile.ZipFile(file_name.split('.')[0]+'.zip', 'w')
        z.write(file_name)
        z.close()
        print(file_name+' файл успешно зазипован')
def razzipovka (file_name):
    if zipfile.is_zipfile(file_name):
        z = zipfile.ZipFile(file_name, 'r')
        z.extractall()
    else:
        print('Не, это не зип')
      
def tekush():
    pathh = os.getcwd()
    print(pathh, '\n')
    pathh = pathh.split('\\')
    print(pathh[len(pathh)-1], '\n')

def kill_it(dir_name):
    os.rmdir(dir_name)
    print('Директория '+dir_name+' удалена')

def sozd_direk(dir_name):
    if not os.path.isdir(dir_name):
        os.umask(0)
        os.mkdir(dir_name,0o777)
        print('Директория с именем '+dir_name+' создана')
    else:
        print('Нельзя сотворить две директории с одинаковыми именами!')

def iz_direk():
    spicokk = os.listdir()
    for i in (spicokk):
        print(i)
    print('\n')

def stroi(file_name):
    if not os.path.isfile(file_name):
        text_file = open(file_name, 'w+')
        text_file.write('')
        os.startfile(file_name)
        print('Сделаем!')
    else:
        print('Здесь нельзя строить!')

def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        print(*file)

def renamee(old_Fname, new_Fanme):
    try:
        os.rename(old_Fname, new_Fanme)
    except PermissionError:
        print('Нельзя просто так взять и переименовать '+old_Fname+' в '+new_Fanme)
    except:
        print('Мы не смогли найти '+old_Fname+' и переименовать его в '+new_Fanme)
    else:
        print(new_Fanme+': эта программа меняет людей, раньше я был - '+old_Fname)

def exterminate(file_name):
    os.remove(file_name)
    print('Джони, я файла '+file_name+' не чувствую')

def movetoo(file_name, dir_name):
    os.replace(file_name, f'{dir_name}/{file_name}')
    print('Файл '+file_name+' был перемещён в директорию '+dir_name)

def chdirr(dir_name, home, put):
    if dir_name != 'back':
        os.chdir(dir_name)
        print('Рабочая директория изменена на '+dir_name)
    elif ("\ "[:-1]).join(home) == ("\ "[:-1]).join(put[:-2].split("\\")):
        print('Не выходить за пределы папки')
    else:
        os.chdir('..')
        print('Возврат к предыдущей директории')

def copy_file(file_name, second_file):
    shutil.copyfile(file_name, second_file)
    print('Файл '+file_name+' скопирован')

def copy_folder(file_name, dir_name):
    if os.path.isdir(dir_name):
        shutil.copy(file_name, dir_name)
        print('Файл '+file_name+' был скопирован в директорию '+dir_name)
    else:
        print('Не получилось найти директорию')
def analiz(cel, home, put):
    try:
        os.chdir(cel)
    except:
        return(True)
    cel = str(os.getcwd()).split('\\')
    os.chdir(("\ "[:-1]).join(put[:-2].split("\\")))
    #print(cell, home, cel[-1][-1])
    #print(len(cell)<len(home))
    #print(cel[0] != home[0] , cel[-1][-1] == ":" , len(cel)<len(home))
    if  len(cel)<len(home):
        #print(len(cel)<len(home), cel, home)
        return(False)
    elif cel[0] != home[0] and (cel[-1][-1] == ":"):
        #print(12)
        return(False)
    else:
        k=0
        for i in home:
            #print(i, cel[k])
            if i != cel[k]:
                return(False)
            k +=1
    return(True)




