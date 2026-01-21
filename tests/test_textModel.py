from src.textModel import TextModel
import pytest


class TestTextModel:
    def test_create_object(self):
        textModel = TextModel("test_string","test_rot", "test_status")
        assert isinstance(textModel, TextModel)


    def test_to_dict(self):
        textModel = TextModel("test_string","test_rot", "test_status")

        assert textModel.to_dict() == {
            "text": "test_string",
            "rot_type": "test_rot",
            "status": "test_status"
        }

    
    def test_show_obj(self):
        textModel = TextModel("test_string","test_rot", "test_status")

        assert str(textModel) == "test_string test_rot test_status"