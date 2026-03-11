import threading
import time
import random

# -------------------------------
# VARIABLES GLOBALES DEL SISTEMA
# -------------------------------

# Semáforo que sincroniza productor y consumidor
sem_temperatura = threading.Semaphore(0)

# Lock para proteger el acceso a la variable compartida
mutex = threading.Lock()

# Variable compartida donde se almacena la temperatura
temperatura_actual = 0

# Umbral de temperatura peligrosa
UMBRAL_TEMPERATURA = 70


# --------------------------------------------------
# FUNCIÓN RECURSIVA PARA VALIDAR TEMPERATURA CRÍTICA
# --------------------------------------------------

def verificar_temperatura(temp, intentos=3):
    """
    Esta función utiliza recursividad para verificar si una temperatura
    es crítica. Si la temperatura es muy alta, se vuelve a evaluar
    simulando una segunda verificación del sensor.
    """

    if intentos == 0:
        return temp

    if temp > UMBRAL_TEMPERATURA:
        print("Verificando nuevamente la temperatura...")

        # Simulación de una nueva lectura del sensor
        nueva_temp = random.randint(20, 100)

        return verificar_temperatura(nueva_temp, intentos - 1)

    return temp


# ----------------------------------
# HILO PRODUCTOR (LECTURA DEL SENSOR)
# ----------------------------------

def leer_temperatura():
    """
    Este hilo simula la lectura de temperatura desde un sensor.
    Genera valores aleatorios y los guarda en una variable compartida.
    Luego libera el semáforo para indicar que hay un nuevo dato disponible.
    """

    global temperatura_actual

    while True:
        try:
            temp = random.randint(20, 100)

            with mutex:
                temperatura_actual = temp

            print(f"[PRODUCTOR] Temperatura leída: {temp} °C")

            # Señal para el consumidor
            sem_temperatura.release()

            time.sleep(2)

        except Exception as e:
            print("Error al leer la temperatura:", e)


# ----------------------------------
# HILO CONSUMIDOR (PROCESA LOS DATOS)
# ----------------------------------

def procesar_temperatura():
    """
    Este hilo espera a que el productor genere una temperatura.
    Cuando recibe la señal del semáforo, procesa el dato.
    """

    global temperatura_actual

    while True:
        try:
            # Espera señal del productor
            sem_temperatura.acquire()

            with mutex:
                temp = temperatura_actual

            # Verificación recursiva
            temp_validada = verificar_temperatura(temp)

            if temp_validada > UMBRAL_TEMPERATURA:
                print("ALERTA: Temperatura crítica detectada")
            else:
                print("[CONSUMIDOR] Temperatura dentro del rango normal")

        except Exception as e:
            print("Error al procesar la temperatura:", e)


# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------

try:
    print("Sistema de Monitoreo de Temperatura iniciado...\n")

    # Creación de hilos
    hilo_productor = threading.Thread(target=leer_temperatura)
    hilo_consumidor = threading.Thread(target=procesar_temperatura)

    # Inicio de los hilos
    hilo_productor.start()
    hilo_consumidor.start()

    # Mantener ejecución
    hilo_productor.join()
    hilo_consumidor.join()

except Exception as e:
    print("Error al iniciar el sistema:", e)