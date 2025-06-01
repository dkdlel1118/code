import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import ttk, scrolledtext, filedialog

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
    if isinstance(result, str):
        text_box.insert(tkinter.END, result)
    else:
        for song in result:
            line = f"{song['rank']:>2}. {song['title']} - {song['artist']} [{song['album']}]\n"
            text_box.insert(tkinter.END, line)

def save_to_file():
    content = text_box.get(1.0, tkinter.END).strip()
    if content:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print("파일 저장 완료:", file_path)
    else:
        print("저장할 내용이 없습니다.")

# GUI 구성
window = tkinter.Tk()
window.title("Melon Chart Top 50 Viewer")
window.geometry("600x600")

label = ttk.Label(window, text="🎵 Melon 실시간 차트 (Top 50)", font=("Helvetica", 16))
label.pack(pady=10)

btn_frame = ttk.Frame(window)
btn_frame.pack(pady=5)

button_fetch = ttk.Button(btn_frame, text="차트 가져오기", command=show_chart)
button_fetch.grid(row=0, column=0, padx=5)

button_save = ttk.Button(btn_frame, text="저장하기", command=save_to_file)
button_save.grid(row=0, column=1, padx=5)

text_box = scrolledtext.ScrolledText(window, wrap=tkinter.WORD, width=70, height=25)
text_box.pack(padx=10, pady=10)

window.mainloop()

