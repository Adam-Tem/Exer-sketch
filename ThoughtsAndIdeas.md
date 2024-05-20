# Thoughts and Ideas

This is a more informal file with no real structure but will act as a place for me to note down any random ideas or thoughts I have about the project. Those sort of ideas you get in the middle of a run or just before going to bed about how to work something out or potential challenges.

- I think to begin with it will be best to focus on just mean-centred mass shapes. By this I mean your basic circles, squares and triangles as more awkward shapes may be hard to work with to get the most optimal size for a given GPS graph.

- Find a way to work out hte midpoint intersections. Some sort of ordering of the data points could be useful to then get an appropriate range and work from that, a classic bit of the old argsort! Funny to be actually using these functions for real. I think that could work though: find range between points, select this range in the coords from the GPX, if line passes through move it to fit. Chances are this will shrink the shape too much to begin with but it can probably then be expanded back out.
