import requests
import config
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": config.pixela_token,
    "username" : config.pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create Pixela user
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# Create new graph
graph_endpoint = f"{pixela_endpoint}/{config.pixela_username}/graphs"

graph_config = {
    "id": config.graph_id,
    "name": config.graph_name,
    "unit": "minutes",
    "type": "float",
    "color": "sora"
}

# Authentication header
headers = {
    "X-USER-TOKEN": config.pixela_token
}

# Create new graph
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Post a pixel
pixel_endpoint = f"{pixela_endpoint}/{config.pixela_username}/graphs/{config.graph_id}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30"
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

# Update data
update_endpoint = f"{pixela_endpoint}/{config.pixela_username}/graphs/{config.graph_id}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "30"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# Delete data - same as update endpoint
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
