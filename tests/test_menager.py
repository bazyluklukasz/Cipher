from unittest import mock
from unittest.mock import patch

import pytest
import buffer
from buffer import Buffer
from cipher.factory_cipher import FactoryCipher
from menu import Menu
from src.menager import Manager


class TestManager:
    def setup_method(self):
        self.mock_menu = mock.Mock()
        self.mock_factory = mock.Mock()
        self.file_handler = mock.Mock()
        self.mock_buffer = mock.Mock()

        self.manager = Manager(
            self.mock_menu,
            self.mock_factory,
            self.file_handler,
            self.mock_buffer,
        )

    @patch('builtins.input', side_effect=["rot13", "text do kodowania"])
    def test_encode(self, mock_input):
        mock_cipher = mock.Mock()
        mock_cipher.encode.return_value = "text do kodowania"

        self.mock_factory.create_cipher.return_value = mock_cipher
        self.mock_factory.AVAILABLE_ROT_CIPHERS = ["rot13", "rot47"]

        self.manager.encode()

        self.mock_factory.create_cipher.assert_called_with("rot13")

        added_obj = self.mock_buffer.add.call_args[0][0]

        assert added_obj.text == "text do kodowania"
        assert added_obj.rot_type == "rot13"
        assert added_obj.status == "encrypted"

    @patch('builtins.input', side_effect=["rot47", "text do odkodowania"])
    def test_decode(self, mock_input):
        mock_cipher = mock.Mock()
        mock_cipher.decode.return_value = "text do odkodowania"

        self.mock_factory.create_cipher.return_value = mock_cipher
        self.mock_factory.AVAILABLE_ROT_CIPHERS = ["rot13", "rot47"]

        self.manager.uncode()

        self.mock_factory.create_cipher.assert_called_with("rot47")

        add_obj = self.mock_buffer.add.call_args[0][0]

        assert add_obj.text == "text do odkodowania"
        assert add_obj.rot_type == "rot47"
        assert add_obj.status == "decrypted"

    @patch('builtins.input', side_effect=["1"])
    def test_save_all(self, mock_input):
        test_data = {"text": "text do buffer", "rot_type": "rot13", "status": "encrypted"}
        self.mock_buffer.data = test_data

        self.manager.save()

        self.file_handler.save_all.assert_called_with(test_data)

    @patch('builtins.input', side_effect=["2"])
    def test_save_append(self, mock_input):
        test_data = {"text": "text do buffer", "rot_type": "rot13", "status": "encrypted"}
        self.mock_buffer.data = test_data

        self.manager.save()

        self.file_handler.append_json.assert_called_with(test_data)

    def test_show_buffer(self):
        self.manager.show_buffer()

        self.mock_buffer.show.assert_called_once()

    def test_clear_data(self):
        self.manager.clear()

        self.mock_buffer.clear.assert_called_once()

    def test_load_buffer(self):
        test_data = {"text": "text do buffer", "rot_type": "rot13", "status": "encrypted"}
        self.file_handler.load_json.return_value = test_data

        self.manager.load_buffer()

        self.mock_buffer.add.assert_called_with(test_data)



