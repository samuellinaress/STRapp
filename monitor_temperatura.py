import threading
import time
import random
import pyodbc

# Conexión a SQL Server
conexion = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=LAPTOP-0H8B2SAT\\SQLEXPRESS;"
    "DATABASE=STR_App;"
    "Trusted_Connection=yes;"
)

cursor = conexion.cursor()

# Lock para concurrencia
mutex = threading.Lock()

UMBRAL = 70


def guardar_temperatura(valor):
    try:
        estado = "CRITICA" if valor > UMBRAL else "NORMAL"

        with mutex:  # evita conflictos concurrentes
            cursor.execute(
                "INSERT INTO Temperaturas (Valor, Estado) VALUES (?, ?)",
                valor, estado
            )
            conexion.commit()

        print(f"Guardado en DB: {valor}°C - {estado}")

    except Exception as e:
        print("Error al guardar en la base de datos:", e)


def generar_temperatura():
    while True:
        temp = random.randint(20, 100)
        print(f"Temperatura generada: {temp}")

        guardar_temperatura(temp)

        time.sleep(2)


# Simular concurrencia con múltiples hilos
hilos = []

for i in range(3):  # 3 sensores simulados
    hilo = threading.Thread(target=generar_temperatura)
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()