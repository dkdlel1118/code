import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import ttk, scrolledtext

def get_melon_chart_top50():
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        song_rows = soup.select('#frm > div > table > tbody > tr[data-song-no]')

        top_50_songs = []
        for i, row in enumerate(song_rows):
            if i >= 50:
                break
            rank = i + 1
            title = row.select_one('div.ellipsis.rank01 a').text.strip()
            artist = row.select_one('div.ellipsis.rank02 a').text.strip()
            album = row.select_one('div.ellipsis.rank03 a').text.strip()

            top_50_songs.append({
                'rank': rank,
                'title': title,
                'artist': artist,
                'album': album
            })
        return top_50_songs

    except Exception as e:
        return f"Error: {e}"

def show_chart():
    result = get_melon_chart_top50()
    text_box.delete(1.0, tkinter.END)
    if isinstance(result, str):  # 오류 메시지
        text_box.insert(tkinter.END, result)
    else:
        for song in result:
            line = f"{song['rank']:>2}. {song['title']} - {song['artist']} [{song['album']}]\n"
            text_box.insert(tkinter.END, line)

# tkinter GUI 구성
window = tkinter.Tk()
window.title("Melon Chart Top 50 Viewer")
window.geometry("600x400")

label = ttk.Label(window, text="🎵 Melon 실시간 차트 (Top 50)", font=("Helvetica", 16))
label.pack(pady=10)

button = ttk.Button(window, text="차트 가져오기", command=show_chart)
button.pack(pady=5)

text_box = scrolledtext.ScrolledText(window, wrap=tkinter.WORD, width=70, height=25)
text_box.pack(padx=10, pady=10)

window.mainloop()
