// peopleWithAgeDrink(13) === "drink toddy"
// peopleWithAgeDrink(17) === "drink coke"
// peopleWithAgeDrink(18) === "drink beer"
// peopleWithAgeDrink(20) === "drink beer"
// peopleWithAgeDrink(30) === "drink whisky"
// Children under 14 old.
//   Teens under 18 old.
//   Young under 21 old.
//   Adults have 21 or more.

"use strict";
const peopleWithAgeDrink = (age) => "drink " + (age < 14 ? "toddy" : age < 18 ? "coke" : age < 21 ? "beer" : "whisky");

// function peopleWithAgeDrink(age) {
//   console.log("Age:", age);
//   if(age < 14) {
//     return "drink toddy";
//   }
//   else if(14 <= age && age < 18) {
//     return "drink coke";
//   }
//   else if(18 <= age && age < 21) {
//     return "drink beer";
//   }
//   else if(age >= 21) {
//     return "drink whisky";
//   }
// }