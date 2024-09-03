
# Sistema de controle de trens autônomos

## Projeto

Este projeto foi criado para simular um sistema de controle de trem autônomo que opera ao longo de uma trilha numérica infinita. O movimento do trem é controlado por uma série de comandos e deve aderir a restrições específicas para garantir uma operação segura e eficiente. O objetivo principal deste projeto é implementar a lógica de controle do trem, satisfazendo todas as restrições fornecidas e garantindo uma cobertura de teste abrangente

## Características

-   **Movimento direcional:** O trem pode se mover para a esquerda ou para a direita com base nos comandos que recebe.
-   **Limitação de movimento:** O trem só pode se mover um total de 50 posições por viagem.
-   **Restrição de movimento consecutivo:** o trem não pode se mover na mesma direção mais de 20 vezes consecutivas.
-   **Relatório de posição final:** o sistema fornece a posição final do trem após todos os comandos terem sido executados.
-   **Tratamento de erros:** o sistema valida comandos e fornece mensagens de erro claras para entradas inválidas ou quando restrições são violadas.

## Estrutura do Projeto



    `train_control_system/
    │
    ├── train_control/
    │   ├── __init__.py
    │   ├── command_parser.py
    │   └── train.py
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_command_parser.py
    │   └── test_train.py
    │
    ├── .gitignore
    ├── README.md
    └── venv/
        ├── ...` 

-   **train_control/** : Este diretório contém os principais arquivos de implementação.
    -   `command_parser.py`: Responsável por validar a lista de comandos.
    -   `train.py`: Implementa a `Train`classe que manipula o movimento do trem e aplica as restrições.
-   **tests/** : Contém os casos de teste unitários para validar o comportamento e a correção do sistema.
    -   `test_command_parser.py`: Contém testes para a `CommandParser`classe.
    -   `test_train.py`: Contém testes para a `Train`classe.

## Instruções de configuração

### Pré-requisitos

-   Certifique-se de que o Python esteja instalado no seu sistema.
-   Instale `pytest`para executar os casos de teste.

### 1. Clone o Repositório

Para começar, clone o repositório para sua máquina local:



`git clone https://github.com/alexandretessaro/train_control_system.git
cd train_control_system` 

### 2. Configure o ambiente virtual

Crie um ambiente virtual para gerenciar dependências do projeto:

`python -m venv venv` 

### 3. Ative o ambiente virtual

Ative o ambiente virtual usando o comando apropriado para seu sistema operacional.

-   **Windows:**
  
    
    `.\venv\Scripts\Activate.ps1` 
    
    Se você encontrar um erro de política de execução de script, execute:
    
    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` 
    
-   **macOS/Linux:**
    
    
    `source venv/bin/activate` 
    

### 4. Instalar dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

`pip install pytest` 

### 5. Execute o conjunto de testes

Para garantir que tudo esteja funcionando corretamente, execute o conjunto de testes:

`pytest -v` 

Todos os testes devem passar se a configuração tiver sido feita corretamente.

## Uso

### Classe de trem

A `Train`classe é responsável por gerenciar a posição do trem na pista e garantir que ele obedeça às restrições. A classe pode mover o trem para a esquerda ou direita e pode executar uma série de comandos.

#### Exemplo



`from train_control.train import Train
train = Train()
final_position = train.execute_commands(["DIREITA", "DIREITA", "ESQUERDA"])
print(f"The train's final position is: {final_position}")` 

### Classe CommandParser

A `CommandParser`classe é usada para validar uma lista de comandos antes que eles sejam executados pelo trem. Esta classe garante que os comandos estejam no formato correto e sejam válidos.

#### Exemplo

`from train_control.command_parser import CommandParser
commands = ["DIREITA", "ESQUERDA"]
CommandParser.validate_commands(commands)` 

## Testando

### Visão geral

Este projeto inclui um conjunto de testes unitários para garantir que todas as funcionalidades e restrições sejam implementadas corretamente e que o sistema se comporte conforme esperado em vários cenários.

### Executando os testes

Para executar todos os testes, navegue até o diretório raiz do projeto e execute:

`pytest` 

### Cobertura de teste

Os testes abrangem os seguintes aspectos:

-   **Validação de comando:** garante que o sistema identifique corretamente comandos válidos e inválidos.
-   **Restrições de movimento:** verifica se o trem atende às restrições de movimento, incluindo o número máximo de movimentos e o limite de movimentos consecutivos na mesma direção.
-   **Relatório de posição final:** verifica se a posição final do trem é informada com precisão após a execução dos comandos.

### Descrições detalhadas dos testes

-   **Testes CommandParser ( `test_command_parser.py`)**
    
    -   `test_valid_commands`: Valida se os comandos corretos são aceitos.
    -   `test_invalid_command`: Garante que comandos inválidos gerem erros apropriados.
    -   `test_empty_command_list`: Verifica se uma lista de comandos vazia gera um erro.
    -   `test_non_list_input`: Garante que entradas que não sejam de lista gerem um erro.
-   **Testes de trem ( `test_train.py`)**
    
    -   `test_initial_position`: Verifica se a posição inicial do trem é zero.
    -   `test_move_right`: Garante que o trem se mova corretamente para a direita.
    -   `test_move_left`: Garante que o trem se mova corretamente para a esquerda.
    -   `test_max_movements`: Verifica se o trem não excede o limite de 50 movimentos.
    -   `test_max_consecutive_moves`: Garante que o trem gere um erro se fizer mais de 20 movimentos consecutivos na mesma direção.
    -   `test_execute_commands`: Verifica se o trem executa uma série de comandos e termina na posição correta.

## Para executar o projeto sem rodar os testes, você pode seguir os seguintes passos:

-   **Preparar o Ambiente** Certifique-se de que o ambiente virtual está ativado e que as dependências necessárias estão instaladas.

- **Executar o Script Principal** Para executar o projeto, você pode rodar o script principal que você acabou de criar:
   `python main.py`
   
 - **Executar Diferentes Conjuntos de Comandos** Você pode modificar a lista de comandos no `main.py` ou no interpretador interativo para testar diferentes cenários e ver como o trem reage a diferentes entradas.

## Contribuindo

Agradecemos contribuições da comunidade! Se você tiver sugestões para melhorar este projeto ou se encontrar algum bug, sinta-se à vontade para bifurcar o repositório e enviar um pull request. Para grandes mudanças, considere abrir um issue primeiro para discutir as mudanças propostas.

## Licença

Este projeto é licenciado sob a Licença MIT. 

