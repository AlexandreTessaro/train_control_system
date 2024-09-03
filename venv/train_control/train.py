# train_control/train.py
class Train:
    def __init__(self):
        self.position = 0
        self.movements = 0
        self.direction_count = 0
        self.last_direction = None
    
    def move_left(self):
        if self.last_direction == 'ESQUERDA':
            self.direction_count += 1
        else:
            self.direction_count = 1
            self.last_direction = 'ESQUERDA'
        
        if self.direction_count > 20:
            raise ValueError("Too many consecutive moves in the same direction")

        if self.movements < 50:
            self.position -= 1
            self.movements += 1
        else:
            print("Maximum movement reached")
    
    def move_right(self):
        if self.last_direction == 'DIREITA':
            self.direction_count += 1
        else:
            self.direction_count = 1
            self.last_direction = 'DIREITA'
        
        if self.direction_count > 20:
            raise ValueError("Too many consecutive moves in the same direction")

        if self.movements < 50:
            self.position += 1
            self.movements += 1
        else:
            print("Maximum movement reached")
    
    def execute_commands(self, commands):
        for command in commands:
            if command == "ESQUERDA":
                self.move_left()
            elif command == "DIREITA":
                self.move_right()
            else:
                raise ValueError(f"Invalid command: {command}")
        
        return self.position
