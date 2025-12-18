const express = require('express');
const app = express();
const PORT = 5002;

app.get('/', (req, res) => {
    res.send('Welcome to my Node app!');
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});