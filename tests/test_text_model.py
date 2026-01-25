from src.text_model import TextModel


class TestTextModel:
    def test_create_object(self):
        text_model = TextModel("test_string","test_rot", "test_status")
        assert isinstance(text_model, TextModel)


    def test_to_dict(self):
        text_model = TextModel("test_string","test_rot", "test_status")

        assert text_model.to_dict() == {
            "text": "test_string",
            "rot_type": "test_rot",
            "status": "test_status"
        }

    
    def test_show_obj(self):
        text_model = TextModel("test_string","test_rot", "test_status")

        assert str(text_model) == "test_string test_rot test_status"