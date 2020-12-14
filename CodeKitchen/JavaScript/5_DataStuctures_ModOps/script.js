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

// Conventional-way
const arr = [2, 3, 4];
const a = arr[0];
const b = arr[1];
const c = arr[2];

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
