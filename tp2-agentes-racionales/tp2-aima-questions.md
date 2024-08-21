# Ejercicios AIMA
## 2.10 
###  Consider a modified version of the vacuum environment in Exercise 2.8, in which theagent is penalized one point for each movement.
### a. Can a simple reflex agent be perfectly rational for this environment? Explain.
No, ya que para que un agente sea perfectamente racional siempre evalua todas las posibles acciones y selecciona la que mejor cumple con sus objetivos. Y al ser un agente reflexivo simple va a tomar decisiones basandose solamente en el conocimiento actual, ya que no lleva un historial de las acciones que hizo anteriormente. No tiene memoria de los estados pasados ni la capacidad de aprender de sus experiencias, por lo tanto no podria ser perfectamente racional. 
### b. What about a reflex agent with state? Design such an agent.
Un agente racional con estado es una mejora con respecto a uno reflexivo simple, pero sigue sin tener memoria de los lugares por los que paso, o las acciones que ya hizo, por lo tanto tampoco seria perfectamente racional.
### c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?
Para el caso del agente reflexivo simple, si este puede percibir el estado limpio/sucio de cada cuadro del entorno, su capacidad de ser perfectamente racional podria mejorar significativamente, ya que podria tomar decisiones optimas con base en la imformacion completa del entorno. 
Para el caso del agente reflexivo con estado pasa lo mismo, y por lo tanto, tambien podria ser perfectamente racional.

## 2.11
###  Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)
###  a. Can a simple reflex agent be perfectly rational for this environment? Explain
Como un agente reflexivo simple no tiene memoria de los estados por los que estuvo, no podria ser perfectamente racional. En un entorno donde el espacio es desconocido, no sabemos si habran obstaculos, el agente no tiene suficiente informacion para tomar soluciones optimas. 
### b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments
El rendimiento del agente aleatorio es bastante similar al relfexivo, por lo tanto seria lo mismo, podemos observarlo en los ejercicios 4 y 5.
### c. Can you design an environment in which your randomized agent will perform poorly? Show your results.
Un agente reflexivo con una funcion aleatoria lo mas probable es que tenga un rendimiento pobre, ya que su principal desventaja es la falta de planificacion y la toma de decisiones ineficientes debido a la aletoriedad.
### d.  Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?
Si podria ser que al tener conocimiento de los casilleros que ya visito tenga un mayor rendimiento, pero igualmente no tiene conocimiento total de los casilleros, por lo tanto podria seguir sin tomar las decisiones mas optimas.








