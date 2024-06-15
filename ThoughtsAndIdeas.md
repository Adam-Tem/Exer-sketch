# Thoughts and Ideas

This is a more informal file with no real structure but will act as a place for me to note down any random ideas or thoughts I have about the project. Those sort of ideas you get in the middle of a run or just before going to bed about how to work something out or potential challenges.

### 20 May 2024

- I think to begin with it will be best to focus on just mean-centred mass shapes. By this I mean your basic circles, squares and triangles as more awkward shapes may be hard to work with to get the most optimal size for a given GPS graph.

- Find a way to work out hte midpoint intersections. Some sort of ordering of the data points could be useful to then get an appropriate range and work from that, a classic bit of the old argsort! Funny to be actually using these functions for real. I think that could work though: find range between points, select this range in the coords from the GPX, if line passes through move it to fit. Chances are this will shrink the shape too much to begin with but it can probably then be expanded back out.

- Really should be making points an object...

### 21 May 2024

- Does starting from a different corner of the square and working your way around slightly differently produce a different outcome? How can this be optimised? Check all four starter corners and then make an expansion algorithm, finally working out the optimal shape by area?

### 03 June 2024

- Right going the opposite direction probably then means you need to look at the other halves of the split of the shape to evaluate against the right coordinates, I think? Let me go on a run and try to work it out!

- I've tried to work out a way to do it in a simple manner but I think it would just have to be the same function reweritten with slight logic changes, so I'll just stick to the one direction for now.

- Trying to now decide the best way forward for actually expanding the shape. For the test cases I have used, it clearly shows that expanding upwards would be the best option, so I guess evaluating all expansion paths in the first round will help decide.

### 04 June 2024

- Come to think of it, it may be better to do a random start position of a small rectangle and only ever use the expansion function. The shrink one will always force into the general middle area of the shape, but I guess using just the expand function could also limit the issues with GPS outlines that are not a perfect round loop. Interesting.

- After running some initial trials of the expansion only setup, it looks as if after just one expansion the shape will keep getting trapped as it reaches a boundary straight away... May need to consider just expanding all sides at the same time? This would probably be more of the idea for a square, triangle, circle, etc.. A rectangle may have actually been the hardest one to start with!
