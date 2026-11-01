import urllib.request

# Original repo ni m3u file no raw url
SOURCE_URL = "https://raw.githubusercontent.com/sportlive18/sportlink-update/main/Combined.m3u"

def clean_playlist():
    try:
        # Request mokli ne link fetch karo
        req = urllib.request.Request(
            SOURCE_URL, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')

        # Clean playlist ne smooth_playlist.m3u name thi save karo
        with open("smooth_playlist.m3u", "w", encoding="utf-8") as f:
            f.write(content)
            
        print("Playlist generated successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_playlist()
