from train_control.train import Train
from train_control.command_parser import CommandParser

def main():
    commands = ["DIREITA", "DIREITA", "ESQUERDA", "DIREITA", "DIREITA"]

    try:
        CommandParser.validate_commands(commands)
    except ValueError as e:
        print(f"Erro: {e}")
        return

    train = Train()
    final_position = train.execute_commands(commands)
    print(f"A posição final do trem é: {final_position}")

if __name__ == "__main__":
    main()
