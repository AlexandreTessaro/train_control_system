# tests/test_train.py
import pytest
from train_control.train import Train

def test_initial_position():
    train = Train()
    assert train.position == 0

def test_move_right():
    train = Train()
    train.move_right()
    assert train.position == 1

def test_move_left():
    train = Train()
    train.move_left()
    assert train.position == -1

def test_max_movements():
    train = Train()
    for _ in range(50):
        train.move_right()
    assert train.position == 50
    train.move_right()  # Should not move
    assert train.position == 50

def test_max_movements():
    train = Train()
    for _ in range(10):  # Move 10 times to the right
        train.move_right()
    for _ in range(10):  # Move 10 times to the left
        train.move_left()
    for _ in range(10):  # Move 10 times to the right again
        train.move_right()
    for _ in range(10):  # Move 10 times to the left again
        train.move_left()
    for _ in range(10):  # Move 10 times to the right to reach 50 moves
        train.move_right()

    assert train.position == 10  # After 50 moves, the position should be 10 (net right movement)

    train.move_right()  # Should not move further
    assert train.position == 10  # Position should remain the same after hitting the 50 move limit


def test_execute_commands():
    train = Train()
    assert train.execute_commands(["DIREITA", "DIREITA"]) == 2
    assert train.execute_commands(["ESQUERDA"]) == 1
