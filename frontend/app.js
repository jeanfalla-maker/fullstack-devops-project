const express = require('express');
const fetch = require('node-fetch');

const app = express();
const PORT = 3000;
const API_URL = process.env.API_URL || 'http://web:5000';

app.get('/', async (req, res) => {
  try {
    const response = await fetch(`${API_URL}/data`);
    const data = await response.json();
    
    let html = `
      <html>
      <head>
        <title>Frontend - Datos de la API</title>
        <style>
          body { font-family: Arial; margin: 40px; background: #f0f0f0; }
          h1 { color: #333; }
          .card { background: white; padding: 20px; margin: 10px; border-radius: 8px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
          .json { background: #282c34; color: #61dafb; padding: 15px; border-radius: 5px; }
        </style>
      </head>
      <body>
        <h1>🐳 Frontend Node.js - Datos de la API Flask</h1>
        <div class="card">
          <h2>Total usuarios: ${data.total}</h2>
        </div>
        <div class="card">
          <h2>Respuesta JSON de la API:</h2>
          <pre class="json">${JSON.stringify(data, null, 2)}</pre>
        </div>
        <div class="card">
          <a href="/insert"><button>Insertar nuevo usuario</button></a>
          <a href="/status"><button>Ver estado API</button></a>
        </div>
      </body>
      </html>
    `;
    res.send(html);
  } catch (e) {
    res.send(`<h1>Error conectando a la API: ${e.message}</h1>`);
  }
});

app.get('/insert', async (req, res) => {
  try {
    const response = await fetch(`${API_URL}/insert`);
    const data = await response.json();
    res.send(`
      <html><body>
        <h1>✅ ${data.mensaje}</h1>
        <p>ID insertado: ${data.id}</p>
        <a href="/">← Volver</a>
      </body></html>
    `);
  } catch (e) {
    res.send(`<h1>Error: ${e.message}</h1>`);
  }
});

app.get('/status', async (req, res) => {
  try {
    const response = await fetch(`${API_URL}/`);
    const data = await response.json();
    res.send(`
      <html><body>
        <h1>Estado de la API</h1>
        <pre>${JSON.stringify(data, null, 2)}</pre>
        <a href="/">← Volver</a>
      </body></html>
    `);
  } catch (e) {
    res.send(`<h1>Error: ${e.message}</h1>`);
  }
});

app.listen(PORT, () => {
  console.log(`Frontend corriendo en http://localhost:${PORT}`);
});
