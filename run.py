from spotify_client import SpotifyClient
from youtube_client import YouTubeClient


def run():

    # Youtube credentials
    youtube_client = YouTubeClient('./creds/client_secret.json')

    #Spotify authentication token
    spotify_client = SpotifyClient(
        'SPOTIFY_AUTH_TOKEN')

    #Get the list of playlists
    playlists = youtube_client.get_playlists()

    #Print the name of playlists
    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")

     #Choose the playlist you want
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    #Get the list of songs
    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(songs)}")

    #Search and add the song
    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist} - {song.track} to your Spotify Liked Songs")


if __name__ == '__main__':
    run()
