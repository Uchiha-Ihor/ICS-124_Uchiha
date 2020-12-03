from data_service import get_dovidnik, get_Analiz

analiz_rinky = {
    'Kod_rinky'      : '',
    'Name_rinky'     : '',
    'Data'           : '',
    'Price_kartopla' : 0.0,
    'Price_kapusta'  : 0.0,
    'Price_zebula'   : 0.0,
    'Middle_price'   : 0.0
}

# print(get_dovidnik)
# print(get_Analiz)

dovidnik = get_dovidnik()
analiz = get_Analiz()

def create_analiz_rinky():
    
    def get_client_name(client_code):
        """повертає назву клієнта по його коду

        Args:
            client_code ([type]): код клієнта

        Returns:
            [type]: назва клієнта
        """

        for client in clients:
            if client[0] == client_code:
                return client[1]

        return "*** код клієнта не знайдений"
    analiz_rinky = []
    for dovidnik in dovidniks:
        analiz_rinky_tmp = analiz_rinky.copy()

        analiz_rinky_tmp['Kod_rinky']        = dovidnik[1] 
        analiz_rinky_tmp['Name_rinky']       = dovidnik[2]
        analiz_rinky_tmp['Data']             = dovidnik[3] 
        analiz_rinky_tmp['Price_kartopla']   = dovidnik[4] 
        analiz_rinky_tmp['Price_kapusta']    = dovidnik[5] 
        analiz_rinky_tmp['Price_zebula']     = dovidnik[6] 
        analiz_rinky_tmp['Middle_price']     = (analiz_rinky_tmp['Price_kartopla'] + analiz_rinky_tmp['Price_kapusta'] + analiz_rinky_tmp['Price_zebula']) /3
        analiz_rinky_list.append(analiz_rinky_tmp)
    return analiz_rinky_list
result = create_analiz_rinky()

for r in result:
    print(r)