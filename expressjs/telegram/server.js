const express = require('express');
require('dotenv').config()

const bodyParser = require('body-parser');

const db = require('./db');
url = `mongodb://${process.env.DB_USER}:${process.env.DB_PASS}@${process.env.DB_HOST}:27017/${process.env.DB_NAME}`;
db(url);

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

