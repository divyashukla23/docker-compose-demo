const express = require('express');
const mongoose = require('mongoose');

const app = express();

mongoose.connect('mongodb://db:27017/test')
  .then(() => console.log("Connected to DB"))
  .catch(err => console.log(err));

app.get('/', (req, res) => {
  res.send("Hello from Docker Compose 🚀");
});

app.listen(3000, "0.0.0.0", () => {
  console.log("Server running on port 3000");
});