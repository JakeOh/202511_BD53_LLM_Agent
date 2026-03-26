from openai import OpenAI

from src.utils import get_openai_api_key


def get_gpt_response(client, messages):
    response = client.chat.completions.create(
        model='gpt-5.4-mini',
        messages=messages,
        temperature=0.9
    )

    return response.choices[0].message.content


def main():
    # OpenAI 객체 생성
    client = OpenAI(api_key=get_openai_api_key())

    # 초기 메시지 프롬프트
    messages = [
        {'role': 'system', 'content': '너는 아주 유능한 AI 비서야.'},
    ]

    while True:
        # 콘솔에서 사용자 입력을 받음
        user_input = input('user>> ')
        if user_input == 'exit':
            print('프로그램을 종료합니다...')
            break

        # 사용자가 입력한 내용을 리스트 messages에 'user' 프롬프트로 추가.
        messages.append({'role': 'user', 'content': user_input})

        # GPT 서버로 요청을 보내고 응답을 받음.
        response = get_gpt_response(client, messages)

        # GPT가 생성한 답변을 출력
        print('GPT>>', response)

        # GPT가 생성한 답변을 'assistant' 프롬프트로 추가해서 다음 질문에 사용하도록 함.
        messages.append({'role': 'assistant', 'content': response})


if __name__ == '__main__':
    main()
