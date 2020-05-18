const Joi = require("joi"); // for input validation.
const express = require("express");
const app = express();

app.use(express.json());

const courses = [
  { id: 1, name: "course1" },
  { id: 2, name: "course2" },
  { id: 3, name: "course3" },
];

app.post("/api/courses", (req, res) => {
  //input validation.
  const schema = {
    name: Joi.string().min(3).required(),
  };
  const result = Joi.validate(req.body, schema);

  if (result.error) {
    //400 Bad request.
    res.status(400).send(result.error.details[0].message);
    return;
  }

  const course = {
    id: courses.length + 1,
    // assumming request body has an object and that object has a name property.
    // need to enble parsing of json objects (using a middleware)in body of request, as not enables by default by express.
    name: req.body.name,
  };
  courses.push(course);
  // by converntion sending newly created object back in response.
  res.send(course);
});

// global object -> process.
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening port ${port}`));
