const os = require('os');

var totalMemory = os.totalmem();
var freeMemory = os.freemem();
// concatenation;
console.log('Total Memory:' + totalMemory);

// instead of concat, use 'Template-String' feature.(ES6)
console.log(`Total Memory:${totalMemory}`);// use back tick instead of quotes.
console.log(`Free Memory:${freeMemory}`);// use back tick instead of quotes.
