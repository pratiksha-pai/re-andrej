import os
import requests
import re
import json

def fetch_description(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet"
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    description = data['items'][0]['snippet']['description']
    return description

def extract_chapters(description):
    pattern = r"(\d+:\d+)\s*-\s*(.*)"
    matches = re.findall(pattern, description)
    
    chapters = []
    for start_time, title in matches:
        minutes, seconds = map(int, start_time.split(":"))
        start_time_seconds = minutes * 60 + seconds
        
        chapters.append({
            "title": title.strip(),
            "start": start_time_seconds
        })
        
    return chapters

# Replace with your own YouTube API key and video ID
api_key = os.getenv("YOUTUBE_API_KEY")
video_id = os.getenv("YOUTUBE_VIDEO_ID")

description = fetch_description(video_id, api_key)
chapters = extract_chapters(description)
print(chapters)
