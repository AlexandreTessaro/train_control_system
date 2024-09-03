# tests/test_command_parser.py
import pytest
from train_control.command_parser import CommandParser

def test_valid_commands():
    CommandParser.validate_commands(["ESQUERDA", "DIREITA"])

def test_invalid_command():
    with pytest.raises(ValueError, match="Invalid command: UP"):
        CommandParser.validate_commands(["UP"])

def test_empty_command_list():
    with pytest.raises(ValueError, match="Commands should be a non-empty list"):
        CommandParser.validate_commands([])

def test_non_list_input():
    with pytest.raises(ValueError, match="Commands should be a non-empty list"):
        CommandParser.validate_commands("DIREITA")
