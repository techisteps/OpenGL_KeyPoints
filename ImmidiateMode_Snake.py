import glfw
from OpenGL.GL import *
import random

# Constants
GRID_SIZE = 5
GRID_WIDTH = 200
GRID_HEIGHT = 150
SNAKE_SIZE = 0.05
FPS = 10

# Snake variables
snake = [(10, 10)]
snake_direction = (1, 0)
food = (0, 0)

def draw_square(x, y):

    x = (x/GRID_WIDTH) - 1.0
    y = (y/GRID_HEIGHT) - 1.0

    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + SNAKE_SIZE, y)
    glVertex2f(x + SNAKE_SIZE, y + SNAKE_SIZE)
    glVertex2f(x, y + SNAKE_SIZE)
    glEnd()

def draw_snake():
    glColor3f(0.0, 1.0, 0.0)  # Snake color is green
    for segment in snake:
        draw_square(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE)

def draw_food():
    glColor3f(1.0, 0.0, 0.0)  # Food color is red
    draw_square(food[0] * GRID_SIZE, food[1] * GRID_SIZE)


def reset_game():
    global snake, snake_direction, food
    snake = [(0, 0)]
    snake_direction = (1, 0)
    generate_food()

def generate_food():
    global food
    food = ( random.randint(0, GRID_WIDTH/GRID_SIZE - 1 ), random.randint(0, GRID_HEIGHT/GRID_SIZE - 1 ) )

def key_callback(window, key, scancode, action, mods):
    global snake_direction
    if action == glfw.PRESS:
        if key == glfw.KEY_UP and snake_direction != (0, 1):
            snake_direction = (0, 1)
        elif key == glfw.KEY_DOWN and snake_direction != (0, -1):
            snake_direction = (0, -1)
        elif key == glfw.KEY_LEFT and snake_direction != (-1, 0):
            snake_direction = (-1, 0)
        elif key == glfw.KEY_RIGHT and snake_direction != (1, 0):
            snake_direction = (1, 0)
        elif key == glfw.KEY_ESCAPE:
            glfw.terminate()
            exit(0)


def update_snake():
    global snake
    head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # Check for collisions
    if head in snake or not (0 <= head[0] < GRID_WIDTH) or not (0 <= head[1] < GRID_HEIGHT):
        reset_game()
    else:
        snake.insert(0, head)

        # Check if snake eats food
        if head == food:
            generate_food()
        else:
            snake.pop()

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE, "Snake Game", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the key callback function
    glfw.set_key_callback(window, key_callback)

    # Set up the game
    reset_game()


    glClear(GL_COLOR_BUFFER_BIT)

    while not glfw.window_should_close(window):

        # Render here
        glClear(GL_COLOR_BUFFER_BIT)

        # Update game logic
        update_snake()

        # Draw the snake and food
        print("snake ", snake, ", snake_direction ", snake_direction)
        draw_snake()
        draw_food()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

        # Control the frame rate
        glfw.set_time(0)
        while glfw.get_time() < 1 / FPS:
            pass

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
