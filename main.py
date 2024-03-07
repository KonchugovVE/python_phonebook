def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=7):

        if choice==1:
            print(print_phonebook(phone_book))
           
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(print_phonebook(change_number(phone_book,last_name,new_number)))
        elif choice==4:
            print(print_phonebook(NewAbon(phone_book)))	
        elif choice==5:
            znachenie=input('Введите значение поиска =>: ')
            print(print_phonebook(delete_by_lastname(phone_book,znachenie)))
        
        elif choice==6:
            
            write_txt('copyphonebook.txt',phone_book)


        choice=show_menu()


def show_menu():  # вывод в консоль меню и запрос ввода от пользователя

    print("\n Выберите необходимое действие:\n",
          "1. Отобразить весь справочник\n",
          "2. Найти абонента по фамилии\n",
          "3. Изменить номер телефона абонента\n",
          "4. Добавить абонента\n",
          "5. Удалить абонента\n",
          "6. Сохранить справочник в текстовом формате\n",
          "7. Завершить работу")
    print('=>:', end='')
    choice = int(input())
    return choice


def read_txt(filename): # чтение файла и создание переменной phone_book


    phone_book=[]

    fields=['Фамилия', 'Имя', 'Номер телефона', 'Описание ']

	

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

            record = dict(zip(fields, line.split(',')))

            phone_book.append(record)	
			#dict(( (С„Р°РјРёР»РёСЏ,РРІР°РЅРѕРІ),(РёРјСЏ, РўРѕС‡РєР°),(РЅРѕРјРµСЂ,8928) ))

    return phone_book


def write_txt(filename , phone_book): # перезапись файла


    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')

# def print_book(filename):
#     book =[]
#     with open (filename, "r", encoding='utf-8') as book:
#         for line in book:
#             print (*line)

def print_phonebook(phone_book): # распечатка книги с фиксированой длиной строки 

    lenName=3
    lenSurname=7
    lenNamberphone=16
    lenDescription=9
    stroki=''
    cherta='_'

    for line in phone_book:    # проверяем кол-во символов ключа и содержимого, большее записываем
        for key in line.keys():
            if key == 'Фамилия':
                # print(line[key],len(line[key]))
                if len(line[key])>lenSurname:
                    lenSurname=len(line[key])
                    # print(lenSurname)
            elif key == 'Имя':
                if len(line[key])>lenName:
                    lenName=len(line[key])       
            elif key == 'Номер телефона':
                # print(line[key],len(line[key]))
                if len(line[key])>lenNamberphone:
                    lenNamberphone=len(line[key]) 
            elif key == 'Описание ':
                if len(line[key])>lenDescription:
                    lenDescription=len(line[key]) 
            # print (lenDescription,lenNamberphone,lenName,lenSurname)

    for key in phone_book[0].keys(): # печатаем шапку отцентровывая каждый столбец
        if key == 'Фамилия':
            # print ('|', key.center(lenSurname), end='')
            stroki=f'{stroki}|{key.center(lenSurname)}'

        elif key == 'Имя':
            #print ('|', key.center(lenName), end='')
            stroki=f'{stroki}|{key.center(lenName)}'
    
        elif key == 'Номер телефона':
            #print ('|', key.center(lenNamberphone), end='')
            stroki=f'{stroki}|{key.center(lenNamberphone)}'
    
        elif key == 'Описание ':
            #print ('|', key.center(lenDescription), '|\n')
            stroki=f'{stroki}|{key.center(lenDescription)} |\n|{cherta*(lenSurname+lenName+lenNamberphone+lenDescription+4)}|\n'
        
    for line in phone_book: # печатаем содержимое книги, отцентровывая каждый столбец       
        for key in line.keys():
            if key == 'Фамилия':
                #print ('|', line[key].center(lenSurname), end='')
                stroki=f'{stroki}|{line[key].center(lenSurname)}'

            elif key == 'Имя':
                #print ('|', line[key].center(lenName), end='')    
                stroki=f'{stroki}|{line[key].center(lenName)}'

            elif key == 'Номер телефона':
                #print ('|', line[key].center(lenNamberphone), end='')
                stroki=f'{stroki}|{line[key].center(lenNamberphone)}'

            elif key == 'Описание ':
                if '\n' in line[key]:
                    stroka=line[key]
                    stroka = stroka[:-1]
                    #print ('|',stroka.center(lenDescription),'|\n')
                    stroki=f'{stroki}|{stroka.center(lenDescription)} |\n'

                else:
                    #print ('|', line[key].center(lenDescription), end='|\n')
                    stroki=f'{stroki}|{line[key].center(lenDescription)} |\n'
    return stroki
        
            
def find_by_lastname(phone_book,znachenie):  # поиск по фамилии
    count =0
    for line in phone_book:
        if znachenie in line['Фамилия']:
            count+=1
            for key in line.keys():
                print(line[key], end=" ")
    if count == 0:
        print ('С Фамилией >:', znachenie,'нет контактов' )
        
def change_number(phone_book,last_name,new_number): # замена номера по фамилии
    count =0
    
    for line in phone_book:
        if last_name in line['Фамилия']:
            count +=1
            
            
    if count==0:
        print ('Контакта', last_name, 'несуществует')
    elif count==1:
        for line in phone_book:
            if last_name in line['Фамилия']:            
                line['Номер телефона'] = new_number
    elif count >1:
        print ('Под этой фамилией',count,' абонета')
    
    return phone_book
def NewAbon(phone_book): # добавления записи нового абонента

    abon = {}
    for key in phone_book[0]:
        print(key,'=>', end='')
        abon[key]= input()
    
    phone_book.append(abon)
    return phone_book

def delete_by_lastname(phone_book,lastname):   # удаление записи нового абонента
    numstroki=0
    for line in range(len(phone_book)):
       stroka = phone_book[line]
       for key in stroka.keys():
           if lastname == stroka[key]:
               numstroki=line
    phone_book.pop(numstroki)    
            
    return phone_book

work_with_phonebook()

