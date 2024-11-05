
# CPU Benchmarking Script

## Descripción
Este script realiza un benchmark de la CPU estresando todos los núcleos mediante cálculos matemáticos realizados en paralelo. Está diseñado para medir el rendimiento de la CPU al ejecutar una serie de operaciones repetitivas y calcular un tiempo promedio de ejecución.

El script utiliza múltiples procesos para estresar todos los núcleos de la CPU, midiendo cuánto tiempo tarda en realizar una cierta cantidad de cálculos de manera repetitiva.

## Requisitos

Para ejecutar el script, asegúrate de tener Python instalado y también de contar con todas las librerías necesarias. Puedes instalarlas ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Librerías utilizadas
- `time`: Para medir el tiempo de ejecución del benchmark.
- `platform`: Para obtener información sobre el sistema operativo.
- `cpuinfo`: Para obtener información detallada de la CPU (`pip install py-cpuinfo`).
- `multiprocessing`: Para ejecutar múltiples procesos en paralelo y estresar todos los núcleos de la CPU.
- `math`: Para realizar los cálculos matemáticos utilizados durante el benchmark.
- `argparse`: Para aceptar argumentos desde la línea de comandos.

## Cómo usar el script

### Ejecución Básica
Para ejecutar el script con los valores predeterminados (10000 cálculos por iteración y 10 repeticiones), simplemente ejecuta el script de la siguiente manera:

```bash
python cpu_benchmark.py
```

### Parámetros Personalizados
Puedes modificar la cantidad de cálculos a realizar y el número de veces que se repite el benchmark utilizando los siguientes parámetros:

- `-c` o `--calculations`: La cantidad de cálculos que se realizarán en cada iteración del benchmark. (Por defecto: 10000)
- `-r` o `--repetitions`: La cantidad de veces que se repetirá el benchmark. (Por defecto: 10)

Por ejemplo, para realizar 20000 cálculos por iteración y repetir el benchmark 5 veces, puedes ejecutar:

```bash
python cpu_benchmark.py -c 20000 -r 5
```

## Ejemplo de Salida
Al ejecutar el script, obtendrás una salida similar a la siguiente, que muestra la información de la CPU y el tiempo de ejecución de cada iteración:

```
CPU: Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz
CPU Thread Count: 12
CPU Arch: X86_64
OS: Windows
Python Ver: 3.8.10

Benchmarking...
1. Execution time: 4.567s
2. Execution time: 4.321s
...
10. Execution time: 4.876s

Average execution time (From 10 attempts): 4.586s
```

## Autor
- **David Jimenez Mora** - Contacto: [d.jimenezm2@uniandes.edu.co](mailto:d.jimenezm2@uniandes.edu.co)

## Notas
- Este script está diseñado para fines de prueba y benchmarking. Ten en cuenta que realizar cálculos intensivos puede estresar tu CPU y generar calor, por lo que no es recomendable ejecutarlo repetitivamente sin pausas.
- Asegúrate de tener una adecuada refrigeración en tu computadora si planeas realizar benchmarks extensivos.