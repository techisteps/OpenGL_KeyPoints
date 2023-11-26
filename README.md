# OpenGL_KeyPoints
This repository hold basic key points to understand before learning OpenGL


# Bullet Points

- OpenGL is graphics API specification only. It's not a library.
- Graphics hardware vendors write hardware drives which support OpenGL specification.
- To write OpenGL program you need a Window library to create a Window as context for OpenGL (GLFW, SDL etc.) and another library to load OpenGL functions from graphics driver (GLut, SDL PyOpenGL etc).
- OpenGL follows a state machine pattern. Its not Object Oriented, Functional programming etc.  
[State Machine example1](https://webglfundamentals.org/webgl/lessons/resources/webgl-state-diagram.html?exampleId=smallest#no-help)  
 [State Machine example2](https://webgl2fundamentals.org/webgl/lessons/resources/webgl-state-diagram.html?exampleId=smallest#no-help)  
- Early version of OpenGL was very limited and its refer as `Immediate Mode` or `Legacy OpenGL`. It's got outdated and should not be used for any new projects.  
[Immediate Mode example 1 (Minimum)](ImmidiateMode_Minimum.py)  
[Immediate Mode example 2 (Snake) ](ImmidiateMode_Minimum.py)  
- Latest OpenGL is called `Modern OpenGL` or `Programmable Pipeline`. It has many profiles as: 
- - **Core** - The Core Profile is designed to provide a modern and forward-looking OpenGL experience.
- - **Compatible Mode** - The Compatibility Profile is aimed at providing compatibility with older versions of OpenGL, including features deprecated in the Core Profile
- - **ES** - This is for mobile devices.  

  [Modern OpenGL example (Minimum)](MordenOpenGL_Minimun.py)


# IMP Links
https://learnopengl.com/  
https://docs.gl/  
http://www.opengl-tutorial.org/  
https://webgl2fundamentals.org/  
https://open.gl/  
https://www.songho.ca/opengl/index.html   
https://registry.khronos.org/OpenGL/index_gl.php  
https://www.khronos.org/developers/reference-cards/  

Tutorials:  
[Learn OpenGL in python](https://www.youtube.com/playlist?list=PL1P11yPQAo7opIg8r-4BMfh1Z_dCOfI0y)


---


# What is OpenGL?

OpenGL, which stands for Open Graphics Library, is a cross-platform, open-source graphics API (Application Programming Interface) that is widely used for rendering 2D and 3D graphics in applications such as video games, simulations, and graphical user interfaces (GUIs). It was developed by the Khronos Group, a consortium of industry leaders in the fields of graphics, parallel computing, and mobile devices.

Key characteristics and features of OpenGL include:

**Cross-Platform**: OpenGL is designed to be platform-independent, meaning it can be used on various operating systems such as Windows, macOS, Linux, and others. This makes it a versatile choice for developers targeting multiple platforms.

**Low-Level Graphics API**: OpenGL provides a low-level interface that allows developers to interact directly with the graphics hardware. This enables efficient and fine-grained control over the rendering process.

**3D Graphics Rendering**: OpenGL is commonly used for rendering 3D graphics, allowing developers to create realistic visualizations of three-dimensional objects and scenes. It supports transformations, lighting, shading, and other features essential for 3D graphics.

**Shader Programming**: With the introduction of modern versions of OpenGL (3.0 and later), the programmable pipeline became a significant feature. Developers can use shaders (small programs) written in GLSL (OpenGL Shading Language) to customize various stages of the graphics pipeline.

**Versatility**: While OpenGL is widely used in game development, it is not limited to this domain. It finds applications in scientific visualization, simulations, CAD (Computer-Aided Design), virtual reality, and more.

**Community and Documentation**: OpenGL has a large and active community of developers. The specification is well-documented, and there are numerous tutorials, forums, and resources available for learning and troubleshooting.

**Compatibility Profiles**: OpenGL provides compatibility profiles to ensure backward compatibility with older versions. However, modern OpenGL encourages the use of core profiles, emphasizing newer features and practices.

It's important to note that while OpenGL is a powerful and widely used graphics API, there are also other graphics APIs such as Vulkan, Metal and DirectX, each with its own strengths and use cases. Vulkan, for example, is a more recent API designed for high performance and efficiency, while DirectX is primarily used on Windows platforms. The choice of API often depends on the specific requirements of a project and the target platforms.



# From where to get OpenGL library?

OpenGL is not a standalone library that you can download separately. Instead, it's an API (Application Programming Interface) specification provided by the Khronos Group. To use OpenGL in your projects, you typically need an implementation of the OpenGL API, and this implementation is usually provided by the graphics driver of your GPU (Graphics Processing Unit).

Here's how you can work with OpenGL:

1. **Graphics Driver**:

- Ensure that your GPU drivers are up to date. Most modern GPUs from companies like NVIDIA, AMD, and Intel support OpenGL. Visit the respective websites to download and install the latest drivers for your GPU.

2. **OpenGL Headers**:

- If you are developing on Windows, you can obtain the OpenGL headers from the Microsoft SDK or other libraries like GLEW (OpenGL Extension Wrangler). GLEW simplifies the process of loading OpenGL extensions, making it easier to access modern OpenGL features. You can download GLEW from its official website: GLEW - The OpenGL Extension Wrangler Library

- On Linux, the OpenGL headers are usually included in the development packages. For example, on Ubuntu, you can install the necessary packages with the following command:

```bash
sudo apt-get install mesa-common-dev libgl1-mesa-dev
```

3. **Development Environment**:

- Choose a programming language and development environment. OpenGL bindings are available for various programming languages, including C, C++, Python, and more.

- - For C and C++, you can include the OpenGL headers and link against the OpenGL library provided by your graphics driver.
- - For Python, you can use the PyOpenGL library, which is a Python binding for OpenGL.

4. **PyOpenGL (for Python)**:

- If you're working with Python, you can install the PyOpenGL library using the following command:

```bash
pip install PyOpenGL
```
- PyOpenGL provides Python bindings for OpenGL, and you can use it to develop OpenGL applications in Python.

5. **OpenGL Documentation**:

- Refer to the official OpenGL documentation provided by the Khronos Group for the API specifications and reference material: OpenGL - The Industry Standard for High Performance Graphics  

Remember that the exact steps may vary depending on your operating system and development environment. Always refer to the documentation and resources specific to the language and platform you are working with.


# Which programming style OpenGL API falls into, is it Object Oriented or Functional etc?


OpenGL does not strictly adhere to a specific programming paradigm like Object-Oriented Programming (OOP) or Functional Programming (FP). Instead, OpenGL follows a procedural style or imperative programming paradigm.

The core OpenGL API consists of a set of procedures (functions) that manipulate the state of the rendering pipeline. In a procedural programming style, you typically call functions or procedures to perform operations. The OpenGL functions are stateful, meaning that they modify the internal state of the rendering context when called.

While the core OpenGL API is procedural, modern OpenGL introduced a programmable pipeline, which allows developers to write shaders in GLSL (OpenGL Shading Language). GLSL is a C-like language, and shaders written in GLSL are more in line with a functional programming style, especially when dealing with transformations and computations on vertex and fragment data.

In summary:

- Core OpenGL API: Procedural - It involves calling procedures (functions) to perform operations on the OpenGL rendering pipeline.

- GLSL Shaders: Shader programming in GLSL can have elements of functional programming, especially when defining transformations and computations within the shaders.

It's worth noting that while procedural programming is the predominant style for using the core OpenGL API, developers often encapsulate OpenGL functionality within classes and structures in their applications, creating a more object-oriented facade around the API for ease of use and code organization. Libraries like GLFW and GLEW provide a more OOP-style interface on top of the OpenGL core, simplifying certain tasks and providing an easier-to-use API.


# Explain OpenGL state machine.

The OpenGL state machine refers to the set of parameters and configurations that define the current state of the OpenGL rendering pipeline. OpenGL operates as a state machine, where various state variables determine how subsequent rendering commands will be executed. Understanding and managing the OpenGL state machine is crucial for effective graphics programming.

Here are key aspects of the OpenGL state machine:

1. State Variables:

- The OpenGL state includes a wide range of variables, such as the current color, transformation matrices, shaders, blending modes, and more.
- These state variables collectively determine the behavior of the rendering pipeline.

2. State Changes:

- Rendering commands in OpenGL often involve changing the state. For example, calling functions like `glColor`, `glMatrixMode`, or `glUseProgram` modifies specific state variables.
- Once a state is changed, subsequent rendering commands will use the updated state until it is changed again.

3. Global State:

- The OpenGL state is global, meaning that changes to the state affect all subsequent rendering operations until the state is explicitly modified again.
- This global nature allows OpenGL to be efficient, as it minimizes the need to repeatedly specify settings for each draw call.

4. Push and Pop State:

- OpenGL provides functions like `glPushAttrib` and `glPopAttrib` that allow you to save and restore portions of the state. This is useful when you want to make temporary changes without affecting the entire state.


5. Immutable State Objects:

- In modern OpenGL, there's a concept of immutable state objects, such as Vertex Array Objects (VAOs) and Framebuffer Objects (FBOs). These objects encapsulate a set of state configurations, making it easier to switch between different rendering setups.

6. Shader Programs:

- The programmable pipeline introduced in modern OpenGL allows you to use shaders (vertex and fragment shaders) to customize parts of the rendering process. Shader programs are a significant part of the OpenGL state.

7. Error Checking:

- OpenGL provides functions like glGetError to check for errors in the API calls. It's important to check for errors during development to ensure that the state transitions are valid.

Here's a simplified example to illustrate state changes in OpenGL:

```cpp
glClearColor(0.0f, 0.0f, 0.0f, 1.0f);  // Set clear color to black
glClear(GL_COLOR_BUFFER_BIT);           // Clear the color buffer

glColor3f(1.0f, 0.0f, 0.0f);            // Set color to red
glBegin(GL_TRIANGLES);                  // Begin drawing triangles
// ... (specify vertices)
glEnd();                                // End drawing triangles
```


In this example:

- `glClearColor` and `glClear` modify the color-related state.
- `glColor3f` changes the current color.
- `glBegin` and `glEnd` define a block of rendering commands that use the current state settings.

Understanding and managing the OpenGL state machine effectively is essential for writing efficient and correct graphics code.

# What are different profiles of OpenGL?

OpenGL has two main profiles: Core Profile and Compatibility Profile. These profiles provide developers with options to choose the level of functionality and backward compatibility with older versions of OpenGL. Here's an overview of each:

1. Core Profile:

- **Purpose:** The Core Profile is designed to provide a modern and forward-looking OpenGL experience. It emphasizes a more streamlined and efficient approach to graphics programming.
- **Features:**
Removes deprecated features present in earlier versions.
Encourages the use of shaders for programmable pipeline stages.
Promotes a more modular and flexible architecture.

2. Compatibility Profile:

- **Purpose:** The Compatibility Profile is aimed at providing compatibility with older versions of OpenGL, including features deprecated in the Core Profile. It allows developers to transition gradually to newer OpenGL versions while maintaining compatibility with existing code.
- **Features:**
Includes all features from earlier OpenGL versions, including deprecated ones.
Allows developers to use fixed-function pipeline features alongside modern OpenGL features.
When creating an OpenGL context, developers can choose whether to create a Core or Compatibility Profile. The choice depends on factors such as the desired level of backward compatibility and the availability of specific features.

Here's a brief summary of how the profiles are created in code:

```cpp
// Example of creating an OpenGL context with a Core Profile
glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

// Example of creating an OpenGL context with a Compatibility Profile
glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_COMPAT_PROFILE);
```

In these examples, the `GLFW_OPENGL_CORE_PROFILE` and `GLFW_OPENGL_COMPAT_PROFILE` flags are used to specify the Core and Compatibility Profiles, respectively.

Developers are encouraged to use the Core Profile for new projects as it promotes modern OpenGL practices and provides better performance. However, if maintaining compatibility with older codebases or using deprecated features is necessary, the Compatibility Profile may be chosen.

It's essential to note that the distinction between Core and Compatibility Profiles applies to OpenGL versions 3.1 and later. In versions 3.0 and earlier, there is no explicit Core or Compatibility Profile, and features are determined by the version number.