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

// Route-3 with parameters
app.get('/api/courses/:id', (req, res) => {
    res.send(req.params.id)
});

// Route-4 with multiple-parameters
app.get('/api/posts/:year/:month', (req, res) => {
    res.send(req.params);
});
// call : /api/posts/2018/1

// Route-5 reading Query parameters
app.get('/api/posts/:year/:month', (req, res) => {
    res.send(req.query);
});
// call : /api/posts/2018/1?sortBy=name

// all related routes can be placed in a single js files.
app.listen(3000, () => console.log("Listening port 3000.."));