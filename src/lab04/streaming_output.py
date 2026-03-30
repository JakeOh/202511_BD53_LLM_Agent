from openai import OpenAI

from src.utils import get_openai_api_key


def get_gpt_response(client, messages):
    """stream=True 를 사용한 요청과 응답 처리"""
    response = client.chat.completions.create(
        model='gpt-5.4-mini',
        temperature=0.9,
        messages=messages,
        stream=True
    )

    for chunk in response:
        yield chunk.choices[0].delta.content


def main():
    client = OpenAI(api_key=get_openai_api_key())
    messages = [
        {'role': 'system', 'content': '너는 유능한 AI 비서야.'}
    ]

    while True:
        user_input = input('User>> ')
        if user_input == '/exit':
            print('Goodbye~')
            break
        # TODO


if __name__ == '__main__':
    main()
