# Snake Game using Turtle Graphics

This is a simple implementation of the classic Snake Game using Python's Turtle graphics module and inheritance. The game is created with object-oriented programming principles, utilizing inheritance to create distinct classes for different game elements.

## How to Play
1. Run the `main.py` file.
2. Use the arrow keys to control the snake.
3. Eat the food (blue dot) to grow longer.
4. Avoid running into the walls or into the snake itself.

## Files
- `main.py`: Main Python script to run the game.
- `snake.py`: Contains the Snake class and its methods.
- `food.py`: Contains the Food class for generating food.
- `score_board.py`: Contains the ScoreBoard class for managing the score.

## Class Descriptions
1. **Snake**: Represents the snake object in the game. It inherits from the `Turtle` class and contains methods to control the snake's movement and growth.
2. **Food**: Represents the food object in the game. It inherits from the `Turtle` class and contains methods to generate food at random locations.
3. **ScoreBoard**: Represents the score board in the game. It manages the score and updates it as the snake eats food.

## How Inheritance is Used
- The `Snake` and `Food` classes both inherit from the `Turtle` class to utilize its functionality for drawing shapes and moving on the screen.
- Inheritance allows us to create specialized classes (`Snake` and `Food`) with their own unique behaviors while reusing code from the `Turtle` class.

## Future Improvements
- Implement advanced game mechanics.
- Add levels of difficulty.
- Enhance graphics and user interface.

Feel free to contribute to the project and make it even better!

## Author
[Luis Leon / LuisLeon-Dev]


