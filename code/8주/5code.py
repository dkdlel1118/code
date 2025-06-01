import requests  # 웹사이트에 요청을 보내기 위한 라이브러리
from bs4 import BeautifulSoup  # 웹사이트의 HTML을 분석하기 위한 라이브러리

# 멜론 차트에서 상위 50곡의 정보를 가져오는 함수
def get_melon_chart_top50():
    # 멜론 차트 URL
    url = "https://www.melon.com/chart/index.htm"
    # 웹 브라우저처럼 보이게 하기 위한 헤더 정보
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 멜론 차트 페이지에 요청을 보내고 응답을 받음
        response = requests.get(url, headers=headers)
        # 요청이 성공하지 않으면 예외를 발생시킴
        response.raise_for_status()
        # HTML 응답을 분석할 수 있도록 BeautifulSoup 객체로 변환
        soup = BeautifulSoup(response.text, 'html.parser')
        # 멜론 차트에서 노래 정보가 있는 테이블의 행들을 선택
        song_rows = soup.select('#frm > div > table > tbody > tr[data-song-no]')

        # 상위 50곡 정보를 저장할 리스트
        top_50_songs = []
        # 노래 정보를 하나씩 처리
        for i, row in enumerate(song_rows):
            # 50곡까지만 처리
            if i >= 50:
                break

            # 순위 계산 (0부터 시작하므로 1을 더함)
            rank = i + 1
            # 노래 제목 가져오기 (없으면 "Unknown Title"로 설정)
            title_element = row.select_one('div.ellipsis.rank01 a')
            title = title_element.text.strip() if title_element else "Unknown Title"
            # 가수 이름 가져오기 (없으면 "Unknown Artist"로 설정)
            artist_element = row.select_one('div.ellipsis.rank02 a')
            artist = artist_element.text.strip() if artist_element else "Unknown Artist"
            # 앨범 이름 가져오기 (없으면 "Unknown Album"로 설정)
            album_element = row.select_one('div.ellipsis.rank03 a')
            album = album_element.text.strip() if album_element else "Unknown Album"

            # 노래 정보를 딕셔너리로 저장하고 리스트에 추가
            top_50_songs.append({
                'rank': rank,
                'title': title,
                'artist': artist,
                'album': album
            })
        # 상위 50곡 리스트 반환
        return top_50_songs

    # 요청 중 문제가 발생했을 때 처리
    except requests.exceptions.RequestException as e:
        print(f"멜론 차트 요청 중 오류 발생: {e}")
        return None
    # HTML 구조가 변경되어 데이터를 찾을 수 없을 때 처리
    except AttributeError:
        print("예상한 요소를 찾을 수 없습니다. 웹사이트 구조가 변경되었을 수 있습니다.")
        return None

# 프로그램의 시작점
if __name__ == "__main__":
    # 멜론 차트 상위 50곡 가져오기
    melon_top50 = get_melon_chart_top50()
    # 가져온 데이터가 있으면 출력
    if melon_top50:
        print("멜론 차트 Top 50:")
        for song in melon_top50:
            print(f"순위: {song['rank']}, 제목: {song['title']}, 가수: {song['artist']}, 앨범: {song['album']}")
    # 데이터를 가져오지 못했을 때 메시지 출력
    else:
        print("멜론 차트 Top 50을 가져오지 못했습니다.")