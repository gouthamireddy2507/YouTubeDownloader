from yt_dlp import YoutubeDL
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Function to create a folder for saving downloaded files
def create_download_folder():
    download_folder = "E:\Langchain"
    
    # Check if the folder exists, and create it if it doesn't
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Folder '{download_folder}' created.")
    else:
        print(f"Folder '{download_folder}' already exists.")
    
    return download_folder

def get_available_resolutions(video_url):
    ydl_opts = {
        'no_proxy': True,
        'logger': logger,
        'proxy': None,
        'verbose': True,  
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        
        if 'entries' in info_dict:  # Check if it's a playlist
            first_video = info_dict['entries'][0]
            video_formats = first_video.get('formats', [])
            resolutions = {fmt['format_id']: f"{fmt['height']}p" for fmt in video_formats if 'height' in fmt}
        else:
            formats = info_dict.get('formats', [])
            resolutions = {fmt['format_id']: f"{fmt['height']}p" for fmt in formats if 'height' in fmt}
        
        return resolutions

def download_video_with_ytdlp(video_url, format_id, download_folder):
    ydl_opts = {
        'no_proxy': True,  # Disable proxy
        'format': f"{format_id}+bestaudio/best",
        'progress_hooks': [progress_hook],
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save to the 'downloaded_files' folder
        'logger': logger,  # Optional for logging
        'verbose': True,  # Enable verbose logging for debugging
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} of {d['filename']} at {d['_speed_str']}")
    elif d['status'] == 'finished':
        print(f"Downloaded: {d['filename']}")

def main():
    # Specify the YouTube URL directly in the code
    video_url = "https://www.youtube.com/playlist?list=PLKnIA16_RmvYhD5pqAeVu3j_jTjnTJIW2"  # Replace with your desired video URL
    
    # Create the download folder
    download_folder = create_download_folder()

    resolutions = get_available_resolutions(video_url)

    # Display available resolutions
    print("Available resolutions:")
    for fmt, height in sorted(resolutions.items(), key=lambda x: x[1], reverse=True):
        print(f"{fmt}: {height}")

    # Ask the user for the desired resolution with up to 3 attempts
    attempts = 3
    selected_format = None

    while attempts > 0:
        selected_resolution = input("Enter the resolution (e.g., '720p', '1080p', '480p'): ")
        
        # Find matching format_id for the resolution
        selected_format = next((fmt for fmt, height in resolutions.items() if height == selected_resolution), None)
        
        if selected_format:
            break  # Exit the loop if a valid resolution is selected
        else:
            attempts -= 1
            print(f"Invalid resolution selected. You have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")
            if attempts > 0:
                print("Please enter one of the available resolutions shown above.")

    if selected_format:
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            if 'entries' in info_dict:  # Check if it's a playlist
                print("Downloading playlist...")
                for entry in info_dict['entries']:
                    print(f"Downloading: {entry['title']}")
                    download_video_with_ytdlp(entry['webpage_url'], selected_format, download_folder)
            else:
                download_video_with_ytdlp(video_url, selected_format, download_folder)
    else:
        print("Too many invalid attempts. Exiting the program.")

if __name__ == "__main__":
    main()
