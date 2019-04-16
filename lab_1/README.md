### Laboratorio 1: Representación del Conocimiento

Utilizando el entorno de trabajo Gym y el dominio de Sonic de Headhog
Construya un archivo csv o base de datos con 100 millones de registros, donde se converja la matriz que representa el mundo de sonic en una instancia de tiempo, y la acción que realizo el jugador escrita en formato de arreglo de botones del control de sega genesis de 1991 - 1992

## ¿Como?

1. Creen una carpeta llamada lab_1 y dentro de ella ejecutar
virtualenv -p python3 env
source env/bin/activate
pip3 install gym-retro
2. Creen una carpeta llamada roms dentro de lab_1 y colocar el archivo md de sonic. Ejecutar:
python3 -m retro.import roms

3. Colocar el archivo controlador dentro de la carpeta lab_1, y ejecutar
python sonic.py
Si sonic se mueve, entonces ya funciona.

__(Si tiene algun problema puedes importar gym, luego seguir el orden de los paso y la carpeta de gym ponerla dentro de el lab_1)__
