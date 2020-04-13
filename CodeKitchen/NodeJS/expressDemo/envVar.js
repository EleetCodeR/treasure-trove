const express = require('express')
const app = express();

// Route-1
app.get('/', (req, res) => {
    res.send('Hello World!!');
});

// Route-2
app.get('/api/courses', (req, res) => {
    // send any object or access database.
    res.send([1, 2, 3]);
});


// app.listen(3000, () => console.log("Listening port 3000.."));
// hard coded port numbers do not work in production environment.
// as they are assigned dynamically in production env.
// for this we use environment variables.(env in which proess runs)

// global object -> process.
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening port ${port}`));
