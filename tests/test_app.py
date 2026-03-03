# Testes Automatizados

Este arquivo contém um exemplo de teste automatizado para a aplicação Python usando `unittest`.

## Exemplo de Teste

```python
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Olá, Azure! Aplicação Python funcionando.")

if __name__ == '__main__':
    unittest.main()
```

## Como Executar os Testes

1. Certifique-se de que o `unittest` está disponível (já incluído no Python).
2. Execute o comando:
   ```bash
   python -m unittest discover tests
   ```