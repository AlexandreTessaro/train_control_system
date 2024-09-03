# train_control/command_parser.py
class CommandParser:
    @staticmethod
    def validate_commands(commands):
        if not isinstance(commands, list) or not commands:
            raise ValueError("Commands should be a non-empty list")
        
        valid_commands = {"ESQUERDA", "DIREITA"}
        for command in commands:
            if command not in valid_commands:
                raise ValueError(f"Invalid command: {command}")
