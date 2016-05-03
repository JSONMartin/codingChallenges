/**
 * Created by jsonmartin on 5/3/16.
 */
Math.round = function(number) {
  if(number - parseInt(number) >= .5) { return parseInt(number)+1; }
  else { return parseInt(number); }
};

Math.ceil = function(number) {
  if(number - parseInt(number) === 0) { return parseInt(number); }
  else { return parseInt(number) + 1; }
};

Math.floor = function(number) {
  return parseInt(number);
};

/*
ES6 arrow function solution:

 Math.floor = number => parseInt(number)
 Math.round = number => Math.floor(number + 0.5)
 Math.ceil  = number => Number.isInteger(number) ? number : Math.floor( number + 1 )
 */