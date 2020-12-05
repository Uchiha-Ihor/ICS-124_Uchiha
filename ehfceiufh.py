"""Головний модуль задачі
1 Виводить розрахунковую таблицу на некран та в файле
2 Виводить первинні данные на екран
"""

импорт  ОС
from  process_data  import  dohid_val
from  data_service  import  show_dovidnyks , show_tovaroobigs , get_dovidnyk , get_tovaroobig

MAIN_MENU  = \
""" 
~~~~~~~~~~ РОЗРАХУНОК ВАЛОВОГО ДОХОДУ УНІВЕРМАГУ ~~~~~~~~~
1 - Вивід таблиці валового дохода універмагу на екран
2 - Запис таблиці валового дохода універмагу в файл
3 - Вивід списка товарообігу універмагу
4 - Вивід списка довідника товарных груп
0 - Завершення роботи
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~
"""

TITLE  =  "ВАЛОВИЙ ДОХІД УНІВЕРМАГУ НА ЙПОТОЧНИ РІК"

ЗАГОЛОВОК  = \
"""
-------------------------------------------------- -------------------------------------------------- -------------
Найменування | Рік | Товарообіг, тис.грн. | Торгова | Валовий дохід, тис.грн.
товарної групи | | План | Очіковане виконання | знижка,% | План | Очіковане виконання
-------------------------------------------------- -------------------------------------------------- -------------
"""

ФУТЕР  =   \
'''
-------------------------------------------------- -------------------------------------------------- -------------
'''

STOP_MESSAGE  =  'Для продовження натисніть <Enter>'

def  show_dohid ( dohid_list ):
    "" "Виводить таблицю валового доходау
    Аргументы:
        dohid_list ([type]): Список доходу
    "" "
    print ( f " \ n \ n { НАЗВАНИЕ : ^ 113 } " )
    печать ( ЗАГОЛОВОК )

    для  dohid  в  dohid_list :
        print ( f " { dohid [ 'tovar_name' ]: 20 } " ,
              f " { dohid [ 'год' ]: ^ 9 } " ,
              f " { dohid [ 'plan1' ]: ^ 10 } " ,
              f " { dohid [ 'ochikyeme_vukonanya1' ]: ^ 23 } " ,
              f " { dohid [ 'znijka' ]: ^ 13 } " ,
              f " { dohid [ 'plan2' ]: ^ 10 } " ,
              f " { dohid [ 'ochikyeme_vukonanya2' ]: ^ 21 } " )

    печать ( ФУТЕР )

def  write_dohid ( dohid_list ):
    """Записує список валового дохода у текстовий файл
    Аргументы:
        dohid_list ([type]): список доходу
    """

    с  open ( './data/dohid.txt' , 'w' , encoding = "utf8" ) как  dohid_file :
        для  dohid  в  dohid_list :
            line  = \
               dohid [ 'tovar_name' ]                 +  ';'  +       \
               str ( dohid [ 'год' ])                  +  ';'  +       \
               str ( dohid [ 'plan1' ])                 +  ';'  +       \
               str ( dohid [ 'ochikyeme_vukonanya1' ]) +  ';'  +       \
               str ( dohid [ 'znijka' ])                +  ';'  +       \
               str ( dohid [ 'plan2' ])                 +  ';'  +       \
               str ( dohid [ 'ochikyeme_vukonanya2' ]) +  ' \ n ' 
               
            dohid_file . написать ( строка )  
            
    print ( 'Файл успішно записано ...' )     

в то время как  True :

    # Виводить головне меню
    os . система ( 'cls' )
    печать ( MAIN_MENU )
    command_number  =  input ( "Введіть номер команди:" )

    # Обробка команд користувача
    если  command_number  ==  '0' :
        print ( 'Програма завершила роботу' )
        выход ( 0 )

    elif  command_number  ==  '1' :
        dohid_list  =  dohid_val ()
        show_dohid ( dohid_list )
        ввод ( STOP_MESSAGE )

    elif  command_number  ==  '2' :
        dohid_list  =  dohid_val ()
        write_dohid ( dohid_list )
        ввод ( STOP_MESSAGE )
        
    elif  command_number  ==  '3' :
        tovaroobigs  =  get_tovaroobig ()
        show_tovaroobigs ( tovaroobigs )
        ввод ( STOP_MESSAGE )
        
    elif  command_number  ==  '4' :
        dovidnyks  =  get_dovidnyk ()
        show_dovidnyks ( довидныки )
        ввод ( STOP_MESSAGE )