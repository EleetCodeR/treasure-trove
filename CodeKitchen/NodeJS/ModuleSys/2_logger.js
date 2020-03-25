// ====== after 6_eventModule
// lets raise and handle events,
const EventEmitter = require('events');
const emitter = new EventEmitter();
// after 6_eventModule ====== 

var url = 'http://mylogger.io/log';

function log(message) {
    // code to send HTTP request.
    console.log(message);

    // ====== after 6_eventModule
    // raise event,
    message = 'Event:logged a message!!';
    emitter.emit("logging", message);
    // after 6_eventModule ====== 
};

// ====== to be able to access this function outside of this module,
// ====== we must export it using exports property of module object as shown,
// module.exports.log = log;
// module.exports.endPoint = url;  // (we can export with different identifier)

//  ====== export as an object with method.
// module.exports.log = log;

//====== exporting as a single method,
module.exports = log;

console.log(__filename);
console.log(__dirname);





