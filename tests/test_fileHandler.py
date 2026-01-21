import tempfile
from unittest.mock import patch

from src.file_handler import FileHandler
from textModel import TextModel


class TestFileHandler:

    def test_load_json(self):
        handler = FileHandler()
        test_obj = [TextModel(text="test", rot_type="rot13", status="decrypted")]
        test_obj2 = [TextModel(text="test", rot_type="rot13", status="decrypted")]

        with tempfile.NamedTemporaryFile(suffix=".json") as temp:
            with patch("builtins.input", return_value=temp.name):
                handler.save_all(test_obj)

            with patch("builtins.input", return_value=temp.name):
                load_file = handler.load_json()

        assert  len(load_file) == 1
        assert  load_file[0].text == "test"
        assert load_file[0].rot_type == "rot13"
        assert load_file[0].status == "decrypted"

#test

    def test_save_all(self):
        handler = FileHandler()
        test_obj = [TextModel(text="test1", rot_type="rot13", status="decrypted")]
        test_obj2 = [TextModel(text="test2", rot_type="rot13", status="decrypted")]
        test_obj3 = [TextModel(text="test3", rot_type="rot13", status="decrypted")]
        test_obj_all = test_obj + test_obj2 + test_obj3

        with tempfile.NamedTemporaryFile(suffix=".json") as temp:
            with patch("builtins.input", return_value=temp.name):
                handler.save_all(test_obj_all)

            with patch("builtins.input", return_value=temp.name):
                load = handler.load_json()


        assert len(load) == 3
        assert load[1].text == "test2"
        assert load[2].status == "decrypted"


    def test_append(self):
        handler = FileHandler()
        test_obj1 = [TextModel(text="test1", rot_type="rot131", status="decrypted")]
        test_obj2 = [TextModel(text="test2", rot_type="rot132", status="decrypted")]

        with tempfile.NamedTemporaryFile(suffix=".json") as temp:
            with patch("builtins.input", return_value=temp.name):
                handler.save_all(test_obj1)

            with patch("builtins.input", return_value=temp.name):
                handler.append_json(test_obj2)


            with patch("builtins.input", return_value=temp.name):
                load = handler.load_json()


            assert len(load) == 2
            assert load[1].text == "test2"