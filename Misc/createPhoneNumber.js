const createPhoneNumber = (numbers) => `(${numbers.slice(0,3).join("")}) ${numbers.slice(3, 6).join("")}-${numbers.slice(6).join("")}`;



// Tests
let res= createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
console.log(res);
//Test.assertEquals(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890");