from datetime import datetime  # datetime 모듈(py)에서 datetime 클래스 이름을 가져옴.

from src.utils import openai_client as client


def get_current_time():
    # 현재 날짜와 시간을 '2026-04-01 11:12:30' 형식의 문자열로 만듦.
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(now)
    return now


def get_gpt_response(messages, tools=None):
    response = client.chat.completions.create(
        model='gpt-5.4-mini',   # LLM 모델 선택
        messages=messages,      # LLM 모델에게 전송하는 메시지
        tools=tools             # LLM 모델에게 제공하는 도구 목록
    )
    print(response.to_json())
    print('\n' + '-' * 50 + '\n')

    return response


def main():
    # LLM 모델에게 제공할 도구 정의(tool definitions) 리스트.
    tools = [
        {
            'type': 'function',
            'function': {
                'name': 'get_current_time',
                'description': '해당 타임존의 날짜와 시간을 %Y-%m-%d %H:%M:%S 형식의 문자열로 반환.'
            },
        },
    ]

    # LLM 모델에게 보낼 메시지
    messages = [
        { 'role': 'system', 'content': '너는 유능한 AI 비서야.' },
        { 'role': 'user', 'content': '현재 시간은?' },
    ]

    # LLM 모델에게 메시지와 함께 우리가 가지고 있는 도구 목록을 제공.
    response = get_gpt_response(messages, tools)


if __name__ == '__main__':
    main()
    get_current_time()
