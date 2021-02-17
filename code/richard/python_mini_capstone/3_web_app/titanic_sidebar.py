import streamlit as st
import requests
import json 

st.write(""" 
# Titanic Survival Predictions
## by Richard Farr
""")

# Create a 2 column layout
col2 = st.beta_container()

# col1.header("Input")
col2.header("Predictions")

#########
# input
###########

# Get the input from the user in column 1

passenger_class = st.sidebar.radio('Passenger Class', ["First","Second","Third"])

sex = st.sidebar.radio('Sex', ["female","male"])
age = st.sidebar.slider('Age', min_value=0, max_value=100, value = 30)
age_category = st.sidebar.selectbox('Age Category', ["infant", "child", "teenager", "adult - young", "adult - middle aged", "adult - old"]) # "Age_category": "adult - young"
embarked = st.sidebar.radio('Embarked', ["Southampton","Cherborg", "Queenstown"]) # "Embarked": "Southampton"
cabin_class = st.sidebar.selectbox('Cabin Class', ["A", "B", "C", "D", "E", "F", "G", "T", "U"]) # "Cabin Class": "U",


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
      "Sibling_Spouse": 0,
      "Parent_Child": 0,
      "Fare": 7.25,
      "Cabin": "Unknown",
      "Embarked": embarked,
      "Cabin Class": "U",
      "Title": "Mr",
      "Title Type": "Adult",
      "Family Size": 2,
      "Family Size_category": "Couple",
      "Fare_category": 1,
      "Age_category": age_category
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




