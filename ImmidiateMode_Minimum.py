import glfw
from OpenGL.GL import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    glVertex2f(0.0, 1.0)      # Vertex 1
    glColor3f(0.0, 1.0, 0.0)  # Set color to green
    glVertex2f(-1.0, -1.0)    # Vertex 2
    glColor3f(0.0, 0.0, 1.0)  # Set color to blue
    glVertex2f(1.0, -1.0)     # Vertex 3
    glEnd()

def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "OpenGL Example", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the key callback function
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        # Render here
        glClear(GL_COLOR_BUFFER_BIT)

        draw_triangle()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
