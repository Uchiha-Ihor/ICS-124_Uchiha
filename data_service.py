def get_dovidnik():
    """ Повертає вміст файла "dovidniks.txt" у вигляді списка
    Returns:
        dovidnik_list - список рядків файла
    """

    with open('./Data/dovidnik.txt', encoding="utf8") as dovidnik_file:
        dovidnik_list = dovidnik_file.readlines()

    # Накопичувач довідника основних засобів
    dovidnik_drive = []

    for line in dovidnik_list:
        line_list = line.split(';')
        line_list[4] = line_list[4][:-1]  # Видаляє '\n' в кінці
        dovidnik_drive.append(line_list)


    return dovidnik_drive


def show_dovidniks(dovidniks):
    """ Виводить список довідника
    Args:
        dovidniks (list): список довідника
    """

    # Задати інтервал виводу
    dovidnik_code_from = input("З якого кода довідника виводити?")
    dovidnik_code_to = input("По який код довідника виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for dovidnik in dovidniks:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print('Дата: {:3} Код: {:10} Ціна Картоплі: {:20} Ціна Капусти: {:32} Ціна Цибулі: {:45}'.format(dovidnik[0], dovidnik[1], dovidnik[2], dovidnik[3] ,dovidnik[4]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту довідникіка нічого не знайдено.")


dovidniks = get_dovidnik()
show_dovidniks(dovidniks)

def get_Analiz():
    """ Повертає вміст файла "Analizs.txt" у вигляді списка
    Returns:
        Analiz_list - список рядків файла
    """

    with open('./Data/Analiz.txt', encoding="utf8") as Analiz_file:
        Analiz_list = Analiz_file.readlines()

    # Накопичувач руху основних засобів
    Analiz_drive = []

    for line in Analiz_list:
        line_list = line.split(';')
        line_list[6] = line_list[6][:-1]  # Видаляє '\n' в кінці
        Analiz_drive.append(line_list)


    return Analiz_drive


def show_Analizs(Analizs):
    """ Виводить список руху основних засобів
    Args:
        Analizs (list): список руху основних засобів
    """

    # Задати інтервал виводу
    Analiz_code_from = input("З якого кода виду товарів виводити?")
    Analiz_code_to = input("По який код виду товарів виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for Analiz in Analizs:
        if Analiz_code_from <= Analiz[0] <= Analiz_code_to:
            print(" Код: {:3} Найменування ринку: {:20} Дата: {:10} Ціна Картоплі: {:30} Ціна Капусти: {:40} Ціна Цибулі: {:50} Середня ціна: {:60} ".format(Analiz[0], Analiz[1], Analiz[2], Analiz[3], Analiz[4], Analiz[5], Analiz[6]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту товарів не знайдено.")

Analizs = get_Analiz()
show_Analizs(Analizs)
