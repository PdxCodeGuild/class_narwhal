import streamlit as st
import requests
import json 

st.write(""" 
# Titanic Survival Predictions
## by Richard Farr
""")

# Create a 2 column layout
col1, col2 = st.beta_columns(2)
col1.header("Input")
col2.header("Predictions")

#########
# input
###########

# Get the input from the user in column 1
passenger_class = col1.radio('Passenger Class', ["First","Second","Third"])
sex = col1.radio('Sex', ["female","male"])
sibling_spouse = st.selectbox('Total Number of Siblings and Spouses', [0,1,2,3,4,5,6,7,8]) # "Sibling_Spouse": 1,
parent_child = st.selectbox('Total Number of parent and child ', [0,1,2,3,4,5,6,7,8,9]) # "Parent_Child": 0,
fare = st.slider('Fare Paid', min_value=0, max_value=515) # "Fare": 7.25,
cabin_class = st.selectbox('Cabin Class', ["A", "B", "C", "D", "E", "F", "G", "T", "U"]) # "Cabin": "Unknown"
# "Embarked": "Southampton",
# "Cabin Class": "U",
# "Title": "Mr",
# "Title Type": "Adult",
# "Family Size": 2,
# "Family Size_category": "Couple",
# "Fare_category": 1,
age_category = st.selectbox('Age Category', ["infant", "child", "teenager", "adult - young", "adult - middle aged", "adult - old"]) # "Age_category": "adult - young"



######## 
# Generate the predictions from the user input
########

url = 'https://go.rapidminer.com/am/api/deployments/464d78e9-f21c-48cb-91fa-b638cf8b565e'

myobj = {
   "data": [
    {
      "Passenger Class": passenger_class,
      "Sex": sex,
      "Age": 22,
      "Sibling_Spouse": sibling_spouse,
      "Parent_Child": parent_child,
      "Fare": 7.25,
      "Cabin": "Unknown",
      "Embarked": "Southampton",
      "Cabin Class": "U",
      "Title": "Mr",
      "Title Type": "Adult",
      "Family Size": 2,
      "Family Size_category": "Couple",
      "Fare_category": 1,
      "Age_category": "adult - young"
    }
   ]
}

x = requests.post(url, json = myobj)
# print(x.text)

prediction = x.json()
prob_survived = round((prediction.get("data")[0].get("confidence(1.00)")) * 100, 1)


######## 
# output
########


col2.write(f"Chances this person survived: {prob_survived} %")




