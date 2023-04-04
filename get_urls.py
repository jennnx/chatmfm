import json
import os
import google.oauth2.credentials
from googleapiclient.discovery import build

def get_youtube_videos(channel_id):
    # Set up YouTube API client
    DEVELOPER_KEY = os.environ.get('GOOGLE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

    # Get video IDs for channel uploads playlist
    playlist_id = youtube.channels().list(part='contentDetails', id=channel_id).execute()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    playlistitems_list_request = youtube.playlistItems().list(
        playlistId=playlist_id,
        part='snippet',
        maxResults=300
    )

    # Get all videos from the playlist
    videos = []
    while playlistitems_list_request:
        playlistitems_list_response = playlistitems_list_request.execute()
        for playlist_item in playlistitems_list_response['items']:
            video_url = 'https://www.youtube.com/watch?v={}'.format(playlist_item['snippet']['resourceId']['videoId'])
            video_title = playlist_item['snippet']['title']

            # Only append if video_title includes the character '#'
            if '#' in video_title:
                videos.append({'title': video_title, 'url': video_url})
        playlistitems_list_request = youtube.playlistItems().list_next(playlistitems_list_request, playlistitems_list_response)

    return videos

def main():
    channel_id = "UCyaN6mg5u8Cjy2ZI4ikWaug"
    videos = get_youtube_videos(channel_id)
    # Save videos to file
    with open('./video_urls/urls.json', 'w') as f:
      json.dump(videos, f)

if __name__ == '__main__':
    main()
