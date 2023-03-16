# Análisis de contaminación en la ciudad de Madrid

Este proyecto tiene como objetivo analizar la contaminación en la ciudad de Madrid, para lo que se han utilizado datos proporcionados por el portal del ayuntamiento de Madrid. También se han incluido datos de tráfico para ver si estos explican los distintos contaminantes. La idea principal es ir añadiendo de forma colaborativa nuevos datos sobre factores que pueden afectar a la contaminación, como podrian ser las precipitaciones o el tráfico aéreo, para ver si estos explican los distintos contaminantes.

Cabe recalcar que los datos recopilados son datos por hora entre los años 2015 y 2022. Lo ideal seria que los nuevos datos que se añadan sigan la misma estructura, pero si no es así, se pueden añadir siempre que se haga la conversión correspondiente.

## Estructura del repositorio

El repositorio se divide en tres carpetas:

- **notebooks**: Contiene los notebooks de limpieza de datos, unificación de los datos en un solo archivo, análisis de correlaciones y machine learning. Todos los notebooks están escritos en Python y Jupyter Notebook. Para añadir nuevas variables a los análisis de correlaciones y machine learning, sólo se necesitan pequeños cambios en los notebooks correspondientes. Estos cambios se indican en los comentarios del código.

- **dashboards**: Contiene dashboards creados con los datos del proyecto. Aquí podrás encontrar las visualizaciones realizadas por distintos colaboradores.

- **data**: Esta carpeta no se encuentra en GitHub, sino en una [carpeta de Google Drive](https://drive.google.com/drive/folders/1fWWQiDF09efULgZoP2jMeDJjEEz6GMlW?usp=sharing). Aquí se encuentran los datos originales de contaminación y tráfico utilizados en el proyecto.

## Cómo colaborar

Este proyecto está abierto a la colaboración de cualquier persona interesada en el tema. Si quieres colaborar, aquí te dejamos algunos pasos para empezar:

1. Clona el repositorio en tu ordenador local.

2. Accede al enlace de Google Drive para descargar los datos que necesites. Puedes añadir los datos nuevos que utilices.

3. Limpia los datos y únleos a los ya existentes. Puedes hacerlo en la carpeta de limpieza dentro de notebooks.

4. Añade tus variables a los notebooks de correlaciones y machine learning. Sólo necesitas hacer pequeños cambios en los notebooks correspondientes, que se indican en los comentarios del código.

5. Siéntete libre de realizar las visualizaciones y análisis que quieras en nuevos notebooks.

6. Si realizas algun dashboard, añadelo a la carpeta "dashboards".

7. Haz un pull request para compartir tus cambios con la comunidad.

Sientete libre para, además de incluir nuevos datos, mejorar el código existente. Cualquier mejora será bienvenida.

## Contribuciones

Este proyecto fue iniciado por Jorge Freire Serrano, pero está abierto a la contribución de cualquier persona interesada en el tema. Si tienes alguna idea para mejorar el proyecto o cualquier duda, no dudes en abrir un issue o contactarnos directamente.
