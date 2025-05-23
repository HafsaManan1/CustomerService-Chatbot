from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage
import streamlit as st

llm = ChatOllama(model="hafsamanan/chatbot2.0", streaming=True, temperature=0)

prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

st.set_page_config(page_title="Banking Chatbot", layout="wide")
st.title("Banking Chatbot")
st.write("This chatbot answers banking-related queries.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
        st.write(message.content)

user_input = st.chat_input("Write your query..")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    history = st.session_state.chat_history[:-1]  # All previous messages except latest input

    final_prompt = prompt.format_messages(history=history, input=user_input)

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response_box = st.empty()
        full_response = ""

        for chunk in llm.stream(final_prompt):
            full_response += chunk.content
            response_box.markdown(full_response)

    st.session_state.chat_history.append(AIMessage(content=full_response))
