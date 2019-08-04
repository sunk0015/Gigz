import requests

url = "https://accounts.google.com/o/oauth2/v2/auth"

querystring = {"client_id":"426488675928-3apqd7ln7aslf5ojlkio9lc6t7p7rd9a.apps.googleusercontent.com","redirect_uri":"http://localhost:8000/auth/google/","response_type":"token","scope":"profile"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "40a0e610-1587-4ec3-b219-40de2423282f"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
