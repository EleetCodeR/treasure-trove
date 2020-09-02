const Joi = require("joi"); // for input validation.
const express = require("express");
const app = express();

app.use(express.json());

const courses = [
  { id: 1, name: "course1" },
  { id: 2, name: "course2" },
  { id: 3, name: "course3" },
];

app.put("/api/courses/:id", (req, res) => {
  // lookup course
  //if not found -> 404: not found
  const course = courses.find((c) => c.id === parseInt(req.params.id));
  if (!course)
    res.status(404).send(`No such course with id:${req.params.id} found!`);

  //Validate course
  // if invalid -> 400: Bad request
  //input validation.

  //   const result = validateCourse(req.body);
  //using object destructuring instead

  const { error } = validateCourse(req.body);

  if (error) {
    //400 Bad request.
    res.status(400).send(error.details[0].message);
    return;
  }

  //update course\
  course.name = req.body.name;
  // Return the updated course.
  res.send(course);
});

function validateCourse(course) {
  const schema = {
    name: Joi.string().min(3).required(),
  };

  return Joi.validate(course, schema);
}

// global object -> process.
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening port ${port}`));
