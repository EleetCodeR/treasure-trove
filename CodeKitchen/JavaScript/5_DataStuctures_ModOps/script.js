'use strict';

const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],

  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },

  order: function (starters, mainCourse) {
    return [this.starterMenu[starters], this.mainMenu[mainCourse]];
  },
};

//#region  --------------- Destructuring-Arrays--------------------------
// Conventional-way
const arr = [2, 3, 4];
const A = arr[0];
const B = arr[1];
const C = arr[2];

// Array Destructuring
// #1 unpacking
const [x, y, z] = arr;
console.log(x, y, z); // 2 3 4

// #2 unpacking
let [main, , secondary] = restaurant.categories;
console.log(main, secondary); // Italian Vegetarian

// # swapping with unpacking
[main, secondary] = [secondary, main];
console.log(main, secondary); // Vegetarian Italian

// # returning mutiple values from function and immediate unpacking.
const [starter, mainCourse] = restaurant.order(2, 0);
console.log(starter, mainCourse); // Garlic bread Pizza

// nested destructuring :
const nested = [2, 4, [5, 6]];
// const [i, , j] = nested;
const [i, , [j, k]] = nested;
console.log(i, j, k); // 2 5 6

// setting default values during unpacking
const [p = 1, q = 1, r = 1] = [8, 9];
console.log(p, q, r); // 8 9 1
//#endregion

//#region  --------------- Destructuring-Objects--------------------------

// basic object destructuring
const { name, openingHours, categories } = restaurant;
console.log(name, openingHours, categories);

// unpacking into different variable names than property names.
const {
  name: restaurantName,
  openingHours: workHours,
  categories: tags,
} = restaurant;
console.log(restaurantName, workHours, tags);

// Default Values
// Setting default values while unpacking (specially useful when we don't know data.)
const {
  menu = [], // a property that does not exist in object set to default value- []
  defvalue = 'default', // a property that does not exist in object set to default value- 'default'
  starterMenu: starters = [],
} = restaurant;
console.log(menu, defvalue, starters);

// Mutating variables
let a = 100;
let b = 200;
const obj = { a: 20, b: 30, c: 40 };
// can not do -

// const {a,b} = obj ;

// as a and b are already defined.and we want to mutate them.

// also {a,b} = obj

// fails as due to curly braces JS assumes block scope and gives error due to = sign
// therefore a way around is that we put above statement into parenthesis.
({ a, b } = obj);
console.log(a, b); // 20 30

// unpacking nested objects:
const {
  fri: { open, close },
} = openingHours;

console.log(open, close);

// rename while nested unpack
const {
  fri: { open: o, close: c },
} = openingHours;

console.log(o, c);

//#endregion
