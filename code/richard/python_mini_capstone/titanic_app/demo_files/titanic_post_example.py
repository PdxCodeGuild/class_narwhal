
import requests
import json 

url = 'https://go.rapidminer.com/am/api/deployments/464d78e9-f21c-48cb-91fa-b638cf8b565e'

myobj = {
   "data": [
    {
      "Passenger Class": "Third",
      "Sex": "male",
      "Age": 22,
      "Sibling_Spouse": 1,
      "Parent_Child": 0,
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
print(x.text)

prediction = x.json()
prob_survived = round((prediction.get("data")[0].get("confidence(1.00)")) * 100, 1)

print(" ")
print(f"Chances this person survived: {prob_survived} %")
print(" ")
