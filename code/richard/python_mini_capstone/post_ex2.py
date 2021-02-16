import requests

deployment_url = 'https://go.rapidminer.com/am/api/deployments/12d6513f-8a7b-44c3-b562-8867f59de95f'

my_input_data = {"data":[{"TV":200,"radio":0,"newspaper":100},{"TV":250,"radio":50,"newspaper":0},{"TV":300,"radio":0,"newspaper":0}]}

r = requests.post(deployment_url, json=my_input_data)

print(r.text)
# json_output = r.json()
# print(json_output)