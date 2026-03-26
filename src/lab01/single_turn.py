from openai import OpenAI

from src.utils import get_openai_api_key


def main():
    # 콘솔 창에서 사용자 입력을 받아서 질문 내용으로 사용.
    # 사용자가 exit 입력하면 프로그램 종료.
    client = OpenAI(api_key=get_openai_api_key())

    while True:  #  무한 반복문
        # 콘솔 창에서 사용자 입력을 받음.
        user_input = input('user>> ')
        if user_input == 'exit':
            print('프로그램을 종료합니다...')
            break  # 반복문 종료

        # 사용자의 입력을 GPT 서버로 보내는 메시지에 포함.
        msg = [
            {'role': 'system', 'content': '너는 아주 유능한  AI 비서야.'},
            {'role': 'user', 'content': user_input},
        ]
        response = client.chat.completions.create(
            model='gpt-5.4-mini',
            messages=msg,
            temperature=0.9
        )
        print('GPT>>', response.choices[0].message.content)
        # 이 방식(single-turn)의 단점은 GPT가 이전 대화 내용을 기억하지 못한다는 점.
        # 연속된 질문에 대해서 이전 대화 내용의 문맥이 전혀 고려되지 않은 텍스트가 생성됨.
        # messages 리스트에 이전 GPT와의 대화 내용을 모두 저장하고 요청을 보내면,
        # 이전 대화 내용의 문맥에 맞는 답변을 유도할 수 있음.


if __name__ == '__main__':
    main()
