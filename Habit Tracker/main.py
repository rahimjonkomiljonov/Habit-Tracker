import requests
from datetime import datetime

USERNAME = "rahimjon"
TOKEN = "usdhcolnsdcyi792geyuw2"
GRAPH_ID = "graph0012"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN,

}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now().strftime("%Y%m%d")
# print(today)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# # pixel_params = {
# #     "date": today,
# #     "quantity": str(input("How many pages of book did you read today? >>>"))
# }
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_delete_pixel_endpoint = f"{pixel_endpoint}/{today}"
update_pixel_params = {
    "quantity": "120"
}

# response = requests.put(url=update_delete_pixel_endpoint, json=update_pixel_params, headers=headers)
#
response = requests.delete(url=update_delete_pixel_endpoint, headers=headers)