import time
import platform
import cpuinfo  # pip install py-cpuinfo
import multiprocessing
import math
import argparse


def print_info():
    """
    Imprime información sobre el sistema y la CPU.

    Args:
        None

    Returns:
        None
    """

    cpu_info = cpuinfo.get_cpu_info()
    os_version = platform.system()
    print(f"CPU: {cpu_info.get('brand_raw', 'Unknown')}")
    print(f"CPU Thread Count: {cpu_info.get('count', 'Unknown')}")
    print(f"CPU Arch: {cpu_info.get('arch_string_raw', 'Unknown')}")
    print(f"OS: {os_version}")
    print(f"Python Ver: {cpu_info.get('python_version', 'Unknown')}")
    print('\nBenchmarking...')


def benchmark_worker(repeat):
    """
    Realiza los cálculos para estresar la CPU.

    Args:
        repeat (int): Cantidad de cálculos a realizar.

    Returns:
        None
    """

    for i in range(0, repeat):
        for x in range(1, 1000):
            math.pi * 2 ** x

        for x in range(1, 10000):
            float(x) / math.pi

        for x in range(1, 10000):
            float(math.pi) / x

        for x in range(1, 10000):
            math.sin(x) ** math.cos(x)


def benchmark(repeat, repeat_benchmark):
    """
    Inicia el benchmark (Ejecutado en todos los núcleos de la CPU).

    Args:
        repeat (int): Cantidad de cálculos a realizar.
        repeat_benchmark (int): Cantidad de veces que se repetirá el benchmark.

    Returns:
        average_benchmark (float): Tiempo promedio de ejecución.
    """

    average_benchmark = 0
    for iteration in range(0, repeat_benchmark):
        start = time.time()

        # Se crean múltiples procesos para ejecutar los cálculos en paralelo y así estresar todos los núcleos de la CPU.
        processes = []
        num_processes = multiprocessing.cpu_count()

        for _ in range(num_processes):
            process = multiprocessing.Process(target=benchmark_worker, args=(repeat // num_processes,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()
            process.close()

        end = time.time()
        duration = (end - start)
        duration = round(duration, 3)
        average_benchmark += duration

        print(f"{iteration + 1}. Execution time: {duration}s")

    average_benchmark = round(average_benchmark / repeat_benchmark, 3)
    return average_benchmark


if __name__ == "__main__":
    # Parseo de argumentos
    parser = argparse.ArgumentParser(description = 'CPU Benchmarking Script - Estresa la CPU realizando cálculos matemáticos en paralelo.\nRealizado por: David Jimenez - d.jimenezm2@uniandes.edu.co')
    parser.add_argument('-c', '--calculations', type = int, default = 10000, help = 'Cantidad de cálculos a realizar. (Por defecto: 10000)')
    parser.add_argument('-r', '--repetitions', type = int, default = 10, help = 'Cantidad de veces que se repetirá el benchmark. (Por defecto: 10)')

    args = parser.parse_args()

    repeat = args.calculations
    repeat_benchmark = args.repetitions

    print_info()
    average_benchmark = benchmark(repeat, repeat_benchmark)
    print(f"\nAverage execution time (From {repeat_benchmark} attempts): {average_benchmark}s")
