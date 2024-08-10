CMPE150-Project
This Python project generates text-based graphical representations based on a series of input commands. The script processes these inputs to produce the desired visual output directly in the terminal.

For more detailed information about the project, please visit the project description here.

Project Overview
The core idea of this project is to construct a matrix, populate it with the specified shapes, and then print it in a formatted manner. The process involves:

Matrix Dimension Calculation:

First, the script determines the width of the matrix necessary to accommodate the given shapes.
Shape Block Processing:

For each block of shapes (which corresponds to elements in the list created by splitting the input by ',N,'), the script calculates the required matrix height.
Matrix Filling:

The matrix is then filled with the desired shapes, represented by "*" for the shapes and "-" for optional decorations like delimiters.
Output:

Finally, the script prints the matrix, showcasing the requested shapes in a neatly aligned format.
This approach ensures that the shapes are correctly centered and aligned within the output, providing a clear and structured visual representation.

