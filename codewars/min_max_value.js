// https://www.codewars.com/kata/577a98a6ae28071780000989/solutions/javascript

"use strict";
// Spread solution
const min = (list) => Math.min(...list)
const max = (list) => Math.max(...list)
// Reduce solution
//const min = (list) => list.reduce((prev, cur) => (cur < prev) ? cur : prev);
//const max = (list) => list.reduce((prev, cur) => (cur > prev) ? cur : prev);

//Tests
let res = max([2, 4, -1, 9])
console.log(res)
