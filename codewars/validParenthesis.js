/**
 * Created by jsonmartin on 5/17/16.
 */
"use strict";
function validParentheses(str) {
  let tokenizer = /[()]/g, count = 0, token;
  while(token = tokenizer.exec(str), token !== null) {
    for(let i = 0; i < str.length; i++) {
      if(str[i] === '(') { count++; }
      else if(str[i] === ')') {
        count--;
        if(count < 0) { return false; }
      }
    }
  }
  return count === 0;
}

function validParenthesesOrig(parens) {
  if(parens.trim() === "") { return true; }
  let removed = false;
  for(let i = 0; i < parens.length - 1; i++) {
    if(parens[i] + parens[i + 1] === "()") {
      parens = parens.slice(0, i) + parens.slice(i+2);
      removed = true;
    }
  }
  console.log("Parens:", parens);
  if(removed) {
    return validParentheses(parens);
  } else {
    return false;
  }
}

let res = validParentheses( "(())((()())())" );//validParentheses( "()" );//validParentheses( "(())((()())())" );
console.log("Res:", res);