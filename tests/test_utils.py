import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import types
import pytest
sys.modules["settings"] = types.SimpleNamespace(bot_token="")

from utils import message_is_forwarded_from_another_chat


def test_message_is_forwarded_true():
    message = types.SimpleNamespace(forward_from_chat=types.SimpleNamespace(username="other"))
    assert message_is_forwarded_from_another_chat(message, "mychannel") is True


def test_message_is_forwarded_false():
    message_no_forward = types.SimpleNamespace()
    assert message_is_forwarded_from_another_chat(message_no_forward, "mychannel") is False

    message_same_chat = types.SimpleNamespace(forward_from_chat=types.SimpleNamespace(username="mychannel"))
    assert message_is_forwarded_from_another_chat(message_same_chat, "mychannel") is False
