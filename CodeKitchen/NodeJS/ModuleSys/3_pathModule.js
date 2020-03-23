const path = require('path');

var pathObj = path.parse(__filename);
var dirObj = path.parse(__dirname);
console.log(pathObj);
console.log(dirObj);