import numpy as np
import random
import copy
import matplotlib.pyplot as plt
import matplotlib.path as mpltPath
from CoordPoint import CoordPoint
from GPXParser import longLatVals, plotLongLat


def random_start(x1, x2, y1, y2):

    start_x = random.uniform(x1,x2)
    start_y = random.uniform(y1,y2) 
    bottom_left = CoordPoint([start_x, start_y], True, True)
    top_left = CoordPoint([start_x, start_y], True, False)
    top_right = CoordPoint([start_x, start_y], False, False)
    bottom_right = CoordPoint([start_x, start_y], False, True)

    return np.array([bottom_left, top_left, top_right, bottom_right, bottom_left])


def is_shape_outside_graph(corner_pos, square_coords, graph_coords):

    match corner_pos:
        case "bottomLeft":
            for point in graph_coords:
                #check x
                if point[0] > square_coords[0].get_x() and point[0] < square_coords[3].get_x():
                    #check y
                    if point[1] > square_coords[0].get_y() and point[1] < square_coords[1].get_y():
                        return True

        case "topLeft":
            for point in graph_coords:
                #check x
                if point[0] > square_coords[1].get_x() and point[0] < square_coords[2].get_x():
                    #check y
                    if point[1] < square_coords[1].get_y() and point[1] > square_coords[0].get_y():
                        return True

        case "topRight":
            for point in graph_coords:
               #check x
               if point[0] < square_coords[2].get_x() and point[0] > square_coords[1].get_x():
                    #check y
                    if point[1] < square_coords[2].get_y() and point[1] > square_coords[3].get_y():
                        return True

        case "bottomRight":
            for point in graph_coords:
            #check x
               if point[0] < square_coords[3].get_x() and point[0] > square_coords[0].get_x():
                    #check y
                    if point[1] > square_coords[3].get_y() and point[1] < square_coords[2].get_y():
                        return True

    return False

def expand_corner(corner_pos, square_coords):

    match corner_pos:
        case "bottomLeft":
            square_coords[0].set_x(square_coords[0].get_x() - 0.001)
            square_coords[0].set_y(square_coords[0].get_y() - 0.001)
            square_coords[1].set_x(square_coords[0].get_x())
            square_coords[3].set_y(square_coords[0].get_y())
        case "topLeft":
            square_coords[1].set_x(square_coords[1].get_x() - 0.001)
            square_coords[1].set_y(square_coords[1].get_y() + 0.001)
            square_coords[0].set_x(square_coords[1].get_x())
            square_coords[2].set_y(square_coords[1].get_y())
        case "topRight":
            square_coords[2].set_x(square_coords[2].get_x() + 0.001)
            square_coords[2].set_y(square_coords[2].get_y() + 0.001)
            square_coords[3].set_x(square_coords[2].get_x())
            square_coords[1].set_y(square_coords[2].get_y())
        case "bottomRight":
            square_coords[3].set_x(square_coords[3].get_x() + 0.001)
            square_coords[3].set_y(square_coords[3].get_y() - 0.001)
            square_coords[2].set_x(square_coords[3].get_x())
            square_coords[0].set_y(square_coords[3].get_y())

    return square_coords

def calculate_square_area(square_coords):
    return (abs(square_coords[2].get_x() - square_coords[1].get_x()) * 
            abs(square_coords[2].get_y() - square_coords[3].get_y()))

def drawSquare(graph_coords, graph_outline):
    x_limits = ax.get_xlim()
    x1, x2 = x_limits[0] + 0.001, x_limits[1] - 0.001

    y_limits = ax.get_ylim()
    y1, y2 = y_limits[0] + 0.001, y_limits[1] - 0.001
    
    max_area = (x2-x1) * (y2-y1)

    square_coords = random_start(x1, x2, y1, y2)
    
    inside = False
    iterations = 0
    while not inside and iterations < 10:
        iterations += 1
        square_coords = random_start(x1, x2, y1, y2)
        inside = graph_outline.contains_point([square_coords[1].get_x(), square_coords[1].get_y()])

    corner_list = ["bottomLeft", "topLeft", "topRight", "bottomRight"]
    if iterations < 10:
        for corner in corner_list:
            outside = False
            count = 0
            while not outside:
                count += 1
                prev_coords = copy.deepcopy(square_coords)
                square_coords = expand_corner(corner, square_coords)
                outside = is_shape_outside_graph(corner, square_coords, graph_coords)
                if count > 100:
                    print("hello")
                    plt.plot([i.get_x() for i in square_coords],[i.get_y() for i in square_coords])
                    break

            square_coords = prev_coords

    return [calculate_square_area(square_coords), square_coords]


graph_coords = longLatVals('TestFiles/test2.gpx')
ax = plotLongLat(graph_coords)
ax.set_aspect('equal', adjustable='box')
max_area = [0,0]
graph_outline = mpltPath.Path(graph_coords)
for i in range(50):
    area = drawSquare(graph_coords, graph_outline)
    if area[0] > max_area[0]:
        max_area = area

plt.plot([i.get_x() for i in max_area[1]],[i.get_y() for i in max_area[1]])

plt.show()