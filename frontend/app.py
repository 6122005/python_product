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
    "Enter WhatsApp Message"
)

if st.button("Generate Reply"):

    reply = generate_reply(message)

    st.subheader("Generated Reply")

    st.write(reply)