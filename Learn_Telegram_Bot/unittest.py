
from unittest.mock import patch, Mock
from telegram.ext import ContextTypes
from telegram import Update
from ..src.telegramBot import show_simple_command, show_simple_command_handler

@patch('telegramBot.set_simple_cmd')
def test_set_simple_cmd(simple_cmd):
    # Given
    update = Update(1, message=Mock(text='/sim'))
    context = ContextTypes.DEFAULT_TYPE

    # When
    show_simple_command_handler(update, context)

    # Then
    simple_cmd.assert_called_once_with('123')
