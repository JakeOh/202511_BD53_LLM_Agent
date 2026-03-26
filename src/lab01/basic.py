from openai import OpenAI

from src.utils import get_openai_api_key

if __name__ == '__main__':
    # 환경 변수에 저장된 OpenAI API 키를 읽어 옴
    api_key = get_openai_api_key()

    # OpenAI 클라이언트: GPT로 질문(요청)을 보내고, 그에 대한 응답(답변)을 전달받는 객체.
    # OpenAI 클라이언트 객체 생성.
    client = OpenAI(api_key=api_key)

    # OpenAI 클라이언트를 사용해서 GPT에 chat completions 요청을 보냄.
    response = client.chat.completions.create(
        # GPT 모델(버전) 지정: gpt-4o-mini($0.15), gpt-5-mini($0.25), gpt-5.4-mini($0/75)
        model='gpt-5.4-mini',
        temperature=0.9,
        messages=[
            {
                'role': 'system',
                'content': '너는 나를 도와주는 인공지는 비서야.'
            },
            {
                'role': 'user',
                'content': '넌 누구니?'
            }
        ]
    )
    print(response)  #> ChatCompletion 객체
    print('-' * 30)
    print(response.choices)  #> list
    print(len(response.choices))  #> list의 아이템 개수 1개.
    print(response.choices[0])  #> Choice 객체
    print(response.choices[0].message)  #> ChatCompletionMessage 객체
    print('-' * 30)
    print(response.choices[0].message.content)  #> GPT 서버에서 보내준 답변
