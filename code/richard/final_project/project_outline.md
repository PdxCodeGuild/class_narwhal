# Are You Smarter Than a Model?
Richard Farr
April 12th, 2021

## Project Overview
I will build a web app that summarizes what happened to the passengers of the titanic in a dashboard and allows users to play a game to see how well they are able to predict who did and did not perish. It will require users to login to play the game and a leaderboard will summarize how each of the players has fared.  

Humans predictions will be compared to the results of a machine learning algorithm. 

If a human can consistantly beat the algorithm then the algo is probably not worth investing in.

The big picture is to prove to my clients that I am capable of turning data into valuable predictions and those predictions are better than the ones they can do themselves.

This project may only be a fun game but it can and should be used as a template for future client work. I hope to be able to use various flavors of this app to sell clients on the value of the predictions produced by my machine learning models.

## Features
When the user first gets to the website they will see a dashboard that summarizes the data. They will be able to filter by the most common attributes and see how that affects that group of users chances of survival. This dashboard will give them a sense of the underlying raw data but they will not be able to see the underlying raw data.

They will then be able to login and take a quiz that pits their predictions against the  predictions of machine learning algorithm I created. The user will get to make predictions on 10 random people and that will be compared to the ML model.

Whenever a user takes a quiz the results will be saved and added to a leaderboard. If its the 2nd or later time a user takes the quiz then all their scores will be averaged. 

## User Stories
As a user, I want to be able to see a pretty dashbord and be able to filter the data becuase I want to understand the data better.

As a user I want to be able to take a quiz and compare my predicitons to the machine learning model and the actual results.

As a user, I want to see how I fare against others who have taken quizzes in the past via a leaderboard.

As a freelance data scientist, I want a way to prove that the machine learning models I build perform better someone just using a dashboard to make predictions.

As a freelance data scientist, I want people knocking down my door asking me to build them predictive models in exchange for lots of money.


### Tasks
- Summarize the raw data in an attractive dashboard
- Filter the data and have the data change in the dashboard accordingly.
- Take a quiz
- See how well a user did on the quiz vs
- See how well a user did compared to the machine learning model
- View a leaderboard of peoples performance in taking the quiz

## Data Model
I see needing 2 tables.
Table 1 will be the titanic data. This will be the training data after all the missing values have been accounted for.
Table 2 is a place to store results of the quiz questions for the human and ml algo whenever a user takes the quiz.

## Schedule

### Milestone 1 - Thursday, April 15th
- Wireframe complete using Balsamiq
- Github repository up and custom domain working

### Milestone 2 - Thursday, April 22nd
- Dashboard working 
- Ability to filter the dashboard based on Sex, passenger class, etc
- Apply Bootstrap to make it look decent

### Milestone 3 - Thursday, April 29th
- Require authentication in order to see the blank pages for the quiz and the leaderboard
- Quiz working

### Milestone 4 - Wednesday, May 5th
- Leaderboard working
