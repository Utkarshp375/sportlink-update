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

        lines = content.splitlines()
        new_lines = []
        
        for line in lines:
            if line.startswith("http"):
                if "|" not in line:
                    # JioTV mate exact headers je thi 403 error na ave
                    if "jiotv" in line.lower() or "jio" in line.lower():
                        line = line + "|User-Agent=JioTV&Referer=https://jiotv.jio.com/"
                    else:
                        line = line + "|User-Agent=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)"
            new_lines.append(line)

        with open("smooth_playlist.m3u", "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
            
        print("JioTV and Fancode headers updated successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_playlist()
