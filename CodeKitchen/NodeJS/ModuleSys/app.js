// ====== after 6_eventModule
// lets raise and handle events,
const EventEmitter = require('events');
const emitter = new EventEmitter();
// after 6_eventModule ====== 


// prints the details of module object.
console.log(module);

// loading a module,
// var logger = require('./logger')
// better to use const to avoid overwritting.
const logger = require('./2_logger');
console.log(logger);

//====== when exported as an object
//logger.log('Printed via module')

//====== when exported as a method
// logger('-- Printed via module --')

// // register event
// emitter.on("logging", (message) => {
//     console.log('logging...\nmessage :', message);
// });

// logger(' => remote logger called')

// the reason for why the above listener was not called is that ,
// we must register event lister on same emitter object which raised the event.,
// as here logger and app module have two different emitters, event was not handled.
// hence we always create a single class for handling events.

// ====== after 7_loggerClass.js ======
const Logger = require('./7_loggerClass');
const loggerCl = new Logger();
// register event
loggerCl.on("logging", (message) => {
    console.log('logging...\nmessage :', message);
});
loggerCl.log(' => remote logger called');
