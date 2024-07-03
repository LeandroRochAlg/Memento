# Padrões de Projeto com Tkinter

Este repositório contém exemplos de uso dos padrões de projeto **Memento** e **Interpreter**, implementados com Tkinter para criar interfaces gráficas.

## Memento Pattern

O padrão Memento é usado para capturar e restaurar o estado interno de um objeto sem violar seu encapsulamento. Neste exemplo, criamos um editor de texto simples que permite desfazer e refazer alterações.

### Funcionalidades:
- Digitar texto
- Salvar o estado atual
- Desfazer alterações
- Refazer alterações

### Como Executar:
1. Certifique-se de ter o Python e Tkinter instalados.
2. Execute o script `memento.py`:
    ```bash
    python memento.py
    ```

## Interpreter Pattern

O padrão Interpreter é usado para interpretar linguagens específicas. Neste exemplo, criamos um interpretador de expressões aritméticas simples com uma interface gráfica.

### Funcionalidades:
- Digitar expressões aritméticas
- Avaliar e mostrar o resultado

### Como Executar:
1. Certifique-se de ter o Python e Tkinter instalados.
2. Execute o script `interpreterpy`:
    ```bash
    python interpreter.py
    ```

## Requisitos

- Python 3.x
- Tkinter (geralmente incluído na instalação padrão do Python)

## Como Instalar

### No Windows:
O Tkinter geralmente vem pré-instalado com o Python. Se não estiver instalado, você pode usar:
```bash
pip install tk
```

### No macOS:
Tkinter também vem pré-instalado com o Python no macOS. Se necessário, você pode usar:
```bash
brew install python-tk
```

### No Linux:
No Linux, você pode instalar Tkinter usando o gerenciador de pacotes da sua distribuição. Para Debian/Ubuntu, use:
```bash
sudo apt-get install python3-tk
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---