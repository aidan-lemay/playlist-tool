from secrets import CLIENT_ID, CLIENT_SECRET

import requests
from flask import Flask, request, redirect

# Spotify App credentials (get these from your Spotify Developer Dashboard)
REDIRECT_URI = 'http://localhost:5000/callback'  # The redirect URI you set in the Spotify Developer Dashboard
SCOPE = 'user-read-private user-read-email'  # Define the permissions you need

# Spotify's authorization URL and token URL
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

# Start Flask app to handle the redirect
app = Flask(__name__)

@app.route('/')
def login():
    """
    Step 1: Redirect user to Spotify's authorization page.
    """
    auth_url = f"{SPOTIFY_AUTH_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    """
    Step 2: Spotify redirects back to this route with an authorization code.
    This function handles the code and exchanges it for an access token.
    """
    code = request.args.get('code')
    
    # Exchange the authorization code for an access token
    token_response = requests.post(SPOTIFY_TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # Parse the token response
    token_data = token_response.json()
    access_token = token_data.get('access_token')
    refresh_token = token_data.get('refresh_token')

    # Optional: Use the access token to fetch user info
    user_profile = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    return f"User profile: {user_profile}, Access Token: {access_token}, Refresh Token: {refresh_token}"

if __name__ == '__main__':
    # Run the Flask app (available at http://localhost:5000)
    app.run(debug=True)
