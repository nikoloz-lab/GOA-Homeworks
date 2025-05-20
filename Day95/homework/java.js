// OBJECTS, PROPERTIES AND METHODS EXPLAINED 

/*
 * WHAT IS AN OBJECT?
 * An object in JavaScript is a collection of related data and/or functionality.
 * It's a container that can store data and functions that work with that data.
 * Objects are one of the core concepts in JavaScript (it's an object-oriented language).
 */

/*
 * WHAT IS A PROPERTY?
 * A property is a piece of data stored within an object.
 * Properties are essentially variables that belong to an object.
 * They represent the state or characteristics of the object.
 * Example: a person object might have properties like name, age, or height.
 */

/*
 * WHAT IS A METHOD?
 * A method is a function that belongs to an object.
 * Methods define the behaviors or actions that the object can perform.
 * They are essentially functions stored as object properties.
 * Example: a person object might have methods like walk(), talk(), or calculateBMI().
 */

//task1

const myself = {
    name: "Alex",
    surname: "Johnson",
    age: 28,
    occupation: "Software Developer",
    introduce: function() {
        return Hello, I'm${this.name} ${this.surname}, ${this.age} years old
    }
};

const familyMember = {
    name: "Emma",
    surname: "Johnson",
    age: 32,
    relation: "Sister",
    occupation: "Doctor",
    
    describe: function() {
      return This_is_my_${this.relation}, ${this.name}.  She_is_${this.age}_years_old.;     }
};


console.log("=== Printing the complete objects ===");
console.log(myself);
console.log(familyMember);

console.log("\n=== Printing individual properties ===");
console.log("My name:", myself.name);
console.log("My surname:", myself.surname);
console.log("My age:", myself.age);
console.log("My occupation:", myself.occupation);

console.log("Family member's name:", familyMember.name);
console.log("Family member's surname:", familyMember.surname);
console.log("Family member's age:", familyMember.age);
console.log("Family member's relation:", familyMember.relation);
console.log("Family member's occupation:", familyMember.occupation);

console.log("\n=== Changing properties and printing again ===");
myself.age = 29;  
myself.occupation = "Senior Developer";  

familyMember.age = 33;  
familyMember.occupation = "Surgeon";  

console.log(myself);
console.log(familyMember);

console.log("=== Adding new attributes and printing again ===");
myself.hobbies = ["programming", "hiking", "reading"];
myself.isMarried = false;

familyMember.hobbies = ["medicine", "swimming", "painting"];
familyMember.children = 2;

console.log(myself);
console.log(familyMember);

console.log("=== Deleting attributes and printing again ===");
delete myself.isMarried;
delete familyMember.children;

console.log(myself);
console.log(familyMember);

//task2

console.log("=== Creating object from user input ===");

const firstName = "Sarah";  
const lastName = "Smith";   
const userAge = 31;         

const user = {
    name: firstName,
    lastName: lastName,
    age: userAge
};

console.log("Original user object:", user);

user.name = "Rebecca";

console.log("Modified user object:", user);

//taszk3
console.log("\n=== Object Reference Explanation ===");

const me = {
    name: "Nika",
    age: 20
};

const you = me;  
you.age = 25;    

console.log("me.age:", me.age);  

/*
 * WHY DID THE me OBJECT CHANGE?
 * 
 * This happens because in JavaScript, objects are reference types.
 * When you assign an object to a new variable (const you = me),
 * you're not creating a copy of the object. Instead, both variables
 * are pointing to the same object in memory.
 * 
 * When you modify a property through either reference (you.age = 25),
 * you're modifying the single shared object, which both variables reference.
 * 
 * To create an actual copy instead of a reference, you could use:
 * - Object.assign({}, me)
 * - {...me} (spread operator)
 * - JSON.parse(JSON.stringify(me)) (deep copy for nested objects)
 */

const meCopy = {...me}; 
meCopy.age = 30;         

console.log("After proper copying:");
console.log("me.age:", me.age);     
console.log("meCopy.age:", meCopy.age); 