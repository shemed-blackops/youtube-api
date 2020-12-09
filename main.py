from read_config import *
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os


def main():
    service, version, key = read_config()
    youtube = build(service, version, developerKey=key)
    pl_video = []
    playlist_id = 'PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV'

    print("Playlist ID: Default [PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV']")
    pl_id = input('> ').strip() or playlist_id

    next_page_token = None

    current_path = os.getcwd()
    file_name = 'playlist.txt'

    save_path = os.path.join(current_path, file_name)

    # Check if file exists if yes delete then create new

    os.remove(save_path) if os.path.exists(
        save_path) else open(save_path, 'w').close()

    print("Starting........")
    with open(save_path, 'a') as f:
        while True:
            pl_request = youtube.playlistItems().list(
                part='snippet',
                playlistId=pl_id,
                pageToken=next_page_token,
                maxResults=50
            )
            pl_response = pl_request.execute()
            items = pl_response['items']
            for item in items:
                video_title = item['snippet']['title']
                f.write(video_title + '\n')
                pl_video.append(video_title)

            next_page_token = pl_response.get('nextPageToken')

            if not next_page_token:
                break

        f.close()
        print("Done.......")

    return pl_video


if __name__ == "__main__":
    main()
