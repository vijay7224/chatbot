
import nltk
import random
import streamlit as st



pairs = [
    ["hello", ["hii", "Hello!"]],
    ["hii", ["hii", "Hello!"]],
    ["how are you", ["I am fine, thank you!"]],
    ["bye", ["Goodbye!", "See you later!"]],
    ["your name", ["I am NLP chatbot!"]],
    ["your creater name",["I am created by vijay surywanshi!"]]
]


def process(text):
    return nltk.word_tokenize(text.lower())


def abcd(user_input):
    tokens = process(user_input)
    for pattern, responses in pairs:
        if pattern in " ".join(tokens):
            return random.choice(responses)
    return "Sorry, I didn't understand that."


st.set_page_config(page_title="NLP Chatbot")
st.title("NLP Chatbot")


if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        bot_reply = abcd(user_input)
        st.session_state["messages"].append(("You", user_input))
        st.session_state["messages"].append(("Bot", bot_reply))


for sender, msg in st.session_state["messages"]:
    if sender == "You":
        st.markdown(f"#### :orange[{sender}:  -{msg}]")
    else:
        st.markdown(f"#### :blue[{sender}:   -{msg}]")
