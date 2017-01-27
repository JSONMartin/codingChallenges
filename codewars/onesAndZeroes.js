// https://www.codewars.com/kata/ones-and-zeros/train/javascript

const binaryArrayToNumber = arr => parseInt(arr.join(''), 2);

let res = binaryArrayToNumber([1, 0, 0, 0]);
console.log(res);