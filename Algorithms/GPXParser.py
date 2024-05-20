import gpxpy
import numpy as np
import matplotlib.pyplot as plt
from CoordPoint import CoordPoint

def longLatVals(file):
    with open(file, 'r') as gpx_file:
        gpx_data = gpxpy.parse(gpx_file)

    coordinates = []
    for track in gpx_data.tracks:

        for segment in track.segments:
            for point in segment.points:
                coordinates.append([point.longitude, point.latitude])
            coordinates.append([segment.points[0].longitude, segment.points[0].latitude])
    
    return np.array(coordinates)

def plotLongLat(coord_array):

    fig, ax = plt.subplots()
    min_long_val = np.min(coord_array[:,0]) - 0.001
    max_long_val = np.max(coord_array[:,0]) + 0.001

    min_lat_val = np.min(coord_array[:,1]) - 0.001
    max_lat_val = np.max(coord_array[:,1]) + 0.001

    ax.plot(coord_array[:,0], coord_array[:,1])
    ax.set_xlim(min_long_val, max_long_val)
    ax.set_ylim(min_lat_val, max_lat_val)

    return ax

def drawSquare(ax, coords):

    x_limits = ax.get_xlim()
    x1, x2 = x_limits[0] + 0.001, x_limits[1] - 0.001

    y_limits = ax.get_ylim()
    y1, y2 = y_limits[0] + 0.001, y_limits[1] - 0.001

    bottom_left = CoordPoint([x1,y1], True, True)
    top_left = CoordPoint([x1,y2], True, False)
    top_right = CoordPoint([x2, y2], False, False)
    bottom_right = CoordPoint([x2,y1], False, True)

    square_coords = np.array([bottom_left, top_left, top_right, bottom_right, bottom_left])

    for corner in square_coords:
        closest_gpx_pt = coords[np.argmin(np.linalg.norm(coords - corner.get_coord(), axis=1))]
        corner.set_coord(closest_gpx_pt)
        for other_corner in square_coords:
            if corner != other_corner:
                corner.compare_point(other_corner)

    plt.plot([i.get_x() for i in square_coords],[i.get_y() for i in square_coords])
    midpointIntersection(coords, square_coords)

    plt.plot([i.get_x() for i in square_coords],[i.get_y() for i in square_coords])
    plt.show()

def midpointIntersection(coords, square_coords):
    
    for i in range(4):
        corner1 = square_coords[i]
        corner2 = square_coords[i+1]
        match i:
            case 0:
                y_point_range = [corner1.get_y(), corner2.get_y()]
                x_point_half_range = [corner1.get_x(), (corner1.get_x() + square_coords[2].get_x())/2]
                for coord in coords:
                    if coord[1] > y_point_range[0] and coord[1] < y_point_range[1]:
                        if coord[0] > x_point_half_range[0] and coord[0] < x_point_half_range[1]:
                            corner1.set_x(coord[0])
                            corner2.set_x(coord[0])
                            x_point_half_range[0] = coord[0]
            case 1:
                x_point_range = [corner1.get_x(), corner2.get_x()]
                y_point_half_range = [(corner1.get_y() + square_coords[3].get_y())/2, corner1.get_y()]
                for coord in coords:
                    if coord[0] > x_point_range[0] and coord[0] < x_point_range[1]:
                        if coord[1] > y_point_half_range[0] and coord[1] < y_point_half_range[1]:
                            corner1.set_y(coord[1])
                            corner2.set_y(coord[1])
                            y_point_half_range[0] = coord[1]
            case 2:
                y_point_range = [corner2.get_y(), corner1.get_y()]
                x_point_half_range = [(corner1.get_x() + square_coords[1].get_x())/2, corner1.get_x()]
                for coord in coords:
                    if coord[1] > y_point_range[0] and coord[1] < y_point_range[1]:
                        if coord[0] > x_point_half_range[0] and coord[0] < x_point_half_range[1]:
                            corner1.set_x(coord[0])
                            corner2.set_x(coord[0])
                            x_point_half_range[1] = coord[0]
            case 3:
                x_point_range = [corner2.get_x(), corner1.get_x()]
                y_point_half_range = [corner1.get_y(), (corner1.get_y() + square_coords[2].get_y())/2]
                for coord in coords:
                    if coord[0] > x_point_range[0] and coord[0] < x_point_range[1]:
                        if coord[1] > y_point_half_range[0] and coord[1] < y_point_half_range[1]:
                            corner1.set_y(coord[1])
                            corner2.set_y(coord[1])
                            y_point_half_range[1] = coord[1]






    # Find range between selected points
    # Select half of graph that is applicable.
    # Order points in argsort format, including if condition of midway check.
    # Set coord to match minimum requirement.
    return




             

coords = longLatVals('TestFiles/test2.gpx')
ax = plotLongLat(coords)
drawSquare(ax, coords)