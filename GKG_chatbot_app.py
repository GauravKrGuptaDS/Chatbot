import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

st.title("Chatbot")

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

def handle_send():
    user_text = st.session_state.user_input.strip()
    if not user_text:
        return

    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_text}
    )

    # Call OpenAI
    response = client.responses.create(
        model="gpt-5.2",
        input=st.session_state.messages
    )

    ai_reply = response.output_text

    # Add assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_reply}
    )

    # Clear input SAFELY
    st.session_state.user_input = ""

# Input widget (created ONCE)
st.text_input(
    "User:",
    key="user_input",
    on_change=handle_send
)

st.caption("Press Enter to send")

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.write(f"**{msg['role'].capitalize()}:** {msg['content']}")