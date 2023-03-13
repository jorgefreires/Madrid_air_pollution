import pandas as pd

def unir(lista_meses):

    # Esta funcion une todos los archivos de original_data en un solo df limpio

    dfs = []

    for e in lista_meses:   

        df = pd.read_csv(f'../original_data/{e}', delimiter=';')
    
        dfs.append(df)

    # Se unen todos los df de los distintos meses en uno solo

    total = pd.concat(dfs, ignore_index=True)

    total.columns = [col.lower() for col in total.columns]   # Se ponen los nombres de las columnas en minúsculas por comodidad

    # Es siempre la misma provincia y municipio y el punto de muestre es redundante pues se tienen datos sobre la estacion, por lo que se borran estos datos

    total.drop(['provincia', 'municipio', 'punto_muestreo'], axis=1, inplace=True)

    '''
    Todas las columnas del estilo v01 muestran si los datos están validados o no. Se borran puesto que hay muy pocos no 
    validados(30 de 3960 para noviembre de 2022) y además se considera que los datos importan aunque no esten validados
    '''

    for e in total.columns:

        if 'v' in e: total.drop([e], axis=1, inplace=True)
        else: pass

    # Las columnas de la hora se cambian por la hora como id del 1 al 24

    total.rename(columns={'h01': '1', 
                          'h02': '2',
                          'h03': '3',
                          'h04': '4',
                          'h05': '5',
                          'h06': '6',
                          'h07': '7',
                          'h08': '8',
                          'h09': '9',
                          'h10': '10',
                          'h11': '11',
                          'h12': '12',
                          'h13': '13',
                          'h14': '14',
                          'h15': '15',
                          'h16': '16',
                          'h17': '17',
                          'h18': '18',
                          'h19': '19',
                          'h20': '20',
                          'h21': '21',
                          'h22': '22',
                          'h23': '23',
                          'h24': '24'
                          }, inplace=True)

    # Se crea una nueva columna idnicando un id para la unidad de medida de cada magniud

    total.insert(2, 'unidad_medida', 0)

    for row in range(len(total)):

        if total.magnitud.iloc[row] == 1: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 6: total.unidad_medida.iloc[row] = 2
        elif total.magnitud.iloc[row] == 7: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 8: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 12: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 9: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 10: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 14: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 20: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 30: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 35: total.unidad_medida.iloc[row] = 1
        else: pass

    return total

def merge(a,b):

    c = pd.merge(a, b, on='fecha')

    return c