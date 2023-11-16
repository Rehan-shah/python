import requests
import datetime as dt

piela_endpoint = "https://pixe.la/v1/users"

userr_params = {
    "token" : "heijfeeiejfej29939133fjj39fj393",
    'username': "rehansnehalshah",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}


# resposne = requests.post(url=piela_endpoint  , json=userr_params)
# print(resposne.text)


# graph_endpoint = f"{piela_endpoint}/{userr_params['username']}/graphs"

# graph_config = {
#     "id": "graph2",
#     "name": "Cycling graph",
#     "unit": 'Km',
#     "type":"float",
#     "color": "ajisai"
# }
#

headers = {
    "X-USER-TOKEN" : userr_params["token"]
}
#
#
#
# # res = requests.post(url=graph_endpoint ,json=graph_config , headers=headers)
#
#
# add_pi = {
#     "date": dt.datetime.now().strftime("%y%m%d"),
#     "quantity" : "10"
# }
#
# res = requests.post(url="https://pixe.la/v1/users/rehansnehalshah/graphs/graph1/" , 
#                     json=add_pi,
#                     headers=headers)



update_pi = {
    "quantity": "15"
}
res = requests.put(url=f"{piela_endpoint}/{userr_params['username']}/graphs/graph1/20230702",
                    json=update_pi,
                    headers=headers)
print(res.text)



res = requests.delete(url=f"{piela_endpoint}/{userr_params['username']}/graphs/graph1/20230702" , headers = headers)


print(res.text)
