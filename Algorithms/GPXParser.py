import gpxpy

with open('TestFiles/test1.gpx', 'r') as gpx_file:
    gpx_data = gpxpy.parse(gpx_file)

for track in gpx_data.tracks:

    for segment in track.segments:
        print(len(segment.points))
        print(segment.points[0].latitude)
        print(segment.points[0].longitude)