import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv
load_dotenv()

# タイトル
st.title("Streamlit Chat")

# ChatBedrock インスタンスを作成
chat = ChatOpenAI(
    temperature=1,
    model="gpt-4o-mini",
    streaming=True,
)

# メッセージを定義
messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
]

# チャット入力欄を定義
if prompt := st.chat_input("質問を入力してください"):
    messages.append(HumanMessage(content=prompt))

    # ユーザーの入力を画面表示
    with st.chat_message("user"):
        st.markdown(prompt)

    # モデルの呼び出しと結果の画面表示
    with st.chat_message("assistant"):
        st.write_stream(chat.stream(messages))
