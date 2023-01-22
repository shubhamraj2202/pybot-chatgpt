""" Python Bot using ChatGPT's API"""

from __future__ import annotations

import openai
from openai import Completion
from openai.openai_object import OpenAIObject


class ChatGPT:
    """Wrapper for ChatGPT"""

    def __init__(self, token: str, org_token: str = "", **kwargs) -> None:
        """Initiaze Args
        Args:
            token (str): Token to interact with OpenAI
            organization (str): Organization Token
        """
        openai.api_key = token
        if org_token:
            openai.organization = org_token
        self.engine = kwargs.get("engine", "text-ada-001")
        self.max_token = kwargs.get("max_tokens", 150)

    def generate_response(self, prompt: str) -> str:
        """
        Generate Response
        Args:
            prompt (str): User Prompts
        Returns:
            str: ChatGPT Response
        """
        message: str = "Request cannot be processed"
        completions: OpenAIObject = Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=self.max_token,
            n=1,
            stop=None,
            temperature=0.5,
        )
        if choices := completions.choices:
            message = choices[0].text.strip()
        return message
