# Curses and Snake
We will be making the game [Snake](https://en.wikipedia.org/wiki/Snake_(video_game_genre)) using a terminal module called [curses](https://docs.python.org/3/library/curses.html#module-curses). This form of graphics predates vector graphics by many years, but is still immensly powerful.

Many of the concepts you will learn in this lesson will translate easily to any graphics-based application development.

## Design Goal: The Minimum Viable Product
To create a Snake clone that successfully takes player input and translates it into movement of a snake in a curses window. The snake is able to "eat" fruit and grow in length when it does so.

If the Snake touches the edges of the window or runs into itself, the game ends.
### Additional Goals
1. Add a score mechanic with feedback to the player.
2. Make the game loop increase in speed as the snake gets longer.
3. Customize the look and color of the snake and fruit.
4. Add obstacles in the play environment that the snake cannot cross.

## Some helpful links:
1. https://docs.python.org/3/howto/curses.html
2. https://unicode-table.com/en/blocks/
