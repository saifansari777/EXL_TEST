import requests

url = "https://reqres.in/api/users"

response  = requests.get(url, params={"page":1})

data = response.json()

pages = data["total_pages"]

total_users = 0

for page in range(1, pages+1):

    resp = requests.get(url, params={"page":page})

    resp_data = resp.json()

    users_count = len(resp_data["data"])

    total_users += users_count

print(f"The Total Number Of User Is {total_users}")