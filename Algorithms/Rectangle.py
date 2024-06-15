import numpy as np
import random
import copy
import matplotlib.pyplot as plt
from CoordPoint import CoordPoint
from GPXParser import longLatVals, plotLongLat

def drawRectangle(ax, coords):

    x_limits = ax.get_xlim()
    x1, x2 = x_limits[0] + 0.001, x_limits[1] - 0.001

    y_limits = ax.get_ylim()
    y1, y2 = y_limits[0] + 0.001, y_limits[1] - 0.001

    bottom_left = CoordPoint([x1,y1], True, True)
    top_left = CoordPoint([x1,y2], True, False)
    top_right = CoordPoint([x2, y2], False, False)
    bottom_right = CoordPoint([x2,y1], False, True)

    sq_coords = random_start(x1,x2,y1,y2)

    sq_coords2 = np.array([copy.copy(i) for i in sq_coords])
    plt.plot([i.get_x() for i in sq_coords],[i.get_y() for i in sq_coords])
    best_expansion(sq_coords, coords)
    plt.plot([i.get_x() for i in sq_coords],[i.get_y() for i in sq_coords])
    x=0
    print("Hello")
    print(np.array_equal(sq_coords2, sq_coords))

    while not np.array_equal(sq_coords2, sq_coords):
 
        sq_coords2 = np.array([copy.copy(i) for i in sq_coords])
        prev_area = ((sq_coords2[1].get_y() - sq_coords2[0].get_y()) * 
                     (sq_coords2[2].get_x() - sq_coords2[0].get_x()))
        best_expansion(sq_coords, coords)
        plt.plot([i.get_x() for i in sq_coords],[i.get_y() for i in sq_coords])
        area = ((sq_coords[1].get_y() - sq_coords[0].get_y()) * 
                (sq_coords[2].get_x() - sq_coords[0].get_x()))
        print((area - prev_area) / area )
        if (area - prev_area) / area < 0.05:
            break


    
    plt.show()

def midpointIntersection(coords, square_coords):

    position_adjustment = position_check(square_coords[0])

    for i in range(4):
        j = (i + position_adjustment) % 4
        shrink_coords(j, square_coords[i-1], square_coords[i], square_coords[(i+1) % 4], coords)

def position_check(coord):
    if coord.get_is_left() == True:
        if coord.get_is_bottom() == True:
            return 0
        else:
            return 1
    else:
        if coord.get_is_bottom() == True:
            return 3
        else:
            return 2
        
def shrink_coords(position, prev_corner, current_corner, next_corner, coords):

    if position == 0:
        full_point_range = [current_corner.get_y(), next_corner.get_y()]
        half_point_range = [current_corner.get_x(), (current_corner.get_x() + prev_corner.get_x())/2]
    elif position == 1:
        full_point_range = [current_corner.get_x(), next_corner.get_x()]
        half_point_range = [(current_corner.get_y() + prev_corner.get_y())/2, current_corner.get_y()]
    elif position == 2:
        full_point_range = [next_corner.get_y(), current_corner.get_y()]
        half_point_range = [(current_corner.get_x() + prev_corner.get_x())/2, current_corner.get_x()]
    else:
        full_point_range = [next_corner.get_x(), current_corner.get_x()]
        half_point_range = [current_corner.get_y(), (current_corner.get_y() + prev_corner.get_y())/2]

    moves = [[0,0],[1,1],[1,0],[0,1]]
    for coord in coords:
        if coord[(position+1) % 2] > full_point_range[0] and coord[(position+1) % 2] < full_point_range[1]:
            if coord[position % 2] > half_point_range[0] and coord[position % 2] < half_point_range[1]:
                if (position % 2) == 0:
                    current_corner.set_x(coord[0])
                    next_corner.set_x(coord[0])
                else:
                    current_corner.set_y(coord[1])
                    next_corner.set_y(coord[1])
                
                half_point_range[moves[position][0]] = coord[moves[position][1]]
        
        
def best_expansion(square_coords, coords):
    
    expansion_coords = []
    print("at all")
    for i in range(4):
        if i == 0:
            valid_coords = coords[(coords[:,0] < square_coords[i].get_x()) &
                            (coords[:,1] > square_coords[i].get_y()) &
                            (coords[:,1] < square_coords[i+1].get_y())]
            
            if len(valid_coords) > 0:
                bottom_left_expansion_coord = valid_coords[np.argmax(valid_coords[:, 0])][0]
                expansion_coords.append(bottom_left_expansion_coord)
                bottom_left_expansion_area = ((square_coords[i].get_x() - bottom_left_expansion_coord) * 
                                            (square_coords[i+1].get_y() - square_coords[i].get_y()))
            else:
                print("sfkjhs")
                expansion_coords.append(square_coords[i].get_x())
                bottom_left_expansion_area = 0
        elif i == 1:
            valid_coords = coords[(coords[:,1] > square_coords[i].get_y()) &
                            (coords[:,0] > square_coords[i].get_x()) &
                            (coords[:,0] < square_coords[i+1].get_x())]
            
            if len(valid_coords) > 0:
                top_left_expansion_coord = valid_coords[np.argmin(valid_coords[:, 1])][1]
                expansion_coords.append(top_left_expansion_coord)
                top_left_expansion_area = ((top_left_expansion_coord - square_coords[i].get_y()) * 
                                            (square_coords[i+1].get_x() - square_coords[i].get_x()))
            else:
                print(1)
                expansion_coords.append(square_coords[i].get_y())
                top_left_expansion_area = 0

        elif i == 2:
            valid_coords = coords[(coords[:,0] > square_coords[i].get_x()) &
                            (coords[:,1] < square_coords[i].get_y()) &
                            (coords[:,1] > square_coords[i+1].get_y())]
            
            if len(valid_coords) > 0:
                top_right_expansion_coord = valid_coords[np.argmin(valid_coords[:, 0])][0] 
                expansion_coords.append(top_right_expansion_coord)
                top_right_expansion_area = ((top_right_expansion_coord - square_coords[i].get_x()) *
                                            (square_coords[i].get_y() - square_coords[i+1].get_y()))
            else:
                print(2)
                expansion_coords.append(square_coords[i].get_x())
                top_right_expansion_area = 0
            
        elif i == 3:
            valid_coords = coords[(coords[:,1] < square_coords[i].get_y()) &
                            (coords[:,0] < square_coords[i].get_x()) &
                            (coords[:,0] > square_coords[(i+1)%4].get_x())]
            
            if len(valid_coords) > 0:
                bottom_right_expansion_coord = valid_coords[np.argmax(valid_coords[:, 1])][1]
                expansion_coords.append(bottom_right_expansion_coord)
                bottom_right_expansion_area = ((square_coords[i].get_y() - bottom_right_expansion_coord) *
                                    (square_coords[i].get_x() - square_coords[(i+1)%4].get_x()))
            else:
                print(3)
                expansion_coords.append(square_coords[i].get_y())
                bottom_right_expansion_area = 0
       
    best_area = np.argmax([bottom_left_expansion_area, 
             top_left_expansion_area, 
             top_right_expansion_area, 
             bottom_right_expansion_area])
    
    print(best_area, expansion_coords[best_area])
    if best_area % 2 == 0:
        square_coords[best_area].set_x(expansion_coords[best_area])
        square_coords[best_area + 1].set_x(expansion_coords[best_area])
    else:
        square_coords[best_area].set_y(expansion_coords[best_area])
        square_coords[(best_area + 1)%4].set_y(expansion_coords[best_area])


def random_start(x1, x2, y1, y2):

    bottom_left = CoordPoint([random.uniform(x1,x2), random.uniform(y1,y2)], True, True)
    top_left = CoordPoint([bottom_left.get_x(), bottom_left.get_y() + 0.001], True, False)
    top_right = CoordPoint([top_left.get_x() + 0.001, top_left.get_y()], False, False)
    bottom_right = CoordPoint([top_right.get_x(), bottom_left.get_y()], False, True)

    return np.array([bottom_left, top_left, top_right, bottom_right, bottom_left])


coords = longLatVals('TestFiles/test1.gpx')
ax = plotLongLat(coords)
drawRectangle(ax, coords)