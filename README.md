# pfda_finalProject_GreenwoodBreietta
Simple snake game. The objective is to get the highest score possible by eating apples. Each apple consumed will grow the snake, and once the snake"s head hits a wall or its own body the game is over. Good luck!!🐍

## Demo Video
Youtube Link: <https://youtu.be/ZRZy9JaSUN4>

## GitHub Repository
GitHub Repo: <https://github.com/bxg2022/pfda_finalProject_GreenwoodBreietta.git>

## Project description/features
Snake: The snake is a list object made of segments. The snake has full 2-dimensional movement, with event handling so the snake can't change to its opposite direction. WASD keyboard controls will change the direction of the snake. The snake is capable of colliding with each type of pickup, the walls, and itself. Every 50 points scored will increase the snake's movement speed. 

Apple: The apple spawns at a random position. When the snake eats the apple, the player gains 10 points and the snake grows by 1 segment. As soon as the apple is eaten, it respawns in a new random location.

Special Pickups: There are 2 special pickup types, the golden apple and the speed pickup. Whenever the golden apple is eaten, the player gains 30 points and the snake shrinks by 1 segment. Once eaten, the golden apple will respawn after a 15 second cooldown. The speed pickup doesn't earn the player any points, but it will reduce the snake's speed (with a floor of the game start speed). Once eaten, the speed pickup will respawn after a 5 second cooldown.

Scoring and Highscore: The score updates every time an apple is eaten, and displays on the screen. The highscore is stored and displayed underneath the current score. If the highscore is surpassed, it will be updated and the new highscore will be displayed in future games.

Collision and Game Over: If the snake's head collides with a wall or its own body, the game is over. The final score will be displayed on the screen, and if the highscore is surpassed the game over screen will congradulate you.

Aesthetics: The snake and each pickup type have unique identifying colors. The background is an imported and resized image of a nighttime forest to give the game a cozy environment. The chosen display font reads as if it is handwritten and adds to the atmosphere of the game.

## Sources/Citations
https://www.pygame.org/docs

https://school.nelsonlim.com/path-player?courseid=pfda2026&unit=696fe6f73085a633970f32daUnit

https://www.geeksforgeeks.org/python/snake-game-in-python-using-pygame-module/

https://www.w3tutorials.net/blog/saving-the-highscore-for-a-game/

https://thepythoncode.com/article/make-a-snake-game-with-pygame-in-python