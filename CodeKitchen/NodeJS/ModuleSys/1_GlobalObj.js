// console.log(); // global
// console object is a type of global object. (Global Scope.)

// similarly following are properties of global object ,
// setTimeout()
// clearTimeout()
// setInterval()
// clearInterval()

// in NODE we have "global" obj which can be,
// used to access all such global functions and objects.
//global.console.log()
// but variables or functions such as below can not be accessed using this.
// not added into global scope, (file/module scope)
var message = '';
console.log(global.message);

// in browser we have window object that represents global scope.
//window.console.log()
//window.setTimeout()
// var message =''
// above variables is also accesible via window object inside the browser.

