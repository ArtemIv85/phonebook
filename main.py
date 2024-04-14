import functions as func
import os


def main():
    choice =1
    
    while choice!=0:
        os.system('CLS')  # Отчистка Терминала
        print(
'''Введите что выхотите сдлеать:
    1 - Найти
    2 - Добавить
    3 - Удалить
    4 - Открыть
    5 - Экспорт контакта в отдельный файл
    0 - Выход ''')
        choice = int(input('напишите номер пункта > '))
        if choice == 2:
            func.add_new_contact()
        elif choice == 4:
            func.open_contact()
        elif choice == 1: # Поиск записи по выбранному пункту
            print('''
        Введите номер критерия поиска записи (Учитывается регистр):
            0 - по номеру записи
            1 - Поиск по фамилии
            2 - Поиск по имени
            3 - Поиск по номеру телефона без "-" и пробелов      
            ''')
            key = int(input('Введите номер пункта > '))
            func.find_contact(str(input('Введите что нужно найти: ')),key)
        elif choice ==3:
            func.delete_contact()
        elif choice ==5:
            func.export_contact()
        
        elif choice == 0 or choice == '':
            break

        input("Нажмите любую клавишу для возврата в меню")
    
        


main()
