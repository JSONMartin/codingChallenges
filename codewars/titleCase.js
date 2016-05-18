/**
 * Created by jsonmartin on 5/16/16.
 */
"use strict";
String.prototype.capitalize = function() {
  return this[0].toUpperCase() + this.slice(1);
};

const titleCase = (title, minorWords) => {
  minorWords = (typeof minorWords !== 'undefined') ? minorWords.toLowerCase().split(" ") : [];
  return title.toLowerCase().split(' ').map((item, index) => {
    if (index > 0 && minorWords.indexOf(item) > -1) {
      return item
    } else {
      return item.capitalize();
    }
  }).join(' ');
};

const titleCaseOriginal = (title, minorWords) => {
  if (minorWords) { minorWords = minorWords.split(' ').map((word) => word.toUpperCase()); }
  let titleArr = title.split(' ');
  titleArr.forEach((word, index) => {
    if(minorWords && minorWords.indexOf(word.toUpperCase()) > -1 && index > 0) {
      titleArr[index] = word.toLowerCase();
    } else {
      titleArr[index] = word.substring(0, 1).toUpperCase() + word.substring(1).toLowerCase();
    }
  });
  return titleArr.join(' ');
};

let res = titleCaseRefactored("a bc the an defg", "an the of");
console.log(res);