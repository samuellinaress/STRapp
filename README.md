# Sistema de Monitoreo de Temperatura en Tiempo Real

## Descripción del Problema

En muchos sistemas industriales es necesario monitorear constantemente la temperatura para detectar condiciones críticas que puedan afectar el funcionamiento de equipos o procesos.

Este proyecto simula un sistema de monitoreo de temperatura en tiempo real utilizando Python.

## Solución Implementada

El sistema utiliza programación concurrente mediante hilos para ejecutar dos procesos al mismo tiempo:

- Un hilo productor que simula la lectura de temperatura desde un sensor.
- Un hilo consumidor que procesa los datos recibidos.

Para sincronizar ambos procesos se utiliza un semáforo.

También se implementa un mecanismo de exclusión mutua mediante un Lock para proteger la variable compartida.

Además, se utiliza una función recursiva para validar temperaturas críticas y simular una segunda verificación del sensor.

## Tecnologías Utilizadas

- Python
- Threading
- Semáforos
- Recursividad

## Funcionamiento

1. El productor genera una temperatura aleatoria.
2. La temperatura se guarda en una variable compartida.
3. El semáforo avisa al consumidor que hay un nuevo dato.
4. El consumidor procesa la temperatura.
5. Si el valor es crítico, se genera una alerta.

## Objetivo del Proyecto

Demostrar el uso de programación concurrente, sincronización mediante semáforos y uso de recursividad en un sistema simple de tiempo real.
