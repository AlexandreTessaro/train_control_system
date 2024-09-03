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
    train.move_right()  
    assert train.position == 50

def test_max_movements():
    train = Train()
    for _ in range(10): 
        train.move_right()
    for _ in range(10): 
        train.move_left()
    for _ in range(10):  
        train.move_right()
    for _ in range(10):  
        train.move_left()
    for _ in range(10):  
        train.move_right()

    assert train.position == 10  

    train.move_right()  
    assert train.position == 10  


def test_execute_commands():
    train = Train()
    assert train.execute_commands(["DIREITA", "DIREITA"]) == 2
    assert train.execute_commands(["ESQUERDA"]) == 1
