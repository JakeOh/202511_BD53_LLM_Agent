import streamlit as st
from openai import OpenAI

from src.utils import get_openai_api_key


def initialize_client():
    # OpenAI 객체를 생성하고 리턴하는 함수
    client = OpenAI(api_key=get_openai_api_key())
    return client


def get_gpt_response(client, messages):
    # OpenAI client를 사용해서 메시지를 보내고 생성된 텍스트를 응답받음.
    response = client.chat.completions.create(
        model='gpt-5.4-mini',
        messages=messages,
        temperature=0.9
    )
    return response.choices[0].message.content



def main():
    client = initialize_client()

    # title 위젯 생성
    st.title('GPT를 사용한 첫번째 챗봇')

    # st.session_state: streamlit 앱이 실행 중에 계속 유지되어야 할 값들을 저장하는 객체.
    # 일반적인 지역 변수들을 화면이 갱신될 때마다 초기화되기 때문에 값을 계속 유지할 수 없음.
    # st.session_state는 값들을 dict처럼 key-value 아이템으로 저장.
    # st.session_state['key'] = value 가능.
    # st.session_state.key = value 가능.
    # 'messages' 키가 st.session_state에 저장되어 있지 않으면, 메시지 프롬프트를 초기화
    if 'messages' not in st.session_state:
        # st.session_state['messages'] = [
        #     {'role': 'assistant', 'content': '무엇을 도와드릴까요?'}
        # ]
        st.session_state.messages = [
            {'role': 'assistant', 'content': '무엇을 도와드릴까요?'}
        ]

    # st.session_state에 저장된 리스트 messages에서 메시지(dict 객체)를 하나씩 반복.
    for msg in st.session_state.messages:
        # 채팅 메시지 위젯 아이콘 설정, 내용을 마크다운으로 출력.
        st.chat_message(msg['role']).markdown(msg['content'])

    # 사용자 입력창 위젯을 출력
    # user_input = st.chat_input('질문을 입력하세요...')
    # if user_input:  # 사용자 입력 텍스트가 있는 경우
    #     st.text(user_input)  # 화면에 텍스트 출력
    if user_input := st.chat_input('질문을 입력하세요...'):
        # 사용자 아이콘, 사용자가 입력한 내용을 채팅 메시지 위젯으로 출력
        st.chat_message('user').markdown(user_input)

        # 사용자가 입력한 내용을 dict로 만들어서 st.session_state에 저장하고 있는 messages 리스트에 추가(append)
        st.session_state.messages.append(
            {'role': 'user', 'content': user_input}
        )

        # st.session_state가 가지고 있는 메시지 리스트를 GPT 서버로 보내서 생성된 답변을 응답으로 받음.
        answer = get_gpt_response(client, st.session_state.messages)

        # AI의 답변을 채팅 메시지 위젯으로 출력
        st.chat_message('assistant').markdown(answer)

        # AI의 답변을 st.session_state의 메시지 리스트에 'assistant' 역할로 추가.
        st.session_state.messages.append(
            {'role': 'assistant', 'content': answer}
        )


if __name__ == '__main__':
    main()
