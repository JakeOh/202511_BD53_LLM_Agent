from datetime import datetime
import pytz  # 타임존 관련 모듈

from src.utils import openai_client as client

# print(pytz.common_timezones)  # 흔히 사용되는 타임존 문자열(예: Asia/Seoul) 목록 출력
# print(pytz.all_timezones)  # 모든 타임존 문자열 목록

def get_current_time(timezone):
    tz = pytz.timezone(timezone)  # 타임존 문자열(예: Asia/Seoul)을 전달받아서 timezone 객체를 생성.
    now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    return now


def get_gpt_response(messages, tools=None):
    response = client.chat.completions.create(
        model='gpt-5.4-mini',
        tools=tools,
        messages=messages
    )
    print(response.to_json())
    print('\n' + '-' * 50 + '\n')

    return response


def main():
    # print('서울:', get_current_time('Asia/Seoul'))
    # print('런던:', get_current_time('Europe/London'))
    # print('미국 동부:', get_current_time('US/Eastern'))

    # 초기 시스템 프롬프트만 설정
    messages = [
        { 'role': 'system', 'content': '너는 유능한 AI 비서야.' }
    ]

    while True:  # 무한 반복문
        if user_prompt := input('User>> '):  # 사용자가 질문을 입력했을 때
            if user_prompt.strip() == '':  # 사용자가 입력한 내용(문자열)이 없을 때
                continue  # 반복문의 시작부분으로 감.
            if user_prompt.strip() == '/exit':
                print('Goodbye~')
                break  # 반복문을 종료


if __name__ == '__main__':
    main()
