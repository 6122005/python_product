import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "backend"
        )
    )
)

from core import generate_reply

if "history" not in st.session_state:
    st.session_state.history = []

st.title("WhatsPilot AI")

if st.button("Clear History"):
    st.session_state.history = []
    st.success("History cleared.")

message = st.text_area(
    "Enter WhatsApp Message",
    height=180,
    placeholder="Type the incoming WhatsApp message..."
)

if st.button("Generate Reply"):

    if not message.strip():
        st.error("Please enter a message.")

    elif len(message) > 500:
        st.error("Maximum 500 characters allowed.")

    else:

        try:

            with st.spinner("Generating reply..."):

                reply = generate_reply(message)

            st.success("Reply generated successfully!")

            st.subheader("Latest Reply")

            st.code(reply)

            st.session_state.history.insert(
                0,
                {
                    "message": message,
                    "reply": reply
                }
            )

            st.session_state.history = st.session_state.history[:5]

        except Exception as e:

            st.error(str(e))

if st.session_state.history:

    st.divider()

    st.subheader("Recent Replies")

    for index, item in enumerate(st.session_state.history, start=1):

        with st.expander(f"Reply {index}"):

            st.write("### Incoming Message")

            st.write(item["message"])

            st.write("### AI Reply")

            st.code(item["reply"])