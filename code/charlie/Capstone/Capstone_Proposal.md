<!-- Designer: Charles Spahn
     Project: Bootcamp Capstone
     Date: 04/13/21
 -->

# Author 
- Charles Spahn
# Project Name
## __"Zellis"__ (kinda like trellis) or __"Plant-Fu"__
- Zellis is like "FarmVilleLand" but even better because you
can see the real life fruits of your labor!

# Project Overview
- My application Zellis is trying to provide people with
a way to actively track their plants' progression from seedling to bloom. They will
be able to create a profile and upload different plants with pictures.
The comment system is aimed at providing a fun, social experience around gardening
especially since the introduction of this latest pandemic. 
There's only so much gardening and a lot of time for people to be at home these days 
to offer up their sound gardening advice.

# Features/User-Stories
1. As a "User" I want to be able to signup for "Zellis" and create a profile because
I want to be able to upload my plants and track them.
- **Tasks**:
    - Create project w/necessary apps.
    - Create User model/database
    - Create signup template

2. As a "User" I want to be able to upload pictures of my plants because I want to be 
able to track their progress.
- **Tasks**:
    - Create Plant model w/image field
    - Create image upload template 
    - Filter results by date 

3. As a "User" I want to be able to comment on or like another user's plants.
- **Tasks**:
    - Create many-to-one(ForeignKey) relationships for many users to have the abiltiy to like/comment on each plant
    - Create ForeignKey relationships for one user to have many plants
    - Filter newest like or comment to top of stack
    - Create user feed with newest posts at top of feed
# Data Model
- Users
- Plants/Images
- Likes/Comments
        
# Schedule
## Weeks:
1. 

- ~~Turn in capstone proposal~~
- Build project w/models 
- Install basic front-end
2.
- Build API
- Tweak models
- Adjust front-end
3.
- Throughly test all MVP features
- Polish front-end(HTML/CSS)
4.
- Add "like to have" features
- and more testing???


