import requests  # 웹사이트에 요청을 보내기 위한 라이브러리
from bs4 import BeautifulSoup  # HTML 데이터를 분석하기 위한 라이브러리

# 사용자로부터 지역명을 입력받음
location = input("지역을 입력하세요 (예: 서울, 대전, 부산): ")

# 입력받은 지역명을 기반으로 네이버 날씨 검색 URL 생성
url = f"https://search.naver.com/search.naver?query={location}+날씨"

# 네이버 날씨 페이지에 요청을 보내고 응답 데이터를 가져옴
response = requests.get(url)
# HTML 응답 데이터를 BeautifulSoup 객체로 변환하여 분석 준비
soup = BeautifulSoup(response.text, "html.parser")

# 날씨 정보를 찾는 부분
try:
    # 현재 온도 정보를 가져옴
    temperature = soup.select_one("div.temperature_text").text.strip()
    # 현재 날씨 상태 정보를 가져옴
    weather = soup.select_one("span.weather.before_slash").text.strip()
    # 어제와 비교한 온도 변화를 가져옴
    temperature_down = soup.select_one("span.temperature.down").text.strip()

    # 가져온 날씨 정보를 출력
    print(f"\n[{location} 날씨 정보]")
    print(f"현재 온도: {temperature}")
    print(f"현재 상태: {weather}")
    print(f"어제보다: {temperature_down}")
# 예외 처리: 날씨 정보를 가져오지 못했을 때 메시지 출력
except:
    print("날씨 정보를 가져오지 못했습니다. 지역명을 다시 확인해주세요.")