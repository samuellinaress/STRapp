import threading
import time
import random

# Semáforo
sem_temperatura = threading.Semaphore(0)

# Lock para proteger la variable compartida
mutex = threading.Lock()

temperatura_actual = 0


# Hilo productor: simula lectura de temperatura
def leer_temperatura():
    global temperatura_actual

    while True:
        try:
            temp = random.randint(20, 100)

            with mutex:
                temperatura_actual = temp

            print(f"Temperatura leída: {temp} °C")

            # Señal al consumidor
            sem_temperatura.release()

            time.sleep(2)

        except Exception as e:
            print("Error al leer la temperatura:", e)


# Hilo consumidor: procesa la temperatura
def procesar_temperatura():
    global temperatura_actual

    while True:
        try:
            # Espera señal del productor
            sem_temperatura.acquire()

            with mutex:
                temp = temperatura_actual

            if temp > 70:
                print("ALERTA: Temperatura alta")
            else:
                print("Temperatura normal")

        except Exception as e:
            print("Error al procesar la temperatura:", e)


try:
    #raise Exception("Error simulado en el sistema")
    # Crear hilos
    hilo_productor = threading.Thread(target=leer_temperatura)
    hilo_consumidor = threading.Thread(target=procesar_temperatura)

    # Iniciar hilos
    hilo_productor.start()
    hilo_consumidor.start()

    # Esperar a que terminen
    hilo_productor.join()
    hilo_consumidor.join()

except Exception as e:
    print("Error al iniciar el sistema:", e)