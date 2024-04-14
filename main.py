#Телефонный справочник
contact_data = {
    'first_name': None,
    'second_name': None,
    'phon_number': None,
    }

def add_new_contact ():
    with open('phonebook.txt', 'a', encoding="utf8") as file:
        contact = ask_data()
        for value in contact.values():
            file.write(f"{value};")
        file.write('\n')
        input('Запись добавлена в справочник. Нажмите любую клавишу для продолжения')
    return True

def open_contact():
    title = ["№ ","Фамилия","Имя","Отчество","Телефон"]
    print('| {:2} | {:<10} | {:<10} | {:<15} | {:<12} |'.format(*title))
    print('-----------------------------------------------------------------')
    with open('phonebook.txt', 'r', encoding="utf8") as file:
        counter=0
        for line in file: # проходим по файлу и каждую строку форматируем под удобный вывод
            table=[] # Создаем табличку для записи туда одого элемента. для удобства вывода
            counter +=1
            line = str(counter)+";"+line #добавление автоматического номера записи в строку
            table.append(line.split(";"))
            print('| {:2} | {:<10} | {:<10} | {:<15} | {:<12} |'.format(*table[0]))
    print(f"Всего в справочнике {counter} записей")
    input('Нажмите любую клавишу для возврата в меню.')    


def ask_data(): # функция опроса данных на ввод
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    
    
    phone = input('Введите номер телефона: ')
    contact = {
    'second_name': s_name,
    'first_name': f_name,
    'middle_name': m_name,
    'phon_number': phone
                }
    return contact
            
            
def find_contact(FindFild,key):  #поиск контакта по фамилии учитывается регистр
    title = ["№ ","Фамилия","Имя","Отчество","Телефон"]
    print('| {:2} | {:<10} | {:<10} | {:<15} | {:<12} |'.format(*title))
    print('-----------------------------------------------------------------')
    
    with open('phonebook.txt', 'r', encoding="utf8") as file:
        counter=0
        result = 0
        for line in file: # проходим по файлу и каждую строку форматируем под удобный вывод
            table=[] # Создаем табличку для записи туда одого элемента. для удобства вывода
            counter +=1
            line = str(counter)+";"+line #добавление автоматического номера записи в строку
            table.append(line.split(";"))
            if FindFild in table[0][key]: #
                print('| {:2} | {:<10} | {:<10} | {:<15} | {:<12} |'.format(*table[0]))
                result +=1
    print(f'Найдено {result} записей.')
    
            

def export_contact(): # Функция экспорта контакта
    print('''
        Необходимо найти запись которую нужно экспортировать.
        Введите номер критерия поиска записи (Учитывается регистр):
            0 - по номеру записи
            1 - Поиск по фамилии
            2 - Поиск по имени
            3 - Поиск по номеру телефона без "-" и пробелов      
            ''')
    key = int(input())
    find_contact(input('Введите что нужно найти: '),key)
    exp_ID = 0
    exp_ID = int(input('Введите номер записи которую нужно экспортировать '))

    with open('phonebook.txt', 'r', encoding="utf8") as file: # Запись в таблицу всего файла
            counter=0
            for line in file:
                if counter == exp_ID-1:
                    with open('export.txt', 'a', encoding="utf8") as export:
                        export.write(line)
                        break
                counter+=1
    print("Запись экспортирована в файл")

def delete_contact():
    print('''
        Необходимо найти запись которую нужно удалить.
        Введите номер критерия поиска записи (Учитывается регистр):
            0 - по номеру записи
            1 - Поиск по фамилии
            2 - Поиск по имени
            3 - Поиск по номеру телефона без "-" и пробелов      
            ''')
    key = int(input())
    find_contact(input('Введите что нужно найти: '),key)
    del_ID = 0
    del_ID = int(input('Введите номер записи которую нужно удалить '))
    if del_ID !=0:
        table1=[]
        with open('phonebook.txt', 'r', encoding="utf8") as file: # Запись в таблицу всего файла
            for line in file:
                table1.append(line)
        with open('phonebook.txt', 'w', encoding="utf8") as file: # Перезапись файла без выбранной записи
            for i in range(len(table1)):
                if del_ID-1 != i:
                    file.write(table1[i])
        print(f'Запись под номером {del_ID} удалена') 



# add_new_contact(contact)

def main():
    choice =1
    while choice!=0:
        print('''
Введите что выхотите сдлеать:
    1 Найти
    2 добавить
    3 Удалить
    4 открыть
    5 Экспорт контакта в отдельный файл
    0 выход ''')
        choice = int(input('напишите номер пункта > '))
        if choice == 2:
            add_new_contact()
        elif choice == 4:
            open_contact()
        elif choice == 1: # Поиск записи по выбранному пункту
            print('''
        Введите номер критерия поиска записи (Учитывается регистр):
            0 - по номеру записи
            1 - Поиск по фамилии
            2 - Поиск по имени
            3 - Поиск по номеру телефона без "-" и пробелов      
            ''')
            key = int(input())
            find_contact(str(input('Введите что нужно найти: ')),key)
        elif choice ==3:
            delete_contact()
        elif choice ==5:
            export_contact()
        
        elif choice == 0 or choice == '':
            break

        input("Нажмите любую клавишу для возврата в меню")
    
        


main()
# print(contact)