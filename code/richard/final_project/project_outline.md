# Are you smarter than a machine learning algorithm?
Richard Farr
April 12th, 2021

## Project Overview
I will build a web app that summarizes what happened to the passengers of the titanic in a dashboard and allows users to play a game to see how well they are able to predict who did and did not perish. It will require users to login to play the game and a leaderboard will summarize how each of the players has fared.  compare it to a machine learning algorithm. 
If people can consistantly beat the algorithm then the algo is really not that good.

The big picture is to prove to my clients that I am capable of turning data into valuable predictions and those predictions are better than the ones they can do themselves.

This project may only be a fun game but it can and should be used as a template for future client work. I see this app as a template that I can use to sell clients on the value of the predictions produced by my machine learning models. 

## Features
When the user first gets to the website they will see a dashboard that summarizes the data. They will be able to filter by the most common attributes and see how that affects that group of users chances of survival.

They will then be able to move on from just a dashboard to logging in to take a quiz that pits their predictions agains the machine learning algorithm I created. The user will get to make predictions on 10 random people and that will be compared to the ML model.

Whenever a user takes a quiz the results will be saved and added to a leaderboard. If its the 2nd or later time a user takes the quiz then all their scores will be averaged. 

## User Stories
First, its a fun game. The user wants to prove to themself that they can do better than the ML algo and their friends.

Secondly, its an upsell for clients. They don't want to pay for a predictive model that isn't as good as one of thier current employees... but which one? The boss can require the employees to take the quiz to figure out if anyone is better than the ml algo.

### Tasks
Summarize the data in an attractive dashboard
Filter the data and have the data change in the dashboard
Take a quiz
See how well you did on the quiz
See how well you did vs the ML algo 
Compare your results to everyone elses in the Dashboard

## Data Model
I see needing 2 tables.
Table 1 will be the titanic data. This will be the training data after all the missing values have been accounted for.
Table 2 is a place to store the quiz scores whenever a user takes the quiz.

## Schedule

### Milestone 1 - Thursday, April 15th
- Wireframe complete using Balsamiq
- Static outline of website up on a custom domain using Bootstrap (no back end)

### Milestone 2 - Thursday, April 22nd
- Dashboard working

### Milestone 3 - Thursday, April 29th
- Quiz working

### Milestone 4 - Wednesday, May 5th
- Leaderboard working
