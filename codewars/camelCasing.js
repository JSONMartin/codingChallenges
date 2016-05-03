'use strict';

function solution(string) {
  let stringArr = string.split("");
  console.log(stringArr);
  for(let idx = 0; idx < stringArr.length; idx++) {
    let letter = stringArr[idx];
    if( letter.toUpperCase() === letter ) {
      stringArr.splice(idx++,0," ");
    }
  }
  return stringArr.join("");
}

let res1 = solution("asdfLol");
console.log(res1);