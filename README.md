# Python

This is a group project developed for a university Python course. It applies object-oriented programming and linear programming to solve the Travelling Salesman Problem (TSP) using the [subtour elimination method](https://pymprog.sourceforge.net/subtour.html). The graphical user interface is built with Tkinter.

To run the program, ensure that Python 3 is installed on your system. Then, download the project files and execute TsP.py.

Upon launching the program, you can navigate to the input type menu and you'll be presented with a menu to input the coordinates (x, y) for each city. You can choose from three input methods:

a)Random Generation – Generate coordinates for a specified number of cities.

b)From File – Load coordinates from a text file where:

&nbsp;&nbsp;&nbsp;&nbsp;The first line contains the number of cities.

&nbsp;&nbsp;&nbsp;&nbsp;Each subsequent line contains two integers representing the x and y coordinates of a city.

c)Manual Entry – Choose the "User" option to enter the number of cities and their coordinates directly through the GUI.

After providing the input, click "Run" to display a map showing all cities.

Left-click on the map to visualize the optimal route and total distance, calculated using linear programming.

Right-click to open a new map window. In this view, left-click again to display a greedy solution (where the salesman always travels to the nearest unvisited city), along with the corresponding distance. Note that this method may not produce the optimal route, but serves as a useful comparison.
