// prints the details of module object.
console.log(module);

// loading a module,
// var logger = require('./logger')
// better to use const to avoid overwritting.
const logger = require('./2_logger')
console.log(logger);

//====== when exported as an object
//logger.log('Printed via module')

//====== when exported as a method
logger('-- Printed via module --')