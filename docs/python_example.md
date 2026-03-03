# Exemplo de Aplicação Python para Azure

Este exemplo demonstra como criar uma aplicação simples em Python usando Flask e prepará-la para deploy no Azure App Service.

## Código

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Azure! Aplicação Python funcionando."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Passos para Deploy

1. Certifique-se de que o Flask está instalado:
   ```bash
   pip install flask
   ```

2. Teste a aplicação localmente:
   ```bash
   python app.py
   ```

3. Crie um arquivo `requirements.txt` com as dependências:
   ```txt
   flask
   ```

4. Faça o deploy no Azure App Service seguindo as instruções da documentação oficial.