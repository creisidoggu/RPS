# Práctica Agentes Inteligentes

## 1. Especificación del entorno de tareas


| Observable       | Agentes       | Determinista       | Episódico       | Estático       | Discreto       | Conocido       |
|------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| Parcial | Multiagente | Estocástico | Secuencial | Estático | Discreto | Conocido |

- __Parcialmente observable__, ya que el agente no tiene un acceso total al estado del entorno ya que no se le muestra lo que el jugador va a sacar antes de sacarlo.

- __Multiagente__, porque el agente jugando al RPS es un entorno competitivo de dos agentes en el que uno es el modelo y el otro es su contrincante a batir.

- __Estocástico__, ya que no hay un siguiente estado del entorno al realizar la primera acción.

- __Secuencial__, ya que la decisión que se tome en esta modificará la siguiente decisión del agente puesto que recopilará los datos de las partidas.

- __Estático__, ya que no hay cambios ni en el entorno ni en la decisión del agente.

- __Discreto__, ya que el estado del entorno y la manera en la que el tiempo es manejado se basa de manera no continua ya que es un juego por turnos.

- __Conocido__, ya que el entorno es unica y exclusivamente el RPS y nada más.

## 2. Identificación del tipo de agente y estructura

El modelo a utilizar es considerado un Agente reactivo basado en modelos ya que para jugar utiliza información previamente recopilada para sus decisiones futuras.

![Agente basado en modelos](/doc/modelo.png)

1. __player_data__ es un archivo json en el que el agente recopila información de los anteriores estados de la partida haciendo una suma de las veces que usó cada opción.

2. __load_save_data__ y __write_save_data__ son funciones para acceder y escribir sobre ese archivo __player_data__ haciendo así la memoria del agente inteligente.

3. __asses_game__ es la función de condición del estado de la partida para los agentes haciendo que se pueda ganar, perder o empatar dependiendo de la opción elegida.

4. __get_computer_action__ es la función condición que decide la acción que usará el agente, en caso de que no haya datos guardados usará random la primera vez y en base a las siguientes veces irá recopilando datos que luego se guardarán en la memoria.

## 3. Ampliación de RPS+ls

Añadida la funcionalidad de Lagarto [3] y Spock [4], además de un menú de selección previo para seleccionar la modalidad a jugar