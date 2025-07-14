const express = require('express');
const path = require('path');
const app = express();

// Serve static files from 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

const PORT = 3000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend running on http://0.0.0.0:${PORT}`);
});
