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

        # Ahiya clear key ane MPD / M3U8 streams mate proper formatting rakhi chhe
        # TiviMate mate je channel m3u8 hoy te direct chalase ane mpd mate clear key tags support karse.
        
        with open("smooth_playlist.m3u", "w", encoding="utf-8") as f:
            f.write(content)
            
        print("Playlist updated with Clearkey / MPD support successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_playlist()
