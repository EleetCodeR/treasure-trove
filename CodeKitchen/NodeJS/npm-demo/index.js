var _ = require("underscore");
// require functions resolution order:
// Core module -> 
// File/Folder -> 
// node_modules (as in here.)

var result = _.contains([1, 2, 3], 2)
console.log(result);
