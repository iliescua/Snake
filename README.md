# Snake

## How to play
Use the arrow keys to control the snake and have it move around the screen. If the game ends then you can quickly restart it using the spacebar.


### v1.0
This was my first attempt at recreating the classic snake game from scratch. I used the turtles libraray to create the screen that the game is played on as well 
as the components that are used in the snake game such as the food and the scoreboard. From there I made the snake move across the screen and respond to keyboard 
inputs (arrow keys to move) and I implemented detection checks to ensure the game ends if the snake touches the borders or itself. 


### v1.1
Changed the way the game can end, so now when it's over it looks for the user to hit space to restart the game. Also, added the functionality so that now when the 
snake collides with a border it will continue from the other side as if it had wrapped around instead of ending the game.


### v1.2
Added persistance to the game by keeping track of the highest score that a player achieved using files to store the data.
