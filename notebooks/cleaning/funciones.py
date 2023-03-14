import warnings
import pyarrow
import pandas as pd
from tqdm import tqdm

def limpieza(lista):   # Función usada para la limpieza de los datos de tráfico

    dfs = []

    for e in tqdm(lista):

        try: 

             # Se importa el archivo

            df = pd.read_csv(f'../../../../../../Documents/Databases/trafic_mad/{e}', sep=';', encoding_errors='ignore')

            # Realmente solo me interesan las columnas fecha, y intensidad. Se borra el resto

            df = df[['fecha', 'intensidad']]

            # Lo que se quiere es tener la media de intensidad del tráifco en toda la ciudad

            df = df.groupby(['fecha']).mean()

            df.reset_index(inplace=True)

            # Se añade el df a la lista para su posterior concatenación

            dfs.append(df)
        
        except: 

            # Hay un csv con el separador ',' en vez de ';'
            
            df = pd.read_csv(f'../../../../../../Documents/Databases/trafic_mad/{e}', sep=',', encoding_errors='ignore')
            
            df = df[['fecha', 'intensidad']]

            df = df.groupby(['fecha']).mean()

            df.reset_index(inplace=True)

            dfs.append(df)

    return dfs
