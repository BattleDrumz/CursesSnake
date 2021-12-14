# Code by Luke Thorne
import curses
from random import randint

HEIGHT, WIDTH = 24, 40

# Initialize curses module, window, and settings
curses.initscr()  # Initializes curses
curses.start_color()

curses.curs_set(0) # Hides the terminal cursor
curses.noecho() # Keeps keypresses from printing to console

WIN = curses.newwin(HEIGHT, WIDTH, 0, 0) # y,x
WIN.nodelay(1) # Allows direct keypresses
WIN.keypad(1) # Keypad Mode
WIN.border(0) 

# Variable and Constants Initialization
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

snake = [(7, 10), (7, 9), (7, 8)]
fruit = (HEIGHT // 2, WIDTH // 2) # Fruit starts in center of the screen
score = 0

ESC = 27
W = 119
A = 97
S = 115
D = 100
key = D
direction = "R"
refresh = 100
bombs = []

# Main Gameplay Loop
while key != ESC:
    WIN.addstr(0, 0, "Score: " + str(score) + " " + direction)
    WIN.timeout(refresh)
    event = WIN.getch()

    prev_key = key
    
    key = event if event != -1 else prev_key
    if key not in (curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP,curses.KEY_DOWN, W, A, S, D, ESC):
        key = prev_key

    head_y = snake[0][0]
    head_x = snake[0][1]

    # Player Controller
    if key == D or key == curses.KEY_RIGHT:
        refresh = 100
        head_x += 1
    elif key == A or key == curses.KEY_LEFT:
        refresh = 100
        head_x -= 1
    if key == W or key == curses.KEY_UP:
        refresh = 150
        head_y -= 1
    if key == S or key == curses.KEY_DOWN:
        refresh = 150
        head_y += 1

    snake.insert(0, (head_y, head_x))

    # End conditions
    if head_y == 0 or head_y == HEIGHT-1: break
    if head_x == 0 or head_x == WIDTH-1: break
    if snake[0] in bombs: break
    if snake[0] in snake[1:]: break

    if snake[0] == fruit: # Eat Fruit
        curses.beep()
        score += 1
        fruit = (randint(1, HEIGHT-2), randint(1, WIDTH-2))
        bombs.append((randint(1, HEIGHT-2), randint(1, WIDTH-2)))
        
        if fruit in snake or fruit in bombs:
           fruit = (randint(1, HEIGHT-2), randint(1, WIDTH-2))
    else:
        last = snake.pop()
        WIN.addch(last[0], last[1], " ")

    for bomb in bombs:
        WIN.addch(bomb[0], bomb[1], "X", curses.color_pair(3))
    for section in snake:
        WIN.addch(section[0], section[1], "\u27D0", curses.color_pair(1))
    
    WIN.addch(fruit[0], fruit[1], "\u2766", curses.color_pair(2))
    

curses.endwin() # Ends curses and returns to console 
print(f"Good job, Your ate {score} fruit!")