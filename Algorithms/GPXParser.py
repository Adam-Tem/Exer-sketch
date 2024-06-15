import numpy as np
import gpxpy
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