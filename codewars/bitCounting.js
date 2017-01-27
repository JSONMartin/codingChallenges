// https://www.codewars.com/kata/bit-counting/train/javascript

/*
 Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in
 the binary representation of that number.

 Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
 */

const countBits = (n) => n.toString(2).split("").reduce((counter, number) => (number === '1' ? counter + 1 : counter), 0);


let res = countBits(1234);
console.log(res);