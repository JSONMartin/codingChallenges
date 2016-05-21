/**
 * Created by jsonmartin on 5/19/16.
 */
"use strict";
function strNumber(inputStr, equals) {
  var a = new Date();
  console.log("Started at:", a);

  let results = [];
  function stringNumberCalc(str, equals, partial) {
    let strArr = str.split('');
    partial = partial || "";
    //console.log(partial);

    if(strArr.length === 0 && partial.replace(/[^\w\s]/gi, '') === inputStr) { //Base case, all digits exhausted, try partial
      if(eval(partial) === equals) {
        if(results.indexOf(partial) === -1) { results.push(partial); }
      }
    }

    for(let i = 0; i < strArr.length; i++) {
      let curNum = strArr[i];
      if(partial === "") {
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, curNum);
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, curNum);
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, curNum);
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, curNum);
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, curNum);
      } else {
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, partial + "+" + curNum);
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, partial + "-" + curNum);
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, partial + "*" + curNum);
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, partial + "/" + curNum);
        stringNumberCalc(strArr.slice(i + 1).join(''), equals, partial + "" + curNum);
      }
    }
  }
  stringNumberCalc(inputStr, equals);
  console.log("Results:", results);
  console.log("Number of matches:", results.length);
  var b = new Date();
  var difference = (b - a) / 1000;
  console.log("Execution took:" + difference + " seconds");
  return results;
}
// strNumber('323', 3);
//strNumber('39845710',15);

strNumber('314159265358', 27182);
// 3 + 1 - 415 * 92 + 65358 = 27182
// 3 * 1 + 4 * 159 + 26535 + 8 = 27182
// 3 / 1 + 4 * 159 + 26535 + 8 = 27182
// 3 * 14 * 15 + 9 + 26535 + 8 = 27182
// 3141 * 5 / 9 * 26 / 5 * 3 - 5 * 8 = 27182

//strNumber('4321',4);