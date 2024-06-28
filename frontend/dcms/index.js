const express = require('express');
const cors = require('cors');
const connection = require('../dcms/backend/connection');
//const tb_dentistRoute = require('./routes/tb_dentist');
const app = express();

app.use(cors());
app.use(express.urlencoded({extended: true}));
app.use(express.json());
//app.use('/tb_dentist',tb_dentistRoute);

module.exports = app;