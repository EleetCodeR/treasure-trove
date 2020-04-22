enum Role {
  ADMIN,
  READ_ONLY,
  AUTHOR,
}

// const person:{
//   name:string;
//   age:number;
//   nickname:string;
//   hobbies: string[];
//   role:[number,string];
// } =

const person = {
  name: "Boruto",
  age: 14,
  nickname: "Hokage's Son",
  hobbies: ["Ninjutsu", "Thaijutsu"],
  //role:[2,'student']
  role: Role.ADMIN,
};
console.log(person.name);
console.log(person.nickname);

let favActivities: string[];
favActivities = ["shadowClone Jutsu", "transportationJutsu"];

for (const hobby of person.hobbies) {
  console.log(hobby);
  console.log(hobby.toUpperCase);
}
