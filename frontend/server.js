const express = require('express');
const path = require('path');
const app = express();

// Serve static files from 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// Listen on all interfaces so it's accessible from EC2 public IP
app.listen(3000, '0.0.0.0', () => {
  console.log('Frontend running on http://<your-ec2-public-ip>:3000');
});

