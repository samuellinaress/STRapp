import threading
import time
import random

# Umbral de temperatura
UMBRAL_TEMPERATURA = 38.0

# Variable compartida
temperatura_actual = None

# Semáforo: indica si hay una temperatura disponible
sem_temperatura = threading.Semaphore(0)

# Mutex para proteger la variable compartida
mutex = threading.Lock()


def leer_temperatura():
    """
    Simula la lectura del sensor de temperatura
    """
    return random.uniform(35.0, 42.0)


def hebra_productora():
    """
    Hebra productora: lee la temperatura
    """
    global temperatura_actual

    while True:
        time.sleep(1)

        temp = leer_temperatura()

        with mutex:
            temperatura_actual = temp
            print(f"[Productor] Temperatura leída: {temp:.2f} °C")

        # signal (sem_post)
        sem_temperatura.release()


def hebra_consumidora():
    """
    Hebra consumidora: procesa la temperatura
    """
    global temperatura_actual

    while True:
        # wait (sem_wait)
        sem_temperatura.acquire()

        with mutex:
            temp = temperatura_actual

        print(f"[Consumidor] Procesando temperatura: {temp:.2f} °C")

        if temp > UMBRAL_TEMPERATURA:
            print(f"ALERTA: Temperatura elevada ({temp:.2f} °C)")


# Programa principal
print("Sistema de monitoreo en tiempo real iniciado...\n")

productor = threading.Thread(target=hebra_productora)
consumidor = threading.Thread(target=hebra_consumidora)

productor.start()
consumidor.start()
