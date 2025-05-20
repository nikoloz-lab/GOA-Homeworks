function Person(name, lastname, age) {
  this.name = name;
  this.lastname = lastname;
  this.age = age;
}

const person1 = new Person("ledi", "parker", 32);
const person2 = new Person("Emily", "ssvinkia", 28);
const person3 = new Person("Miguel", "o'hara", 45);

console.log("Person 1:", person1);
console.log("Person 2:", person2);
console.log("Person 3:", person3);