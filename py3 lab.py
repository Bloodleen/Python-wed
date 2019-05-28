import os

def sort(i):
        return i[2]

def file()
    path = input('Введите путь ')
    lst = os.listdir(path)
    n = 0
    for vava in lst:
        if '.' in vava:
            n+=1
    print(n)

def text1():
    f=open('products.txt', 'r')
    a=(f.read()).split('\n')
    a.pop(0)
    a.sort(key=sort)
    lst=[]
    for i in range(len(a)):
        lst.append(a[i].split(';'))
    print(lst)

def text2():
    f=open('products.txt', 'r')
    a=(f.read()).split('\n')
    a.pop(0)
    c=int(input('Введите номер товара'))
    if c==0:
        c=int(input('Неверно, введите исправный номер товара'))
    b=int(input('Введите число, на которое надо увеличить количество товара'))    
    a.sort(key=sort)
    lst=[]
    for i in range(len(a)):
        lst.append(a[i].split(';'))
    for i in range(len(lst)):
        vava=lst[i]
        if vava[0]==str(c):
            vava[3]=str(b+int(vava[3]))
            lst[i]=vava
    print(lst)

def text3()
     f = open('products.txt','w')
     f.write('№;Наименование_товара;Цена;Количество')
     for vava in mlst:
         f.write('\n')
         f.write(';'.join(vava))
     f.close()

def menu(lst):
    print('')
    print('0 - Выход из программы')
    print('1 - Посчитать кол-во файлов в заданной директории')
    print('2 - Вывод информации о товарах и считывание для пунктов 3,4')
    print('3 - Увеличение количества товаров')
    print('4 - Сохранить')
    a = int(input('Ввод '))
    print('')
    if a == 0:
        return lst
    if a == 1:
        file()
        if int(input('Выход из программы? 1 - да, 0 - нет. '))== 1:
               return lst
        menu(lst)
    if a == 2:
        lst = text(lst)
        if int(input('Выход из программы? 1 - да, 0 - нет. ')) == 1:
            return lst
        menu(lst)
    if a == 3:
        lst = text1(lst)
        if int(input('Выход из программы? 1 - да, 0 - нет. '))== 1:
               return lst
        menu(lst)
    if a == 4:
        text3(lst)
        if int(input('Выход из программы? 1 - да, 0 - нет. '))== 1:
               return lst
        menu(lst)
    print('')
