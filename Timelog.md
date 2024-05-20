# Exer-sketch Project Timelog

Below is the daily workflow of the Exer-sketch project: goals achieved, problems identified and potential next steps. I will fill this in every time I work on the project, as a way of tracking progress while also holding myself accountable to put a good amount of hours towards this and trying to stay consistent.

## 20 May 2024

### 0.5 hours

Project repo has officially been set up and some basic goals and outlines identified.

### 1 hour

Just gone and made sure that node and python are all up to date and good to go for the project. Managed to do a little exploring of the Strava API but feel that it may be easier to first parse a GPX file and then get the exports from the API, just in case I do not end up using the Strava API. Managed to get the first little bit of GPX parsing done, by getting the lat/long value of the first point in a file.

### 0.75 hours

Quick update, managed to get the lat long values being plotted in a matplotlib graph, and have made it so that the graph is connected. I will now focus on trying to get some sort of shape inside the graph and try to expand it to the biggest size possible.

### 1.25 hours

Some further progress has been made. The initial adjustments to a square shape modifier have been added, by reducing the x and y coords of the corners to fit inside their closest points, but does not factor in for any midpoint intersections.

### 1.25 hours

The algorithm is showing some promise. I now have the square managing to be shrunk into a particular space of the GPS shape, but it is now about expanding it so that it is the optimal size. I have also managed to abstract the coordinate point into a separate class, just trying to keep things tidy from the get go.
