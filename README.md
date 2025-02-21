# sandraks_horizon_s2
NEAREST NEIGHBOR POINT CONNECTOR

DESCRIPTION:
This Python script allows users to input (x, y) coordinates and visualizes them on a scatter plot. It then connects each point to its nearest neighbor using red lines, ensuring that duplicate connections are avoided.

FEATURES:
Users can input multiple points manually.
Points are plotted on a 2D plane with labels.
Each point is connected to its nearest neighbor.
Ensures that no pair is connected more than once.

HOW IT WORKS:
The program takes user input for points and stores them in a list.
It plots all points on a 2D graph.
It calculates the nearest neighbor for each point and connects them.
The graph is displayed with labeled points and connections.

Example Input & Output
Input:
Enter point (x, y): (2, 3)
Enter point (x, y): (5, 8)
Enter point (x, y): (1, 1)
Enter point (x, y): done

Output:
A graph with the points plotted and nearest neighbor connections shown.
