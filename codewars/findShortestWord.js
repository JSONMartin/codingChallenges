// https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/javascript

let findShort = s => s.split(' ').reduce((prev, cur) => Math.min(cur.length, prev), Infinity);

findShort = s => Math.min(...s.split(" ").map(w => w.length)); // Spread operator solution

// Testing
let res = findShort("bitcoin take over the world maybe who knows perhaps")//, 3;
console.log(res);