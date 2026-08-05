var express = require('express');
var app = express();

app.set('view engine', 'ejs');

const URL = process.env.BACKEND_URL || 'http://localhost:8000/api';

app.get('/', async (req, res) => {
    const response = await fetch(URL);
    const data = await response.json();

    const safeData = Array.isArray(data) ? data : [data];

    res.render('index', { data: safeData });
});

app.listen(3000, () => {
    console.log('Frontend is running on port 3000');
});