from __future__ import annotations

from typing import Optional, Tuple

from chatgpt import ChatGPT, get_bot


def get_test_bot() -> Tuple[Optional[ChatGPT], str]:
    bot: Optional[ChatGPT] = None
    init_error: str = ""
    try:
        bot = get_bot()
    except Exception as err:
        init_error = str(err)
    return (bot, init_error)
