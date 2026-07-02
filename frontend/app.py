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

st.title("WhatsPilot AI")

message = st.text_area(
    "Enter WhatsApp Message",
    height=180,
    placeholder="Type the incoming WhatsApp message here..."
)

if st.button("Generate Reply"):

    # Empty input validation
    if not message.strip():
        st.error("Please enter a message.")
    
    # Character limit
    elif len(message) > 500:
        st.error("Message is too long. Maximum 500 characters.")

    else:
        try:

            with st.spinner("Generating reply..."):

                reply = generate_reply(message)

            st.success("Reply generated successfully!")

            st.subheader("Generated Reply")

            st.write(reply)

        except Exception as e:

            st.error(f"Something went wrong:\n{e}")