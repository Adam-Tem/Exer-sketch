import gpxpy
import numpy as np
import matplotlib.pyplot as plt

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

def drawShape(ax, coords):

    x_limits = ax.get_xlim()
    x1, x2 = x_limits[0] + 0.001, x_limits[1] - 0.001

    y_limits = ax.get_ylim()
    y1, y2 = y_limits[0] + 0.001, y_limits[1] - 0.001

    bottom_left = [[x1,y1], True, True]
    top_left = [[x1,y2], True, False]
    top_right = [[x2, y2], False, False]
    bottom_right = [[x2,y1], False, True]


    #Work shape in until it is small enough, then expand back out slowly.

    #BOTTOM LEFT CHECK
    closest_bleft = coords[np.argmin(np.linalg.norm(coords - bottom_left[0], axis=1))]
    bottom_left[0] = closest_bleft
    top_left[0][0] = closest_bleft[0]
    bottom_right[0][1] = closest_bleft[1]

    #TOP LEFT CHECK
    closest_tleft = coords[np.argmin(np.linalg.norm(coords - top_left[0], axis=1))]
    top_left[0] = closest_tleft
    top_left[0], bottom_left[0] = closerPoint(top_left, bottom_left)
    top_left[0], top_right[0] = closerPoint(top_left, top_right)

    #TOP RIGHT CHECK
    closest_tright = coords[np.argmin(np.linalg.norm(coords - top_right[0], axis=1))]
    top_right[0] = closest_tright
    top_right[0], bottom_right[0] = closerPoint(top_right, bottom_right)
    top_right[0], top_left[0] = closerPoint(top_right, top_left)

    #BOTTOM RIGHT CHECK
    closest_bright = coords[np.argmin(np.linalg.norm(coords - bottom_right[0], axis=1))]
    bottom_right[0] = closest_bright
    bottom_right[0], top_right[0] = closerPoint(bottom_right, top_right)
    bottom_right[0], bottom_left[0] = closerPoint(bottom_right, bottom_left)

    ##If condition to see if the new coord is further away or not...
    ## NEED TO START TO PARAMETERISE!!!

    square_coords = np.array([bottom_left[0], top_left[0], top_right[0], bottom_right[0], bottom_left[0]])
    plt.plot(square_coords[:,0], square_coords[:,1])
    plt.show()

def closerPoint(point1, point2):
    #Format of point: [coord, boolean for left, boolean for top]
    if point1[1] == point2[1]:

        if point1[1] == True:
            point1[0][0] = point2[0][0] =  max(point1[0][0], point2[0][0])           
            return point1[0], point2[0]
        
        else:
            point1[0][0] = point2[0][0] =  min(point1[0][0], point2[0][0])           
            return point1[0], point2[0]
    
    elif point1[2] == point2[2]:
            
            if point1[2] == True:
                point1[0][1] = point2[0][1] =  max(point1[0][1], point2[0][1])           
                return point1[0], point2[0]
            else:
                point1[0][1] = point2[0][1] =  min(point1[0][1], point2[0][1])           
                return point1[0], point2[0]
    else:
        raise ValueError("Diagonal coordinates do not need to be checked")
             

coords = longLatVals('TestFiles/test2.gpx')
ax = plotLongLat(coords)
drawShape(ax, coords)