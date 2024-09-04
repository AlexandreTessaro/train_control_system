from train_control.train import Train
from train_control.command_parser import CommandParser

def main():
    commands = []
    consecutive_count = 0
    total_moves = 0
    last_command = None

    while True:
        command = input("Digite o comando (ESQUERDA ou DIREITA) ou 'sair' para finalizar: ").upper()
        if command == 'SAIR':
            break
        elif command in ["ESQUERDA", "DIREITA"]:
            if command == last_command:
                consecutive_count += 1
                if consecutive_count >= 20:
                    print(f"Você já fez 20 movimentos consecutivos para {command}. Por favor, altere a direção.")
                    continue
            else:
                consecutive_count = 1
                last_command = command

            commands.append(command)
            total_moves += 1

            if total_moves >= 50:
                print("Você atingiu o limite de 50 movimentos. O trem parou.")
                break
        else:
            print("Comando inválido. Digite 'ESQUERDA', 'DIREITA' ou 'sair'.")

    try:
        # Validação dos comandos coletados
        CommandParser.validate_commands(commands)

    except ValueError as e:
        print(f"Erro: {e}")
        return

    if commands:
        train = Train()
        final_position = train.execute_commands(commands)
        print(f"A posição final do trem é: {final_position}")
    else:
        print("Nenhum comando foi fornecido.")

if __name__ == "__main__":
    main()
