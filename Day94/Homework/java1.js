//for loops

console.log("For Loop task 1: Squares of numbers from 1 to 10");
for (let i = 1; i <= 10; i++) {
  console.log(${i}_squared_is_${i * i});
}

console.log("For Loop task 2: Numbers from 1 through 50");
for (let i = 1; i <= 50; i++) {
  console.log(i);
}


console.log("For Loop Example 3: Greeting each name in a list");
const names = ['ana', 'ben', 'carl', 'dana', 'eva'];
for (let i = 0; i < names.length; i++) {
  console.log(Hello,) (${names[i]}!);
}

console.log("For Loop Example 4: Numbers from 100 to 0, decrementing by 10");
for (let i = 100; i >= 0; i -= 10) {
  console.log(i);
}

console.log("For Loop task 5: Sum of even numbers in a list");
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 === 0) {
    sum += numbers[i];
  }
}

console.log(The_sum_of_even_numbers;${sum});