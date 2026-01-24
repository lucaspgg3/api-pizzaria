import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZXhwIjoxNzY5NzA1NTc2fQ.MnO8cQQ-otg4WixSCSWMkhu593_wXfepRBFBwkZIYyA"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)

print(requisicao)
print(requisicao.json())