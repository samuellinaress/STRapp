import time
import random

# Umbral máximo permitido
UMBRAL_TEMPERATURA = 38.0

def leer_temperatura():
    """
    Simula la lectura de un sensor de temperatura
    """
    return random.uniform(35.0, 42.0)

def evaluar_temperatura(temperatura):
    """
    Evalúa si la temperatura supera el umbral
    """
    if temperatura > UMBRAL_TEMPERATURA:
        return True
    return False

def mostrar_alerta(temperatura):
    """
    Muestra una alerta cuando la temperatura es crítica
    """
    print(f"ALERTA: Temperatura elevada ({temperatura:.2f} °C)")

def mostrar_temperatura(temperatura):
    """
    Muestra la temperatura actual
    """
    print(f"Temperatura actual: {temperatura:.2f} °C")

def iniciar_monitoreo():
    """
    Ciclo principal de monitoreo en tiempo real
    """
    print("Sistema de monitoreo iniciado...\n")

    while True:
        temperatura = leer_temperatura()
        mostrar_temperatura(temperatura)

        if evaluar_temperatura(temperatura):
            mostrar_alerta(temperatura)

        time.sleep(1)  # Intervalo de tiempo (1 segundo)

# Inicio del sistema
iniciar_monitoreo()
