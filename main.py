# Imports
from secrets import CLIENT_ID, CLIENT_SECRET
import requests
import json

username = ""

# Generate Access Token (First Run OR If Expired)
def access():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    body = "grant_type=client_credentials&client_id=" + CLIENT_ID + "&client_secret=" + CLIENT_SECRET

    response = requests.post(url, body, headers=headers)

    if response.status_code != 200:
        print("Error In Retrieving Access Token")
        return ""
    elif response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("System Error")
        return ""
    
def getCurrentUser():
    url = "https://api.spotify.com/v1/me"
    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error In Retrieving User")
        return ""
    elif response.status_code == 200:
        return response.json()["id"]
    else:
        print("System Error")
        return ""

def getPlaylists():
    url = "https://api.spotify.com/v1/users/" + username + "/playlists"

access_token = access()
user_id = getCurrentUser()
