import unittest.mock

import pytest
from src.buffer import Buffer
from src.text_model import TextModel


class TestBuffer:
    @pytest.fixture
    def buffer(self):
        return Buffer()

    @pytest.fixture
    def text_model(self):
        return TextModel("asdasd", "rot13", "encrypted")

    def test_add_buffer(self, buffer, text_model):
        buffer.add(text_model)
        assert len(buffer.data) == 1
        assert text_model in buffer.data

    def test_clear_data(self, buffer, text_model):
        buffer.add(text_model)
        buffer.clear()
        assert len(buffer.data) == 0
        assert (text_model in buffer.data) is False


    def test_show_data(self, buffer, text_model, mocker):
        buffer.clear()
        mock_print = mocker.patch("builtins.print")
        buffer.add(text_model)
        buffer.show()
        assert mock_print.call_count == 2

