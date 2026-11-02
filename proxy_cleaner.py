import urllib.request

SOURCE_URL = "https://raw.githubusercontent.com/sportlive18/sportlink-update/main/Combined.m3u"

def clean_playlist():
    try:
        req = urllib.request.Request(
            SOURCE_URL, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')

        # Badha original headers ane Kodiprop tags sathe ni file seedhi save thase
        with open("smooth_playlist.m3u", "w", encoding="utf-8") as f:
            f.write(content)
            
        print("Playlist updated successfully with all headers!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_playlist()
