# Ejercicio 1 
| Actividad | Desempeño | Entorno | Actuadores | Sensores |
| --------- | --------- | ------- | ---------- | -------- |
| Jugar al CS | puntuacion obtenida al final de la partida, basada en factores como victorias, eliminaciones y objetivos alcanzados | mapa 3d, armas, municiones | teclado, mouse, apuntar, disparar | posicion del jugador, enemigos, aliados, estado de los objetos y condiciones del mapa |
| Explorar los oceanos | Completar la exploracion sin incidentes y de manera eficiente | geografia mjundo marino, corrientes y la vida marina | motores, sistemas de propulsion para moverse y ajustar la direccion | radares, camaras, y sensores que capturan los movimientos de la vida marina |
| Comprar y vender tokens crypto | exactitud en la ejecucion de las ordenes de compra y venta deseadas | plataformas mediante las cuales se compran y venden los tokens, oferta y demanda | botones y graficos que muestran la compra y la venta | cambios significativos en los precios, datos y analisis para predecir futuros moimientos del mercado |
| Practicar tenias contra una pared | mantener el rendimiento durante el tiempo de practica sin perder calidad | pared, pelota de tenis | raqueta de tenis, cuerpo de la persona para realizar los movimientos | respuesta de la pelota al impacto contra la pared |
| Realizar un salto de altura | altura, tecnica y eficiencia | zona del salto | movimiento de la persona a saltar, entrenamiento y preparacion previa | equipos que miden la altura obtenida |
| Pujar por un articulo en la subasta | estrategia utilizada, rapidez con la que se realiza la puja | evento donde se realiza la subasta | online o en persona, ofrecer dinero | datos de las ofertas realizadas por otra persona |

## a) Jugar al CS (o cualquier otro 3d Shooter).
# Propiedades

- Parcialmente observable: El jugador solo puede ver lo que está en su campo de visión.
- Multi-agente: Permite la interacción con otros jugadores.
Estocástico: Las acciones de otros agentes y ciertos eventos pueden ser impredecibles.
- Secuencial: Cada acción depende de las anteriores.
- Dinámico: El entorno cambia constantemente.
- Continuo: Movimiento fluido en el espacio de juego.
- Conocido: Las reglas y el entorno son conocidos.

## b) Explorar los océanos
# Propiedades

Parcialmente observable: La visibilidad es limitada.
Agente simple: Si solo se explora sin interactuar con otros agentes.
Estocástico: Factores ambientales como corrientes marinas y condiciones meteorológicas son impredecibles.
Secuencial: Las decisiones afectan las acciones subsiguientes.
Dinámico: Cambios en el entorno por movimiento de animales o condiciones ambientales.
Continuo: Movimiento continuo en el agua.
Desconocido: Exploración de nuevos lugares sin información previa detallada.

## c) Comprar y vender tokens crypto (alguno).
# Propiedades

- Parcialmente observable: Solo se conoce información pública, mientras que factores internos de cada token pueden no ser visibles.
- Multi-agente: Competencia con otros compradores y vendedores.
- Estocástico: Los precios fluctúan de forma impredecible.
- Secuencial: Las decisiones afectan las ganancias/perdidas futuras.
- Dinámico: Cambios constantes en los precios de los tokens.
- Discreto: Las acciones (compra/venta) son discretas.
- Conocido: El funcionamiento del mercado y las reglas son conocidas.

## d) Practicar tenis contra una pared.
# Propiedades

- Totalmente observable: Todo el entorno es visible.
- Agente simple: Solo participa el jugador.
- Determinista: El rebote depende solo del ángulo y velocidad del golpe.
- Secuencial: Cada golpe depende de la posición actual.
- Dinámico: La pelota está en movimiento constante.
- Continuo: Movimiento continuo de la pelota.
- Conocido: Se conocen las reglas y el comportamiento de la pelota.

## e) Realizar un salto de altura.
# Propiedades

- Totalmente observable: El entorno es completamente visible.
- Agente simple: Solo el atleta participa en la acción.
- Determinista: El resultado depende de la técnica y fuerza del atleta.
- Episódico: Cada salto es una acción independiente.
- Estático: El entorno no cambia durante el salto.
- Continuo: Movimiento fluido y continuo.
- Conocido: Las reglas y condiciones son conocidas.



