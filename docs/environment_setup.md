# Ambiente Virtual e Dependências

Para facilitar o gerenciamento do ambiente Python, utilize um ambiente virtual e um arquivo `requirements.txt`.

## Criar Ambiente Virtual

1. Crie o ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Arquivo `requirements.txt`

Inclua as dependências necessárias no arquivo `requirements.txt`:

```
flask
unittest
```

Isso garante que o ambiente esteja configurado corretamente para desenvolvimento e testes.