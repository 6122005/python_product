from prompts import SYSTEM_PROMPT
from llm import ask_llm


def generate_reply(message):

    prompt = f"""
{SYSTEM_PROMPT}

Incoming Message:

{message}

Reply:
"""

    return ask_llm(prompt)