import glfw
from OpenGL.GL import *
import numpy as np

# Vertex shader program
vertex_shader_source = """
#version 330 core
layout (location = 0) in vec2 aPos;
void main()
{
    gl_Position = vec4(aPos.x, aPos.y, 0.0, 1.0);
}
"""

# Fragment shader program
fragment_shader_source = """
#version 330 core
out vec4 FragColor;
void main()
{
    FragColor = vec4(1.0, 0.5, 0.2, 1.0);
}
"""

def compile_shader(shader_type, source):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        raise Exception(f"Shader compilation error: {glGetShaderInfoLog(shader)}")
    return shader

def link_program(vertex_shader, fragment_shader):
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        raise Exception(f"Shader linking error: {glGetProgramInfoLog(program)}")
    return program

def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Configure GLFW
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "OpenGL Example", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the key callback function
    glfw.set_key_callback(window, key_callback)

    # Compile and link shaders
    vertex_shader = compile_shader(GL_VERTEX_SHADER, vertex_shader_source)
    fragment_shader = compile_shader(GL_FRAGMENT_SHADER, fragment_shader_source)
    shader_program = link_program(vertex_shader, fragment_shader)

    # Set up vertex data and buffers
    vertices = np.array([-0.5, -0.5,  # Vertex 1
                         0.5, -0.5,   # Vertex 2
                         0.0,  0.5],  # Vertex 3
                        dtype=np.float32)

    # Create VAO and VBO
    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    # Bind VAO
    glBindVertexArray(VAO)

    # Bind VBO and set vertex data
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # Set vertex attribute pointers
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(GLfloat), ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Unbind VAO
    glBindVertexArray(0)

    while not glfw.window_should_close(window):
        # Render here
        glClear(GL_COLOR_BUFFER_BIT)

        # Use the shader program
        glUseProgram(shader_program)

        # Bind VAO
        glBindVertexArray(VAO)

        # Draw the triangle
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # Unbind VAO
        glBindVertexArray(0)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # Cleanup
    glDeleteVertexArrays(1, [VAO])
    glDeleteBuffers(1, [VBO])
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    glDeleteProgram(shader_program)

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
