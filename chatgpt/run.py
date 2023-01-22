""" Python File to Invoke ChatBot"""

from __future__ import annotations

import os
from typing import Dict, Optional

from .src.bot import ChatGPT
from .src.utils import EXIT_INPUTS, HELLO_INPUTS, WELCOME_MSG


def get_tokens() -> Dict[str, str]:
    """Fetches Token from Environment Vars"""
    if not (token := os.environ.get("APIKEY_CHATGPT")) or not (
        org_token := os.environ.get("ORG_APIKEY_CHATGPT")
    ):
        raise Exception("TOKEN NOT FOUND at PATH ~/.secrets")
    return dict(token=token, org_token=org_token)


def get_bot(tokens: Optional[Dict[str, str]] = None) -> ChatGPT:
    """
    Create ChatGPT Instance
    Args:
        tokens (Dict[str, str], optional): Token reuqired by ChatGPT. Defaults to get_tokens().
    Returns:
        ChatGPT: ChatGPT Instance
    """
    if not tokens:
        tokens = get_tokens()
    return ChatGPT(token=tokens["token"], org_token=tokens["org_token"])


def chatbot(bot: Optional[ChatGPT] = None) -> None:
    """Invokes Bot and Interact with Users"""
    if not bot:
        bot = get_bot()
    idx: int = 0
    while True:
        idx += 1
        if idx == 1:
            print(WELCOME_MSG)
        print("_" * 100 + "\n")

        user_input: str = input("You:\n>> ")
        if user_input.strip().lower() in EXIT_INPUTS:
            print("\nChatbot:\n>> Goodbye! 👋\n")
            break

        if user_input.strip().lower() in HELLO_INPUTS:
            print("\nChatbot:\n>> Hello, Please ask me anything!\n")
            continue

        response: str = bot.generate_response(user_input)
        print(f"\nChatbot:\n>> {response}\n")


if __name__ == "__main__":
    chatbot()
