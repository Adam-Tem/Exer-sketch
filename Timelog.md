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

## 21 May 2024

### 2 minutes

Managed to resolve the logic issue that I had for not shrinking the square enough. I was adjusting the wrong side of the scale so it would then not move any further.

## 03 June 2024

### 1.5 hours

Well then... An impromptu training camp holiday for a week in Mallorca meant this was put completely on hold but the holiday was great and I don't feel super focussed to work on this but know that I need to have something to show when I go to job interviews so that is motivation enough! Have managed to refactor the code a little for shrinking down the rectangle. It means that the direction of corner checks can be carried out in the opposite way, which works well for one test case but not so much for the second test case...

### 1 hour

Okay, some progress on the expansion side of things, still unsure it is actually creating the most optimal shape from the initial shrink but can continue working on this and test more examples.

### 0.5 hours

Some reasonable progress with the expansion function. Still struggling to try to parameterise it in a nice way and still a few logic errors but decent work nonetheless.

## 10 June 2024

### 1 hour

Not good leaving the project this long... After some head scratching and reshuffling there, the expansion only option seems to be working the best, just need to add a few more case catchers to ensure that the first rectangle drawn is fully inside the GPS outline, but then it should be close to the rectangle algorithm being done??? WHo knows at this point.

## 13 June 2024

### 1 hour

Still only an hour but looked at the start of the design process for the frontend mobile development side of things. Colour palette will honestly be the hardest challenge but I am using Figma which I guess is at least some sort of experience.

## 15 June 2024

### 2 hours

After a bad training day, I've managed to actually put a bit more time towards the design of this! Pretty much completed the Figma design of the app and done an initial round of user testing and collecting feedback from the fam. Colourway was actually liked and navigation and layout okay also, however some potential clashes with the gps drawings used and the background colours but an easy fix. Time to start the actual app!

### 1 hour

I have successfully downloaded the Android studio app for testing purposes of the expo app, however it is struggling big time on my laptop and I'm not too sure why, but is at least displaying the basics.

### 1.5 hours

Okay the initial setup of the expo app is going well. Some very annoying issues with the layout and I forgot that it is by columns instead of rows that the spacing works so spent 20 minutes trying to work that out but I have managed to get at least some sort of general layout going!

## 16 June 2024

### 0.75 hours

Well I am definitely scratching my head now. I have added a simple arrow function that logs when the pressable components are clicked and that works fine, but I am now getting an error where I have a router problem? Hmm, some debugging and googling needed.

### 1 hour

The learning curve is pretty steep but we are getting there. Managed to create a mini test dataset and then now have it displayed using a flatlist which is cool! I can understand now that each of these values in the dataset can then be contained inside their own component style to be formatted nicely, so I guess that can be next!

### 1 hour

After a little bit of chatGPT prompting and some design prompts from dad, we now have a working leaderboard that is displaying scores from a json list in order! A bit of a mess at the moment as it is all just in the one file for the globalLeaderboard but the flatlist is cool and then to actually have a bit of logic in is nice as well. I guess the next goal would be to get some sort of list for the home page display and try and switch between them, or maybe first do it for a synthetic global and local list.

## 17 June 2024

### 3 hours

Probably a cumulative 3 hours of fighting against types using typescript. I think I will just swap to javascript...

## 19 June 2024

### 0.75 hours

Somehow managed to get the navigation bar to work in a reasonably speedy manner and it is now functional on the app! Decided not to pass the data from the index and just upload it to the leaderboard screen, but this may need changed in the future. But for now it will do!

## 20 June 2024

### 1.5 hours

I have successfully got the app to be able to 'upload' a file (or at least get the location of a file stored on a variable) that should then be able to be passed to the backend to do some magic! This is where it starts to get serious because it is using tools like axios and flask that require a bit more brain power than just designing, but so far so good!

## 21 June 2024

### 1.25 hours

I have started to try and set up a Flask backend but I guess it is obvious problems I am encoutnering as when I am "hosting" the server on localhost of my machine, my phone then does not recognise this as localhost, so it really has to be a live server for this to work... Will need to look into free options!

## 27 June 2024

### 2.5 hours

Well that was some serious flow state with the coding there as time just slipped away! Managed to get some sort of file upload going and it can be accessed across multiple devices, nice!!!

## 28 June 2024

## 1.5 hours

I have now successfully got the gpx files to upload onto the local server and then have them be displayed on the home page! I guess it is getting close to the time to actually integrate the algorithm, but it may be best first to get the visuals of the activities to a suitable position and then link it up, but another step in the right direction.
