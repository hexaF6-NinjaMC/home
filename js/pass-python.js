const spawner = require('child_process').spawn;
const express = require('express');

const app = express();
const API_PORT = process.env.PORT || 3000;

//string
const name = 'Aaron';

const python_process = spawner('python', ['../py/helloWorld.py', name]);

python_process.stdout.on('data', (data) => {
    console.log(`Data from helloWorld.py: ${data.toString()}`)
});