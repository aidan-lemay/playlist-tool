# playlist-tool

### Environment:
* `python3 -m venv ../venv/playlist`
* `source ../venv/playlist/bin/activate`

### Features:
* Liked Songs Backup to JSON
    * Future: Liked Songs Restore From JSON
* Selected Playlists Merge To Existing / New Playlist
    * Run On Schedule
* Export Playlists to JSON
    * Future: Upload Playlist From JSON
* Cleanup Duplicate Songs in Playlist / Library

### Flow:
* Launch application
* Check if auth key is saved locally
* NO: 
    * Log in with Spotify, retrieve auth key
    * Save auth key somewhere local
* YES:
    * Redirect to main application menu

### Considerations:

- Oauth seems to need a browser to authenticate. Maybe this needs to be a webapp instead of a console app.
    - Am I able to run it headless if this is the case? Can I generate some kind of user key on my spotify account to hardcode it?
