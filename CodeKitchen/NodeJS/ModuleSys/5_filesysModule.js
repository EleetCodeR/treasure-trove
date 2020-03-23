const fs = require('fs');
// Synchronus method
const files = fs.readdirSync('./');
console.log(files);

//Asych form,
fs.readdir('./', function (err, files) {
    if (err) console.log('Error :', err);
    else console.log('Result:', files);
});

// with error
fs.readdir('$', function (err, files) {
    if (err) console.log('Error :', err);
    else console.log('Result:', files);
});

// we always use asychronous methods