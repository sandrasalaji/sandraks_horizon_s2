import matplotlib.pyplot as plt
import numpy as np

def get_user_input():
    points = []
    print("Enter points as (x, y) pairs. Type 'done' when finished.")
    while True:
        user_input = input("Enter point (x, y): ")
        if user_input.lower() == 'done':
            break
        try:
            x, y = map(float, user_input.strip("()").split(","))
            points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter a point in the format (x, y).")
    return points

def plot_points(points):
    x_vals, y_vals = zip(*points)
    plt.scatter(x_vals, y_vals, color='blue')
    for i, (x, y) in enumerate(points):
        plt.text(x, y, f'({x}, {y})', fontsize=9, ha='right')
    plt.title("User  Input Points")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

def connect_nearest_neighbors(points):
    num_points = len(points)
    connected = set()  # To keep track of connected pairs
    for i in range(num_points):
        x1, y1 = points[i]
        nearest_neighbor = None
        min_distance = float('inf')
        
        for j in range(num_points):
            if i != j:
                x2, y2 = points[j]
                distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                
                # Check if this is the nearest neighbor
                if distance < min_distance:
                    nearest_neighbor = j
                    min_distance = distance
        
        # Now we have the nearest neighbor, check for duplicates
        if nearest_neighbor is not None:
            # Check if the line already exists
            if (i, nearest_neighbor) not in connected and (nearest_neighbor, i) not in connected:
                plt.plot([x1, points[nearest_neighbor][0]], [y1, points[nearest_neighbor][1]], 'r-')
                connected.add((i, nearest_neighbor))
            else:
                # Find the next nearest neighbor
                second_nearest_neighbor = None
                second_min_distance = float('inf')
                
                for j in range(num_points):
                    if j != i and j != nearest_neighbor:
                        x2, y2 = points[j]
                        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                        if distance < second_min_distance:
                            second_nearest_neighbor = j
                            second_min_distance = distance
                
                if second_nearest_neighbor is not None:
                    plt.plot([x1, points[second_nearest_neighbor][0]], [y1, points[second_nearest_neighbor][1]], 'r-')
                    connected.add((i, second_nearest_neighbor))

def main():
    points = get_user_input()
    if points:
        plot_points(points)
        connect_nearest_neighbors(points)
        plt.grid()
        plt.axis('equal')
        plt.show()
    else:
        print("No points were entered.")

if _name_ == "_main_":
    main()