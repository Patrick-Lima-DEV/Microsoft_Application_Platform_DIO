// Exemplo simples de aplicação Node.js para deploy no Azure App Service
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Olá, Azure App Service!');
});

app.listen(port, () => {
  console.log(`Aplicação rodando na porta ${port}`);
});
