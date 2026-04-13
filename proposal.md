# Title
Snake Game
## Repository
https://github.com/bxg2022/pfda_finalProject_GreenwoodBreietta.git

## Description
A functioning snake game. Relevant to media and digital arts because games combine playing media and consuming art digitally.

## Features
- Game loop
	- init, game loop is a while loop, quit
- Snake character:
    - class snake
	- snake moves on WASD key presses
    - overlap with food will grow snake and increase score
    - overlap with self or walls will end game
- Food: 
	- class food
    - randomize food locations
    - relocate after snake eats food
- Score:
    - tracks score every time snake eats food
    - scoreboard display
    - highscore display (will update when surpassed)
- Display/aesthetics:
    - pygame.Draw

## Challenges
- Further understanding of the Pygame library
- Using the Random library
- Figuring out how to map keys to trigger functionality
- Making the game work (collisions/overlap triggering functions, scoreboard accurately recording, food respawning)

## Outcomes
Ideal Outcome:
- Creating a fully-functioning, aesthetically pleasing, playable snake game.

Minimal Viable Outcome:
- Snake moves around the screen and is visible. Snake consumes food and score goes up. Snake and food look pretty.

## Milestones

- Week 1
  1. Set up the game (init, game loop, quit).
  2. Create menus (main menu, game over menu)
  3. Create snake character and movement function

- Week 2
  1. Implement game functionality/mechanics:
        - Snake: collision with food, snake grows after eating food, collision with self or walls triggers game over
        - Food: randomize food location, new location after eating
  2. Scoreboard: track score (increases with each food consumed), high score will update when surpassed

- Week N (Final)
  1. Design a cool background environment
  2. Design snake and food to look pretty (randomize the type of food)
