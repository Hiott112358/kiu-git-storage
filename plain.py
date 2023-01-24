import json

def read(name_file):
    with open(name_file,'r',encoding='utf-8') as file:
        return json.load(file)

data_beg = read('file.json')
data_fin = read('file_1.json')

#print(data_beg)
#print(data_fin)

def dell(data1,data2): #Если файл удалили 
    del_arr = []
    try:
        for i in data1:
            if i not in data2:
                del_arr.append(i)
        return del_arr
    except:
        new_arr = [data2]
        if data1 not in new_arr:
            del_arr.append(data1)
        return del_arr

def add(data1,data2): #Появился новый
    add_arr = []
    try:
        for i in data2:
            if i not in data1:
                add_arr.append(i)
        return add_arr
    except:
        new_arr = [data1]
        if (data2 not in new_arr):
            add_arr.append(data2)
        return add_arr

deleted = {}
newest = {}

for name, znac in data_beg.items(): #Ключ и значение
    for name2, znac2 in data_fin.items():
        if name == name2:
            deleted[str(name)] = (dell(znac,znac2))
            #print(deleted)
        if name == name2:
            newest[str(name)] = (add(znac, znac2))
            #print(newest)
#print(deleted)
#print(newest)
new_file = open("Differences.txt", "w+", encoding="utf-8")
for i,j in deleted.items():
    if j != []:
        new_file.writelines(f'Удалили в ключе {i} элементы со значением {j}' + '\n')
        print(f'Удалили в ключе {i} элементы со значением {j}')
for i,j in newest.items():
    if j != []:
        new_file.writelines(f'Добавили в ключе {i} элементы со значением {j}' + '\n')
        print(f'Добавили в ключе {i} элементы со значением {j}')

#new_file = open("Differences.txt", "w+", encoding="utf-8")
  
#new_file.writelines(f'Удалили в ключе {i} элементы со значением {j}' + '\n')
#new_file.writelines(f'Добавили в ключе {i} элементы со значением {j}' + '\n')
    #new_file.writelines(+ '\n')

    