const EventEmitter = require('events');
// class named should be pascal case.
const emitter = new EventEmitter();

// Register a Listener to listen to event first.
// we can also pass arguments (eventArgs) to call back function as shown.

// emitter.on('messageLogged', function (eventArg) {
//     console.log('Listener is called.', eventArg);

// });
// we can also use addlistener method same as "on"


// Using arrow function as per ES6
emitter.on('messageLogged', (eventArg) => {
    console.log('Listener is called.', eventArg);

});


// Raise an event; named "messageLogged" and pass some data.
emitter.emit('messageLogged', { id: 10, url: "http://google.com" });