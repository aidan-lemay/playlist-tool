# playlist-tool

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