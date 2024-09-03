from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# chatを生成
chat = ChatOpenAI(model="gpt-4o-mini")

# メッセージ定義
messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

# モデルの呼び出し
response = chat.invoke(messages)

print(response.content)
