const spawner = require('child_process').spawn;

//string
const name = 'Aaron';

const python_process = spawner('python', ['../py/helloWorld.py', name]);

python_process.stdout.on('data', (data) => {
    console.log(`Data from helloWorld.py: ${data.toString()}`)
});