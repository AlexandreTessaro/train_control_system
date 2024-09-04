import sys
import os
import pytest
from train_control.command_parser import CommandParser

# Ajusta o caminho para importar o CommandParser corretamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Testa se os comandos válidos são aceitos sem erro
def test_valid_commands():
    CommandParser.validate_commands(["ESQUERDA", "DIREITA"])

# Testa se um comando inválido gera a exceção ValueError com a mensagem esperada
def test_invalid_command():
    with pytest.raises(ValueError, match="Invalid command: UP"):
        CommandParser.validate_commands(["UP"])

# Testa se uma lista vazia de comandos gera a exceção ValueError com a mensagem esperada
def test_empty_command_list():
    with pytest.raises(ValueError, match="Commands should be a non-empty list"):
        CommandParser.validate_commands([])

# Testa se a entrada que não é uma lista gera a exceção ValueError com a mensagem esperada
def test_non_list_input():
    with pytest.raises(ValueError, match="Commands should be a non-empty list"):
        CommandParser.validate_commands("DIREITA")
