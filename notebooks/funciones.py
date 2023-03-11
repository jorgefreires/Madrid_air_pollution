import warnings
import pyarrow
import pandas as pd
from tqdm import tqdm
import funciones as f

def limpieza(lista):

    try:

        dfs = []

        for e in tqdm(lista):

            # Se importa el archivo

            df = pd.read_csv(f'../../../../../../../../Volumes/JFreire/Databases/trafic_mad/{e}', sep=';')

            # Realmente solo me interesan las columnas fecha, y intensidad. Se borra el resto

            try: 
                
                df = df[['fecha', 'intensidad']]

                # Lo que se quiere es tener la media de intensidad del tráifco en toda la ciudad

                df = df.groupby(['fecha']).mean()

                df.reset_index(inplace=True)

                # Se añade el df a la lista para su posterior concatenación

                dfs.append(df)
            
            except: 

                # Hay un csv con el separador ',' en vez de ';'
                
                df = pd.read_csv(f'../../../../../../../../Volumes/JFreire/Databases/trafic_mad/{e}', sep=',')
                
                df = df[['fecha', 'intensidad']]

                df = df.groupby(['fecha']).mean()

                df.reset_index(inplace=True)

                dfs.append(df)


    except:

        warnings.warn('No se ha podido importar el archivo')

        print(e)

    return dfs
