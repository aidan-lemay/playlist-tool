from keys import CLIENT_ID, CLIENT_SECRET

import requests
from flask import Flask, request, redirect
from threading import Timer

# Spotify App credentials (get these from your Spotify Developer Dashboard)
REDIRECT_URI = 'http://localhost:5000/callback'  # The redirect URI you set in the Spotify Developer Dashboard
SCOPE = 'user-read-private user-read-email'  # Define the permissions you need

# Spotify's authorization and token URLs
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

# Flask app to handle the authentication process
app = Flask(__name__)

def shutdown_server():
    """Function to stop the Flask server."""
    func = request.environ.get('werkzeug.server.shutdown')
    if func is not None:
        func()

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
    Step 2: Spotify redirects back with an authorization code.
    Handle the code, exchange it for an access token, display info in the console, and shut down the server.
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

    token_data = token_response.json()
    access_token = token_data.get('access_token')
    refresh_token = token_data.get('refresh_token')

    # Optional: Use the access token to fetch user profile information
    user_profile = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": f"Bearer {access_token}"
    }).json()

    # Print the tokens and user profile in the console
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)
    print("User Profile:", user_profile)

    # Schedule the shutdown of the server after 1 second
    Timer(1, shutdown_server).start()

    # Notify the user in the browser
    return "<h1>Authentication complete. Please return to the application window. The program will now exit.</h1>"

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)