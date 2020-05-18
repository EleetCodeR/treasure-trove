const express = require("express");
const app = express();

const courses = [
  { id: 1, name: "course1" },
  { id: 2, name: "course2" },
  { id: 3, name: "course3" },
];
// Route-1
app.get("/", (req, res) => {
  res.send("Hello World!!");
});

// Route-2
app.get("/api/courses", (req, res) => {
  // send any object or access database.
  res.send(courses);
});

// Route-3 with parameters
app.get("/api/courses/:id", (req, res) => {
  const course = courses.find((c) => c.id === parseInt(req.params.id));
  if (!course)
    res.status(404).send(`No such course with id:${req.params.id} found!`);
  res.send(course);
});

// app.listen(3000, () => console.log("Listening port 3000.."));
// hard coded port numbers do not work in production environment.
// as they are assigned dynamically in production env.
// for this we use environment variables.(env in which proess runs)

// global object -> process.
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening port ${port}`));
