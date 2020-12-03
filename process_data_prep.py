""" Аналіз руху основних засобів
"""

# Підключити функції з модуля 'data_service'
from data_service import get_dovidnik, get_Analiz

# Структура аналізу руху основних засобів вихідних даних
Analiz_rinky = {
    'Kod_rinky'      : '',
    'Name_rinky'     : '',
    'Data'           : '',
    'Price_kartopla' : 0.0,
    'Price_kapusta'  : 0.0,
    'Price_zebula'   : 0.0,
    'Middle_price'   : 0.0
}


dovidniks = get_dovidnik()
Analizs = get_Analiz()

def Analiz_rinky_means():
    """ Формування аналізу руху основних засобів
    """

    def get_analiz_name(Analiz_code):
        """ Повертає назву засоба по його коду
        Args:
            Analiz_name ([type]): код засоба
        Returns:
            [type]: назва засобу
        """

        for Analiz in Analizs:
            if Analiz[0] == Analiz_code:
                return Analiz[1]

        return "*** Код засобу не знайдений"

    # Накопичувач аналізу руху основних засобів
    Analiz_rinky_list = []

    for dovidnik in dovidniks:
        Analiz_rinky_tmp = Analiz_rinky.copy()
        
        Analiz_rinky_tmp['Kod_rinky']        = dovidnik[1] 
        Analiz_rinky_tmp['Name_rinky']       = dovidnik[2]
        Analiz_rinky_tmp['Data']             = dovidnik[3] 
        Analiz_rinky_tmp['Price_kartopla']   = dovidnik[4] 
        Analiz_rinky_tmp['Price_kapusta']    = dovidnik[5] 
        Analiz_rinky_tmp['Price_zebula']     = dovidnik[6] 
        Analiz_rinky_tmp['Middle_price']     = (Analiz_rinky_tmp['Price_kartopla'] + Analiz_rinky_tmp['Price_kapusta'] + Analiz_rinky_tmp['Price_zebula']) /3
        Analiz_rinky_list.append(Analiz_rinky_tmp)

        Analiz_rinky_list.append(Analiz_rinky_tmp)

    return Analiz_rinky_list

result = Analiz_rinky_means()

for r in result:
    print(r)
