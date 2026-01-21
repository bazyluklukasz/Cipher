from unittest.mock import patch

from src.menu import Menu


@patch("builtins.print")
def test_menu_show(mock_print):
    menu = Menu()
    menu.show_menu()

    assert  mock_print.call_count == len(menu.options) + 1

