import requests
from datetime import datetime

USERNAME = "arunsaini"
TOKEN = "ad79ddg0qrfj5sdkf8kn4"
GRAPH_ID = "graph1"

Pixela_endpoint = "https://pixe.la/v1/users"
user_prams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# responce = requests.post(url=Pixela_endpoint, json=user_prams)
# print(responce.text)

graph_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ichou"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# responce = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(responce.text)

pixel_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
print(today.strftime("%Y%m%d"))
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you cycling today?:")
}

responce = requests.post(url=pixel_endpoint,json=pixel_config, headers=headers)
print(responce.text)

update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{20230514}"
update_config = {
    "quantity": "25.0"
}
# resource = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(resource.text)

delete_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{20230514}"

# resource = requests.delete(url=delete_endpoint,headers=headers)
# print(resource.text)