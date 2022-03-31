const express = require('express');
const bodyParser = require('body-parser');

const router = require('./network/routes');
// import express from 'express'; //ES6

var app = express();
app.use(bodyParser.json());
// app.use(router);

router(app);

const PORT = 3000;

app.use('/app', express.static('public'));

app.listen(PORT);

console.log('Running on http://localhost:'+PORT);

