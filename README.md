# YouTube Video/Playlist Downloader

This Python script allows you to download YouTube videos or playlists in your desired resolution using the `yt-dlp` library. The downloaded files are saved in a folder named `downloaded_files` in the same directory as the script.

## Features

- Downloads videos from YouTube in different resolutions (e.g., 720p, 1080p, etc.).
- Supports both individual video and playlist downloads.
- Saves the downloaded files to a `downloaded_files` folder within the current directory.
- Displays download progress with percentage and download speed.

## Requirements

- Python 3.x
- `yt-dlp` library

## Installation

1. **Clone or Download the Repository**:
   Clone this repository or download the script directly.

2. **Install Dependencies**:
   Ensure you have the `yt-dlp` library installed. You can install it using `pip`:

   ```bash
   pip install yt-dlp
   ```
## Usage
### Step 1: Modify the Video URL
In the script, you can directly specify the YouTube video or playlist URL.
```python
	video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your desired video URL
```
Replace the URL with the link of the video or playlist you want to download.
### Step 2: Run the Script
Once you've set the URL, you can run the script. The script will:
- Retrieve the available video resolutions (e.g., 720p, 1080p).
- Ask you to select a resolution.
- Download the video in the selected resolution.
- Save the downloaded files to a folder called `downloaded_files`.
Run the script with:
```bash
	python download.py
```
## Step 3: Download Completion
Once the video or playlist is downloaded, the files will be saved in the `downloaded_files` directory. If the folder doesn't exist, the script will automatically create it.
Example Output:
```
Available resolutions:
137: 1080p
22: 720p
18: 360p

Enter the resolution (e.g., '720p', '1080p', '480p'): 1080p
Downloading: Video Title
Downloading: 50% of Video Title.mp4 at 3.5MB/s
Downloaded: Video Title.mp4
```
Folder Structure
```
your_project_directory/
├── download_script.py  # The Python script
└── downloaded_files/   # Folder containing downloaded videos
    ├── Video Title.mp4
    └── Another Video.mp4
```
### Notes
- If the video or playlist has multiple formats, you can choose your desired resolution when prompted.
- The downloaded_files folder is created automatically if it doesn't exist.
- If you enter an invalid resolution, you have up to 3 attempts to provide a valid one.

**This project idea is not mine; I have just modified it according to my needs.**