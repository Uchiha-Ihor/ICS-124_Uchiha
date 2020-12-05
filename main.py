""" Головний модуль задачі
- Виводить розрахункову табліцю на екран та в файл
- Виводить первинні данні на екран
"""

import os
from process_data import Analiz_rinky_means
from data_service import show_Analizs, show_dovidniks, get_dovidnik, get_Analiz

MAIN_MENU = \
""" 
~~~~~~~~   ОБРОБКА АНАЛІЗУ РУХУ ОСНОВНИХ ЗАСОБІВ   ~~~~~~~~
1 - Вивід таблиці аналізу засобів на екран
2 - Запис таблиці аналізу засобів в файл
3 - Вивід списка руху основних засобів
4 - Вивід списка довідника основних засобів
0 - Завершення роботи
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

TITLE = "АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ"

HEADER = \
"""
============================================================================================================================================
Код    |    Назва рынку    |    Дата    | Ціна на Картоплю | Ціна на Капусту | Ціна на Цибулю | Середня ціна
============================================================================================================================================
"""

FOOTER =  \
'''
============================================================================================================================================
'''

STOP_MESSAGE = '\n Для продовження натисніть <Enter> '

def show_Analiz_rinky(Analiz_rinky_list):
    """ Виводить таблицю аналізу основних засобів
    Args:
        Analiz_rinky_list ([type]): Список засобів
    """
    print(f"\n\n{TITLE:^141}")
    print(HEADER)

    for Analiz_rinky in Analiz_rinky_list:
        print(f"{Analiz_rinky['Kod_rinky']:10}",
              f"{Analiz_rinky['Name_rinky']:17}",
              f"{Analiz_rinky['Data']:^10}",
              f"{Analiz_rinky['Price_kartopla']:^23}",
              f"{Analiz_rinky['Price_kapusta']:^13}", #поменять на процес дата
              f"{Analiz_rinky['Price_zebula']:^10}",
              f"{Analiz_rinky['Middle_price']:^31}")

    print(FOOTER)

def write_Analiz_rinky(Analiz_rinky_list):
    """ Записує список аналізу у текстовий файл
    Args:
        Analiz_rinky_list ([type]): список аналізу
    """

    with open('./Data/Analiz_rinky.txt', 'w') as Analiz_file:
        for Analiz_rinky in Analiz_rinky_list:
            line = \
               str(Analiz_rinky['Kod_rinky']) + ';' + \
               str(Analiz_rinky['Name_rinky']) + ';' +                        \
               str(Analiz_rinky['Data']) + ';' +                      \
               str(Analiz_rinky['Price_kartopla']) + ';' +       \
               str(Analiz_rinky['Price_kapusta']) + ';' +    \
               str(Analiz_rinky['Price_zebula']) + ';' +      \
               str(Analiz_rinky['Middle_price'])  + '\n' 
               
            Analiz_file.write(line)  
            
    print('\n[INFO]: Файл успішно записано...')     

while True:

    # Виводить головне меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # Обробка команд користувача
    if command_number == '0':
        print('\n[INFO]: Програма завершила роботу\n')
        exit(0)

    elif command_number == '1':
        Analiz_rinky_list = Analiz_rinky_means()
        show_Analiz_rinky(Analiz_rinky_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        Analiz_rinky_list = Analiz_rinky_means()
        write_Analiz_rinky(Analiz_rinky_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        dovidniks = get_dovidnik()
        show_dovidniks(dovidniks)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        Analizs = get_Analiz()
        show_Analizs(Analizs)
        input(STOP_MESSAGE)