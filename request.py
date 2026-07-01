import requests


def get_toss_access_token():
    # 1. API 엔드포인트 URL 설정
    url = "openapi.tossinvest.com/oauth2/token"

    # 2. HTTP 헤더 설정
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    # 3. 요청 바디 데이터 (본인의 실제 키 값으로 변경하세요)
    payload = {
        "grant_type": "client_credentials",
        "client_id": "tsck_live_aUMfHeVefROEbHnQdj7BZj",
        "client_secret": "tssk_live_FXlfyBhjfJWSYzMElf2ysRi8UM8a6Cm4C3x2mhvJTmcA",
    }

    try:
        # 4. POST 요청 보내기
        # requests.post에서 data= 인자에 딕셔너리를 넣으면 자동으로 x-www-form-urlencoded 형식으로 인코딩됩니다.
        response = requests.post(url, headers=headers, data=payload)

        # HTTP 상태 코드가 200(성공)인지 확인
        if response.status_code == 200:
            token_data = response.json()  # JSON 응답을 파이썬 딕셔너리로 변환
            return token_data.get("access_token")
        else:
            print(f"토큰 발급 실패 (상태 코드: {response.status_code})")
            print(f"에러 메시지: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"네트워크 연결 오류 발생: {e}")
        return None


# 함수 실행 테스트
if __name__ == "__main__":
    token = get_toss_access_token()

    if token:
        print("🎉 토큰 발급 성공!")
        print(f"발급된 토큰: {token}")

        # [참고] 이후 다른 API를 호출할 때 헤더 구성 예시
        # api_headers = {
        #     "Authorization": f"Bearer {token}",
        #     "Content-Type": "application/json"
        # }