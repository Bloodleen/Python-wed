import os

def sort(i):
        return i[2]

def file():
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

def text3():
    f=open('products.txt', 'r')
    a=(f.read()).split('\n')
    a.pop(0)
    a.sort(key=sort)
    f.close()
    f = open('products.txt','w')
    f.write('№;Наименование_товара;Цена;Количество')
    for vava in a:
        f.write('\n')
        f.write(vava)
    f.close()

def menu():
    print('')
    print('0 - Выход из программы')
    print('1 - Посчитать кол-во файлов в заданной директории')
    print('2 - Вывод информации о товарах и считывание для пунктов 3,4')
    print('3 - Увеличение количества товаров')
    print('4 - Сохранить')
    a = int(input('Ввод '))
    print('')
    if a == 0:
       sys.exit()
    if a == 1:
        file()
        while int(input('Выход из программы? 1 - да, 0 - нет. '))!= 1:
                file()
        menu()
    if a == 2:
        text1()
        while int(input('Выход из программы? 1 - да, 0 - нет. '))!= 1:
                text1()
        menu()
    if a == 3:
        text2()
        while int(input('Выход из программы? 1 - да, 0 - нет. '))!= 1:
                text2()
        menu()
    if a == 4:
        text3()
        while int(input('Выход из программы? 1 - да, 0 - нет. '))!= 1:
                text3()
        menu()
    print('')
