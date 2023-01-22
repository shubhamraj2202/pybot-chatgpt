from __future__ import annotations

import builtins
from unittest.mock import patch

import pytest

from chatgpt import chatbot
from tests.context_manager import Capturing
from tests.utils import get_test_bot

bot, init_error = get_test_bot()


class TestChatGPT:
    @pytest.mark.skipif(not bot, reason=init_error)
    @patch("builtins.input")
    def test_bot(self, mock_input) -> None:
        mock_input.side_effect = ["Hello", "Exit"]
        with Capturing() as chatoutput:
            chatbot(bot)
        assert "Please ask me anything" in "".join(chatoutput)
