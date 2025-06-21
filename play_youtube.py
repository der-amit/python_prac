import yt_dlp
import subprocess

def play_youtube_video(url):
    """Play YouTube video using mpv """
    output_config = {
        'format': 'best[height<=720]',  # Get best quality up to 720p
        'quiet': True,  # Suppress yt-dlp output
        'no_warnings': True
    }
    
    try:
        print("Extracting video URL...")
        with yt_dlp.YoutubeDL(output_config) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info['url']
            title = info.get('title', 'Unknown')
        
        print(f"Playing: {title}")
        print("Press 'q' in the video window to quit")
        
        # Play with mpv
        subprocess.run(['mpv', video_url])
        
    except Exception as e:
        print(f"Error: {e}")

# Test it out
myurl = input("Paste the URL:")

if __name__ == "__main__":
    # Example YouTube URL - replace with any video you want
    youtube_url = myurl
    play_youtube_video(youtube_url)
    
#sample https://www.youtube.com/watch?v=ytu7rkDBdMY 