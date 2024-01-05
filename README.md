# Space Invaders

Este proyecto es una implementación simple del clásico juego Space Invaders utilizando la biblioteca Pygame en Python. Space Invaders es un juego de disparos en el que el jugador controla una nave espacial que debe defenderse de oleadas de naves enemigas.

## Contenido del Proyecto

### 1. Configuración de Pantalla
- La pantalla del juego tiene un tamaño de 1280x720 píxeles.
- Se ha establecido un título y un icono personalizado.

### 2. Música de Fondo
- Se ha incorporado una música de fondo que se reproduce de forma continua durante el juego.

### 3. Nave del Jugador
- Se ha creado una nave espacial para el jugador que puede moverse horizontalmente con las teclas 'A' y 'D'.
- El jugador puede disparar con la tecla 'ESPACIO'.

### 4. Naves Enemigas
- Se han creado múltiples naves enemigas que se generan aleatoriamente en la parte superior de la pantalla.
- Las naves enemigas se mueven horizontalmente y descienden cuando alcanzan los bordes de la pantalla.
- Si una nave enemiga colisiona con un disparo del jugador, se destruye, y se incrementa el puntaje del jugador.

### 5. Disparos
- El jugador puede disparar para destruir las naves enemigas.
- Se ha añadido un sonido de disparo al efectuar un disparo.

### 6. Puntaje
- El puntaje del jugador se muestra en la esquina superior izquierda de la pantalla.
- Cada vez que una nave enemiga es destruida, el puntaje se incrementa.

### 7. Fin del Juego
- Si una nave enemiga alcanza la parte inferior de la pantalla, el juego termina y se muestra un mensaje de "Game Over".