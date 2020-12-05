"""формування заявок на розрахунок валового доходу по магазину
"""
# підключити функції з модуля `data_service`
from data_service import get_dovidnik, get_Analiz

Analiz_rinky = {
    'Kod_rinky'      : '',
    'Name_rinky'     : '',
    'Data'           : '',
    'Price_kartopla' : 0.0,
    'Price_kapusta'  : 0.0,
    'Price_zebula'   : 0.0,
    'summa_produkty' : 0.0,
    'Middle_price'   : 0.0

}

dovidniks = get_dovidnik()
Analizs = get_Analiz()

def Analiz_rinky_means():
    """ Формування валового доходу універмагу
    """

    def get_rinok_name(Analiz_code):
        """ Повертає назву засоба по його коду
        Args:
            dovidnyk_name ([type]): код засоба
        Returns:
            [type]: назва засобу
        """

        for Analiz in Analizs:
            if Analiz[0] == Analiz_code:
                return Analiz[1]

        return "*** Код не знайдений"
    # Накопичувач валового доходу універмагу
    Analiz_rinky_list = []

    for dovidnik in dovidniks:

        # Створити копію шаблона
        Analiz_rinky_tmp = Analiz_rinky.copy()

        Analiz_rinky_tmp['Kod_rinky']        = dovidnik[1] 
        Analiz_rinky_tmp['Name_rinky']       = get_rinok_name(dovidnik[1])
        Analiz_rinky_tmp['Data']             = dovidnik[0] 
        Analiz_rinky_tmp['Price_kartopla']   = dovidnik[2] 
        Analiz_rinky_tmp['Price_kapusta']    = dovidnik[3] 
        Analiz_rinky_tmp['Price_zebula']     = dovidnik[4]
        Analiz_rinky_tmp['summa_produkty']   = float(Analiz_rinky_tmp['Price_kartopla']) + float(Analiz_rinky_tmp['Price_kapusta']) + float(Analiz_rinky_tmp['Price_zebula'])
        Analiz_rinky_tmp['Middle_price']     = float(Analiz_rinky_tmp['summa_produkty']) /3
        Analiz_rinky_list.append(Analiz_rinky_tmp)

    return Analiz_rinky_list

result = Analiz_rinky_means()

for r in result:
    print(r)