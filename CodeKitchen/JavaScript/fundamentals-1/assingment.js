// Values and Variables
const country = "India";
const continent = "Asia";
let population = 103;

console.log('country : ' + country);
console.log('continent : '+ continent);
console.log('population : '+ population);

//Data Types
const isIsland = false;
let language;
console.log(typeof isIsland);
console.log(typeof population);
console.log(typeof country);
console.log(typeof language);

//let,const, var
language = 'Marathi';

//Basic Operators
let halfPopulation = population/2;
halfPopulation++;
console.log("half population : "+ halfPopulation);
const finlandPop = 6;
console.log("is population greater than finland? : "+ (population>finlandPop));
console.log("is population less than 33 million? : "+ (population<33));
let description = country + "is in "+continent+", and its "+population+" million people speak "+language;
console.log(description);

//Strings and template literals (ES6 feature)
console.log(`String \n
with multiple \n
lines`);

console.log(`String \n\
with multiple \n\
lines`);

console.log(`String
with multiple
lines`);

description = `${country} is in ${continent}, and its ${population} million people speak ${language}`;
console.log(description);
