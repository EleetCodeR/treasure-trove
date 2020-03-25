const EventEmitter = require('events');

class Logger extends EventEmitter {
    log(message) {
        // code to send HTTP request.
        console.log(message);

        // raise event,
        message = 'Event:logged a message!!';
        this.emit("logging", message);

    }
}

module.exports = Logger;// expose the class itself.